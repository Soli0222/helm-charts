# Soli0222 Helm Charts

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Helm](https://img.shields.io/badge/Helm-v3-informational?logo=helm)](https://helm.sh/)

A collection of Helm charts for various applications and services.

> [!IMPORTANT]
> **このリポジトリは役目を終えました。アーカイブされています。**
>
> ここにあった chart はすべて移設済みです。新しい場所は次のとおりです。
>
> | chart | 移設先 |
> |-------|--------|
> | `daypassed-bot`, `emoji-bot-gateway`, `emoji-renderer`, `mk-stream`, `note-tweet-connector`, `rss-fetcher`, `spotify-nowplaying`, `spotify-reblend` | 各アプリのリポジトリの `charts/` → `oci://ghcr.io/soli0222/charts` |
> | `sui` | [Soli0222/sui](https://github.com/Soli0222/sui) の `charts/sui/` → `oci://ghcr.io/soli0222/charts` |
> | `blackbox-exporter-probes`, `distribution`, `mc-mirror-job` (= `mc-mirror-cronjob`), `mimir`, `misskey`, `navidrome`, `summaly` | [Soli0222/pke](https://github.com/Soli0222/pke) の `charts/` (Flux が GitRepository で直接参照) |
> | `mermaid-live-editor` | どこからも参照されていなかったため移設せず廃止 |
>
> GitHub Pages (`https://soli0222.github.io/helm-charts`) の Helm リポジトリは更新されません。
> OCI 配布のものは次のように参照します。
>
> ```bash
> helm install my-release oci://ghcr.io/soli0222/charts/<chart-name> -f values.yaml
> ```
>
> 以下は当時のドキュメントです。

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
| [distribution](#distribution) | 0.1.3 | 3.1.1 | A Helm chart for Distribution Registry - A stateless, highly scalable container image registry |
| [mc-mirror-cronjob](#mc-mirror-cronjob) | 1.0.0 | RELEASE.2025-07-21T05-28-08Z | A Helm chart for a Kubernetes CronJob that runs mc mirror |
| [mermaid-live-editor](#mermaid-live-editor) | 0.1.0 | latest | A Helm chart for Mermaid Live Editor - edit, preview and share mermaid charts/diagrams |
| [mimir](#mimir) | 0.1.6 | 3.1.4 | A Helm chart for Grafana Mimir running in monolithic mode |
| [misskey](#misskey) | 0.4.1 | 2026.7.0 | A Helm chart for Misskey - A decentralized social networking platform |
| [navidrome](#navidrome) | 2.5.0 | 0.63.2 | A Helm chart for Navidrome - A modern Music Server and Streamer |
| [sui](#sui) | 0.3.0 | 2.0.0-beta.3 | A Helm chart for the sui asset forecasting application |
| [summaly](#summaly) | 0.1.8 | 5.5.1-psr.4.3 | A Helm chart for Summaly |

