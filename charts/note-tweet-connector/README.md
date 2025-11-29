# note-tweet-connector

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.0.0](https://img.shields.io/badge/AppVersion-2.0.0-informational?style=flat-square)

A Helm chart for Note Tweet Connector - MisskeyとTwitter間でノートを自動的に連携するためのコネクタ

## 機能

- Misskeyで公開されたノートを自動的にTwitterに投稿
- TwitterのツイートをMisskeyにノートとして保存
- 画像付きノートのサポート（最大4枚まで）
- リノートの内容をツイートとして投稿
- 重複投稿を防ぐためのコンテンツトラッキング機能
- Prometheusメトリクスの公開
- Graceful Shutdown対応

## インストール

```bash
helm repo add soli0222 https://soli0222.github.io/helm-charts
helm repo update
helm install note-tweet-connector soli0222/note-tweet-connector -f values.yaml
```

## 前提条件

- Kubernetes 1.19+
- Helm 3.0+
- Twitter APIおよびMisskeyのAPIキー
- IFTTT Webhookの設定（テキストのみのツイート用）
- 外部Secretリソース（環境変数用）

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| nameOverride | string | `""` | Override the chart name |
| fullnameOverride | string | `""` | Override the full release name |
| image.repository | string | `"ghcr.io/soli0222/note-tweet-connector"` | Image repository |
| image.tag | string | `""` | Image tag (defaults to appVersion) |
| image.pullPolicy | string | `"IfNotPresent"` | Image pull policy |
| imagePullSecrets | list | `[]` | Image pull secrets |
| serviceAccount.create | bool | `true` | Create a service account |
| serviceAccount.annotations | object | `{}` | Service account annotations |
| serviceAccount.name | string | `""` | Service account name |
| podSecurityContext | object | `{}` | Pod security context |
| securityContext | object | `{}` | Container security context |
| replicaCount | int | `1` | Number of replicas |
| args.port | int | `8080` | Webhook server port |
| args.metricsPort | int | `9090` | Metrics server port |
| args.trackerExpiry | string | `"5h"` | Tracker expiry duration |
| args.readTimeout | string | `"15s"` | HTTP read timeout |
| args.writeTimeout | string | `"15s"` | HTTP write timeout |
| args.idleTimeout | string | `"60s"` | HTTP idle timeout |
| args.shutdownTimeout | string | `"30s"` | Graceful shutdown timeout |
| args.logLevel | string | `"info"` | Log level (debug, info, warn, error) |
| service.type | string | `"ClusterIP"` | Main webhook service type |
| service.port | int | `8080` | Main webhook service port |
| metricsService.enabled | bool | `true` | Enable separate metrics service |
| metricsService.type | string | `"ClusterIP"` | Metrics service type |
| metricsService.port | int | `9090` | Metrics service port |
| resources | object | `{}` | Resource limits and requests |
| nodeSelector | object | `{}` | Node selector |
| tolerations | list | `[]` | Tolerations |
| affinity | object | `{}` | Affinity rules |
| podAnnotations | object | `{}` | Pod annotations |
| podLabels | object | `{}` | Pod labels |
| ingress.enabled | bool | `false` | Enable ingress |
| ingress.className | string | `""` | Ingress class name |
| ingress.annotations | object | `{}` | Ingress annotations |
| ingress.hosts | list | `[{"host": "example.tld", "paths": [{"path": "/", "pathType": "ImplementationSpecific"}]}]` | Ingress hosts configuration |
| ingress.tls | list | `[]` | Ingress TLS configuration |
| secrets.secretName | string | `""` | Name of the external secret |
| secrets.env | list | See values.yaml | Environment variables from secret |
| env | list | `[]` | Additional environment variables |
| livenessProbe | object | See values.yaml | Liveness probe configuration |
| readinessProbe | object | See values.yaml | Readiness probe configuration |
| monitoring.serviceMonitor.enabled | bool | `false` | Enable ServiceMonitor creation |
| monitoring.serviceMonitor.namespace | string | `""` | ServiceMonitor namespace |
| monitoring.serviceMonitor.labels | object | `{}` | Additional ServiceMonitor labels |
| monitoring.serviceMonitor.annotations | object | `{}` | ServiceMonitor annotations |
| monitoring.serviceMonitor.interval | string | `"30s"` | Scrape interval |
| monitoring.serviceMonitor.scrapeTimeout | string | `"10s"` | Scrape timeout |
| monitoring.serviceMonitor.path | string | `"/metrics"` | Metrics path |
| monitoring.prometheusRule.enabled | bool | `false` | Enable PrometheusRule creation |
| monitoring.prometheusRule.namespace | string | `""` | PrometheusRule namespace |
| monitoring.prometheusRule.labels | object | `{}` | Additional PrometheusRule labels |
| monitoring.prometheusRule.rules.errorRate.enabled | bool | `true` | Enable high error rate alert |
| monitoring.prometheusRule.rules.errorRate.threshold | int | `5` | Error rate threshold (%) |
| monitoring.prometheusRule.rules.errorRate.for | string | `"5m"` | Duration before alerting |
| monitoring.prometheusRule.rules.errorRate.severity | string | `"warning"` | Alert severity |
| monitoring.prometheusRule.rules.slowProcessing.enabled | bool | `true` | Enable slow processing alert |
| monitoring.prometheusRule.rules.slowProcessing.threshold | int | `10` | Processing time threshold (seconds) |
| monitoring.prometheusRule.rules.slowProcessing.for | string | `"5m"` | Duration before alerting |
| monitoring.prometheusRule.rules.slowProcessing.severity | string | `"warning"` | Alert severity |
| monitoring.prometheusRule.rules.serviceDown.enabled | bool | `true` | Enable service down alert |
| monitoring.prometheusRule.rules.serviceDown.for | string | `"5m"` | Duration before alerting |
| monitoring.prometheusRule.rules.serviceDown.severity | string | `"critical"` | Alert severity |
| monitoring.prometheusRule.additionalRules | list | `[]` | Additional custom PrometheusRules |

## 必要な環境変数（Secret）

外部のSecretリソースに以下の環境変数を設定してください：

| 環境変数 | 説明 |
|----------|------|
| `MISSKEY_HOOK_SECRET` | Misskeyからのwebhookを認証するための秘密キー |
| `IFTTT_HOOK_SECRET` | IFTTTからのwebhookを認証するための秘密キー |
| `MISSKEY_HOST` | Misskeyインスタンスのホスト名（例: example.tld） |
| `MISSKEY_TOKEN` | MisskeyのAPIトークン |
| `API_KEY` | Twitter APIキー |
| `API_KEY_SECRET` | Twitter APIキーシークレット |
| `ACCESS_TOKEN` | Twitterアクセストークン |
| `ACCESS_TOKEN_SECRET` | Twitterアクセストークンシークレット |
| `IFTTT_EVENT` | IFTTTイベント名 |
| `IFTTT_KEY` | IFTTTキー |

## エンドポイント

### メインサーバー（デフォルト: ポート8080）

| エンドポイント | 説明 |
|---------------|------|
| `POST /` | Webhookリクエストを受け付け |
| `GET /healthz` | ヘルスチェック |

### メトリクスサーバー（デフォルト: ポート9090）

| エンドポイント | 説明 |
|---------------|------|
| `GET /metrics` | Prometheusメトリクス |

## メトリクス

以下のメトリクスが公開されます：

| メトリクス | 型 | 説明 |
|-----------|-----|------|
| `build_info` | Gauge | バージョン情報 |
| `webhook_requests_total` | Counter | リクエスト総数（source, status別） |
| `webhook_request_duration_seconds` | Histogram | リクエスト処理時間 |
| `webhook_request_errors_total` | Counter | エラー数（source, error_type別） |
| `note2tweet_total` | Counter | Note→Tweet変換試行数 |
| `note2tweet_success_total` | Counter | 成功数 |
| `note2tweet_errors_total` | Counter | エラー数 |
| `note2tweet_skipped_total` | Counter | スキップ数（reason別） |
| `tweet2note_total` | Counter | Tweet→Note変換試行数 |
| `tweet2note_success_total` | Counter | 成功数 |
| `tweet2note_errors_total` | Counter | エラー数 |
| `tweet2note_skipped_total` | Counter | スキップ数（reason別） |
| `tracker_entries_total` | Gauge | トラッカー内エントリ数 |
| `tracker_duplicates_hit_total` | Counter | 重複検出数 |

## 使用例

### 基本的なインストール

```yaml
# values.yaml
secrets:
  secretName: "my-note-tweet-connector-secret"

ingress:
  enabled: true
  className: "nginx"
  hosts:
    - host: ntc.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: ntc-tls
      hosts:
        - ntc.example.com
```

### モニタリング有効化

```yaml
# values.yaml
monitoring:
  serviceMonitor:
    enabled: true
    interval: "30s"
  prometheusRule:
    enabled: true
    rules:
      errorRate:
        enabled: true
        threshold: 5
      serviceDown:
        enabled: true
        severity: critical
```
