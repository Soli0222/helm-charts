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
| [dayspassed-bot](#dayspassed-bot) | 0.1.0 | 1.0.0 | A Kubernetes CronJob for days passed bot |
| [flow-sight](#flow-sight) | 1.1.0 | 1.1.0 | Flow-Sight application for workflow visualization |
| [mc-mirror-job](#mc-mirror-job) | 0.2.0 | RELEASE.2025-07-21T05-28-08Z | MinIO Client mirror CronJob |
| [mk-stream](#mk-stream) | 1.0.0 | 2.0.0 | Streaming application |
| [navidrome](#navidrome) | 1.0.0 | 0.58.0 | Modern Music Server and Streamer |
| [note-tweet-connector](#note-tweet-connector) | 0.3.0 | 1.7.1 | Connector between note-taking and Twitter |
| [spotify-nowplaying](#spotify-nowplaying) | 1.0.0 | 2.3.0 | Spotify Now Playing status display |
| [subscription-manager](#subscription-manager) | 1.1.0 | 1.0.0 | Subscription management application |

## Chart Details

### dayspassed-bot

A Kubernetes CronJob that runs a bot to track days passed since a specific date.

```bash
helm install dayspassed-bot soli0222/daypassed-bot
```

### flow-sight

A web application for visualizing workflows and data flows.

```bash
helm install flow-sight soli0222/flow-sight
```

### mc-mirror-job

A CronJob that uses MinIO Client (mc) to mirror data between storage systems.

```bash
helm install mc-mirror soli0222/mc-mirror-cronjob
```

### mk-stream

A streaming application for real-time data processing.

```bash
helm install mk-stream soli0222/mk-stream
```

### navidrome

A modern Music Server and Streamer compatible with Subsonic/Airsonic clients.

Features:
- Web-based music streaming
- Multiple format support
- User management
- Scrobbling support
- Mobile app compatibility

```bash
helm install navidrome soli0222/navidrome
```

### note-tweet-connector

A service that connects note-taking applications with Twitter for automated posting.

```bash
helm install note-tweet-connector soli0222/note-tweet-connector
```

### spotify-nowplaying

Displays current Spotify playing status with web interface.

```bash
helm install spotify-nowplaying soli0222/spotify-nowplaying
```

### subscription-manager

A web application for managing various subscriptions and recurring payments.

```bash
helm install subscription-manager soli0222/subscription-manager
```

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
