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
| [distribution](#distribution) | 0.1.1 | 3.0.0 | A Helm chart for Distribution Registry - A stateless, highly scalable container image registry |
| [emoji-bot-gateway](#emoji-bot-gateway) | 0.1.0 | 1.0.0 | A Helm chart for Emoji Bot Gateway - Misskey Streaming API based emoji generation bot |
| [emoji-renderer](#emoji-renderer) | 1.0.0 | 1.1.1 | A Helm chart for the Emoji Renderer Service - Misskey Custom Emoji image generation microservice |
| [flow-sight](#flow-sight) | 1.1.3 | 1.1.0 | A Helm chart for Flow-Sight application |
| [komga](#komga) | 1.0.4 | 1.24.1 | A Helm chart for Komga - A comic/manga server |
| [mc-mirror-cronjob](#mc-mirror-cronjob) | 0.2.1 | RELEASE.2025-07-21T05-28-08Z | A Helm chart for a Kubernetes CronJob that runs mc mirror |
| [mermaid-live-editor](#mermaid-live-editor) | 0.1.0 | latest | A Helm chart for Mermaid Live Editor - edit, preview and share mermaid charts/diagrams |
| [misskey](#misskey) | 0.1.1 | 2025.12.2 | A Helm chart for Misskey - A decentralized social networking platform |
| [misskey-summarizer](#misskey-summarizer) | 0.1.2 | 1.2.0 | A Helm chart for Misskey Summarizer CronJob |
| [mk-stream](#mk-stream) | 1.0.0 | 2.0.0 | A Helm chart for Kubernetes |
| [navidrome](#navidrome) | 2.0.1 | 0.59.0 | A Helm chart for Navidrome - A modern Music Server and Streamer |
| [note-tweet-connector](#note-tweet-connector) | 1.0.3 | 2.0.2 | A Helm chart for the Note Tweet Connector |
| [rss-fetcher](#rss-fetcher) | 0.1.1 | 1.1.0 | A Helm chart for RSS Fetcher application |
| [spotify-nowplaying](#spotify-nowplaying) | 3.0.1 | 4.2.0 | A Helm chart for the Spotify Now Playing application |
| [spotify-reblend](#spotify-reblend) | 0.1.2 | 1.1.1 | A Helm chart for Spotify ReBlend application |
| [subscription-manager](#subscription-manager) | 1.1.1 | 1.0.0 | A Helm chart for Subscription Manager application |
| [summaly](#summaly) | 0.1.6 | 5.2.3-psr.4.1 | A Helm chart for Summaly |
| [wallos](#wallos) | 0.1.4 | 4.6.0 | A Helm chart for Wallos subscription tracker |

