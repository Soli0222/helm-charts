# Soli0222 Helm Charts

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Helm](https://img.shields.io/badge/Helm-v3-informational?logo=helm)](https://helm.sh/)

A collection of Helm charts for various applications and services.

## Usage

### Adding the Helm Repository

```bash
helm repo add soli0222 https://soli0222.github.io/helm-charts
helm repo update
```

### Installing Charts

```bash
# Install a chart
helm install my-release soli0222/<chart-name>

# Install with custom values
helm install my-release soli0222/<chart-name> -f values.yaml

# Upgrade
helm upgrade my-release soli0222/<chart-name>

# Uninstall
helm uninstall my-release
```

## Available Charts

| Chart | Version | App Version | Description |
|-------|---------|-------------|-------------|
| [blackbox-exporter-probes](#blackbox-exporter-probes) | 1.0.0 | 1.0.0 | A Helm chart for deploying Prometheus Blackbox Exporter Probes. |
| [daypassed-bot](#daypassed-bot) | 0.1.0 | 1.0.0 | A Helm chart for deploying the daypassed-bot as a Kubernetes CronJob. |
| [flow-sight](#flow-sight) | 1.1.3 | 1.1.0 | A Helm chart for Flow-Sight application |
| [komga](#komga) | 1.0.1 | 1.23.5 | A Helm chart for Komga - A comic/manga server |
| [mc-mirror-cronjob](#mc-mirror-cronjob) | 0.2.1 | RELEASE.2025-07-21T05-28-08Z | A Helm chart for a Kubernetes CronJob that runs mc mirror |
| [mk-stream](#mk-stream) | 1.0.0 | 2.0.0 | A Helm chart for Kubernetes |
| [navidrome](#navidrome) | 2.0.0 | 0.58.5 | A Helm chart for Navidrome - A modern Music Server and Streamer |
| [note-tweet-connector](#note-tweet-connector) | 0.3.0 | 1.7.1 | A Helm chart for the Note Tweet Connector |
| [spotify-nowplaying](#spotify-nowplaying) | 1.0.0 | 2.3.0 | A Helm chart for the Spotify Now Playing application |
| [subscription-manager](#subscription-manager) | 1.1.1 | 1.0.0 | A Helm chart for Subscription Manager application |
| [summaly](#summaly) | 0.1.6 | 5.2.3-psr.4.1 | A Helm chart for Summaly |
| [wallos](#wallos) | 0.1.3 | 4.5.0 | A Helm chart for Wallos subscription tracker |

For detailed configuration options and features, please refer to each chart's individual README.

## Development

### Prerequisites

- [Helm](https://helm.sh/) 3.x
- [helm-docs](https://github.com/norwoodj/helm-docs) (optional, for documentation generation)

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Soli0222/helm-charts.git
cd helm-charts
```

2. Make your changes to the charts

3. Test your changes:
```bash
# Lint the chart
helm lint charts/<chart-name>

# Test template rendering
helm template test charts/<chart-name>

# Test installation (dry-run)
helm install test charts/<chart-name> --dry-run --debug
```

### Chart Structure

Each chart follows the standard Helm chart structure:

```
charts/<chart-name>/
├── Chart.yaml          # Chart metadata
├── README.md           # Chart documentation
├── values.yaml         # Default values
└── templates/          # Kubernetes manifest templates
    ├── _helpers.tpl    # Template helpers
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── ...
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines

- Follow [Helm best practices](https://helm.sh/docs/chart_best_practices/)
- Update chart version when making changes
- Include comprehensive documentation
- Test your changes thoroughly
- Follow [semantic versioning](https://semver.org/) for chart versions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Create an issue for bug reports or feature requests
- Discussions can be held in the repository's discussions section
- Check individual chart README files for specific configuration options

## Acknowledgments

- [Helm](https://helm.sh/) for the package manager
- [Kubernetes](https://kubernetes.io/) for the container orchestration platform
- All the open-source applications packaged in these charts
