#!/usr/bin/env python3
"""
Auto-update README.md with latest chart information from Chart.yaml files.

This script:
1. Scans all charts in the charts/ directory
2. Extracts version and appVersion from Chart.yaml
3. Extracts description from Chart.yaml
4. Updates the "Available Charts" table in README.md
"""

import os
import re
from pathlib import Path
import yaml


def get_chart_info(chart_path):
    """Extract chart information from Chart.yaml"""
    chart_yaml = chart_path / "Chart.yaml"
    if not chart_yaml.exists():
        return None
    
    with open(chart_yaml, 'r', encoding='utf-8') as f:
        chart_data = yaml.safe_load(f)
    
    return {
        'name': chart_data.get('name', ''),
        'version': chart_data.get('version', ''),
        'appVersion': chart_data.get('appVersion', ''),
        'description': chart_data.get('description', '')
    }


def get_all_charts(charts_dir):
    """Get information for all charts"""
    charts = []
    charts_path = Path(charts_dir)
    
    for chart_dir in sorted(charts_path.iterdir()):
        if chart_dir.is_dir() and not chart_dir.name.startswith('.'):
            info = get_chart_info(chart_dir)
            if info:
                charts.append(info)
    
    return charts


def generate_table(charts):
    """Generate markdown table for charts"""
    if not charts:
        return ""
    
    lines = [
        "| Chart | Version | App Version | Description |",
        "|-------|---------|-------------|-------------|"
    ]
    
    for chart in charts:
        name = chart['name']
        version = chart['version']
        app_version = chart['appVersion']
        description = chart['description']
        
        # Create link to chart section (assuming kebab-case anchors)
        anchor = name.lower().replace('_', '-')
        name_link = f"[{name}](#{anchor})"
        
        lines.append(f"| {name_link} | {version} | {app_version} | {description} |")
    
    return "\n".join(lines)


def update_readme(readme_path, charts_dir):
    """Update README.md with latest chart information"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get all charts
    charts = get_all_charts(charts_dir)
    
    # Generate new table
    new_table = generate_table(charts)
    
    # Find and replace the table section
    # Pattern: from "## Available Charts" to the next "##" or end of content
    pattern = r'(## Available Charts\s*\n\n)(\|.*?\n)*(\|.*?\n)+(.*?)(?=\n## |\Z)'
    
    replacement = f'## Available Charts\n\n{new_table}\n\n'
    
    # Try to replace the table
    new_content = re.sub(
        pattern,
        replacement,
        content,
        flags=re.MULTILINE | re.DOTALL
    )
    
    # If pattern didn't match, try a simpler pattern
    if new_content == content:
        pattern2 = r'## Available Charts.*?(?=\n## Chart Details|\Z)'
        new_content = re.sub(
            pattern2,
            replacement.rstrip() + '\n',
            content,
            flags=re.MULTILINE | re.DOTALL
        )
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated README.md with {len(charts)} charts")
    for chart in charts:
        print(f"   - {chart['name']} v{chart['version']} (app: {chart['appVersion']})")


def main():
    # Paths
    repo_root = Path(__file__).parent.parent
    readme_path = repo_root / "README.md"
    charts_dir = repo_root / "charts"
    
    if not readme_path.exists():
        print(f"❌ README.md not found at {readme_path}")
        return 1
    
    if not charts_dir.exists():
        print(f"❌ charts directory not found at {charts_dir}")
        return 1
    
    update_readme(readme_path, charts_dir)
    return 0


if __name__ == "__main__":
    exit(main())
