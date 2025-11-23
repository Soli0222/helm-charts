#!/usr/bin/env python3
"""
Auto-bump Helm chart versions based on changes detected in pull requests.

This script:
1. Detects which charts have been modified
2. Extracts the main application version from values.yaml
3. Updates Chart.yaml with new version and appVersion
4. Only bumps version if not already manually bumped
"""

import os
import sys
import subprocess
from pathlib import Path
import yaml


def run_cmd(cmd):
    """Run shell command and return output"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def get_changed_charts(base_branch):
    """Get list of charts that have been modified"""
    output = run_cmd(f"git diff --name-only origin/{base_branch}..HEAD")
    charts = set()
    for line in output.split('\n'):
        if line.startswith('charts/'):
            parts = line.split('/')
            if len(parts) >= 2:
                charts.add(parts[1])
    return sorted(charts)


def extract_app_version(values_path):
    """
    Extract main application tag from values.yaml.
    
    Priority order:
    1. backend.image.tag
    2. frontend.image.tag
    3. image.tag (top-level)
    
    This excludes dependency images like database.image.tag or initContainer.image.tag
    """
    with open(values_path, 'r') as f:
        data = yaml.safe_load(f)
    
    # Priority: backend > frontend > image
    if 'backend' in data and 'image' in data['backend'] and 'tag' in data['backend']['image']:
        return data['backend']['image']['tag'].strip('"\'')
    
    if 'frontend' in data and 'image' in data['frontend'] and 'tag' in data['frontend']['image']:
        return data['frontend']['image']['tag'].strip('"\'')
    
    if 'image' in data and 'tag' in data['image']:
        return data['image']['tag'].strip('"\'')
    
    return None


def bump_patch_version(version):
    """Increment patch version (e.g., 1.0.0 -> 1.0.1)"""
    parts = version.split('.')
    if len(parts) == 3:
        try:
            parts[2] = str(int(parts[2]) + 1)
            return '.'.join(parts)
        except ValueError:
            # If patch version is not a number, return as-is
            return version
    return version


def update_chart_yaml(chart_path, new_version=None, new_app_version=None):
    """Update Chart.yaml with new version and/or appVersion"""
    with open(chart_path, 'r') as f:
        lines = f.readlines()
    
    updated_lines = []
    for line in lines:
        if new_version and line.startswith('version:'):
            updated_lines.append(f'version: {new_version}\n')
        elif new_app_version and line.startswith('appVersion:'):
            updated_lines.append(f'appVersion: "{new_app_version}"\n')
        else:
            updated_lines.append(line)
    
    with open(chart_path, 'w') as f:
        f.writelines(updated_lines)


def main():
    base_branch = os.getenv('BASE_BRANCH', 'main')
    github_output = os.getenv('GITHUB_OUTPUT')
    
    changed_charts = get_changed_charts(base_branch)
    
    if not changed_charts:
        print("No charts changed")
        if github_output:
            with open(github_output, 'a') as f:
                f.write('charts_changed=false\n')
        return 0
    
    print(f"Changed charts: {changed_charts}")
    if github_output:
        with open(github_output, 'a') as f:
            f.write('charts_changed=true\n')
    
    bumped_charts = []
    
    for chart in changed_charts:
        chart_yaml_path = Path(f'charts/{chart}/Chart.yaml')
        values_yaml_path = Path(f'charts/{chart}/values.yaml')
        
        if not chart_yaml_path.exists():
            print(f"Skipping {chart} (no Chart.yaml found)")
            continue
        
        print(f"\nProcessing chart: {chart}")
        
        # Load Chart.yaml
        with open(chart_yaml_path, 'r') as f:
            chart_data = yaml.safe_load(f)
        
        current_version = chart_data.get('version', '0.0.0')
        current_app_version = str(chart_data.get('appVersion', '')).strip('"\'')
        
        print(f"  Current version: {current_version}")
        print(f"  Current appVersion: {current_app_version}")
        
        # Get base branch version
        base_chart = run_cmd(f"git show origin/{base_branch}:charts/{chart}/Chart.yaml")
        base_data = yaml.safe_load(base_chart) if base_chart else {}
        base_version = base_data.get('version', current_version)
        
        print(f"  Base version: {base_version}")
        
        needs_version_bump = False
        new_app_version = None
        
        # Check for changes in files other than Chart.yaml
        changed_files = run_cmd(f"git diff --name-only origin/{base_branch}..HEAD -- charts/{chart}/")
        non_chart_yaml_changes = [f for f in changed_files.split('\n') if f and not f.endswith('Chart.yaml')]
        
        if non_chart_yaml_changes:
            if current_version == base_version:
                print("  ✓ Chart files changed but version not bumped - will auto-bump")
                needs_version_bump = True
            else:
                print(f"  ✓ Version already bumped manually from {base_version} to {current_version}")
        
        # Check if values.yaml tag has changed
        if values_yaml_path.exists():
            values_diff = run_cmd(f"git diff origin/{base_branch}..HEAD -- {values_yaml_path}")
            if 'tag:' in values_diff:
                new_app_version = extract_app_version(values_yaml_path)
                if new_app_version and new_app_version != current_app_version:
                    print(f"  ✓ New appVersion from tag: {new_app_version}")
                    needs_version_bump = True
                else:
                    new_app_version = None
        
        # Apply updates
        if needs_version_bump:
            new_version = bump_patch_version(current_version)
            print(f"  → Bumping version: {current_version} -> {new_version}")
            if new_app_version:
                print(f"  → Updating appVersion: {current_app_version} -> {new_app_version}")
            update_chart_yaml(chart_yaml_path, new_version, new_app_version)
            bumped_charts.append(chart)
        else:
            print("  ✗ No version bump needed")
    
    if github_output:
        with open(github_output, 'a') as f:
            f.write(f'bumped_charts={" ".join(bumped_charts)}\n')
    
    print(f"\n{'='*60}")
    print(f"Summary: Bumped {len(bumped_charts)} chart(s): {bumped_charts}")
    print(f"{'='*60}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
