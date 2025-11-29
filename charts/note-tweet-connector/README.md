# note-tweet-connector

![Version: 1.0.3](https://img.shields.io/badge/Version-1.0.3-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.0.2](https://img.shields.io/badge/AppVersion-2.0.2-informational?style=flat-square)

A Helm chart for the Note Tweet Connector

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| args.idleTimeout | string | `"60s"` |  |
| args.logLevel | string | `"info"` |  |
| args.metricsPort | int | `9090` |  |
| args.port | int | `8080` |  |
| args.readTimeout | string | `"15s"` |  |
| args.shutdownTimeout | string | `"30s"` |  |
| args.trackerExpiry | string | `"5h"` |  |
| args.writeTimeout | string | `"15s"` |  |
| env | list | `[]` |  |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"ghcr.io/soli0222/note-tweet-connector"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations | object | `{}` |  |
| ingress.className | string | `""` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"example.tld"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| ingress.tls | list | `[]` |  |
| livenessProbe.failureThreshold | int | `3` |  |
| livenessProbe.httpGet.path | string | `"/healthz"` |  |
| livenessProbe.httpGet.port | string | `"http"` |  |
| livenessProbe.initialDelaySeconds | int | `10` |  |
| livenessProbe.periodSeconds | int | `10` |  |
| livenessProbe.timeoutSeconds | int | `5` |  |
| metricsService.enabled | bool | `true` |  |
| metricsService.port | int | `9090` |  |
| metricsService.type | string | `"ClusterIP"` |  |
| monitoring.prometheusRule.additionalRules | list | `[]` |  |
| monitoring.prometheusRule.annotations | object | `{}` |  |
| monitoring.prometheusRule.enabled | bool | `false` |  |
| monitoring.prometheusRule.labels | object | `{}` |  |
| monitoring.prometheusRule.namespace | string | `""` |  |
| monitoring.prometheusRule.rules.errorRate.enabled | bool | `true` |  |
| monitoring.prometheusRule.rules.errorRate.for | string | `"5m"` |  |
| monitoring.prometheusRule.rules.errorRate.severity | string | `"warning"` |  |
| monitoring.prometheusRule.rules.errorRate.threshold | int | `5` |  |
| monitoring.prometheusRule.rules.serviceDown.enabled | bool | `true` |  |
| monitoring.prometheusRule.rules.serviceDown.for | string | `"5m"` |  |
| monitoring.prometheusRule.rules.serviceDown.severity | string | `"critical"` |  |
| monitoring.prometheusRule.rules.slowProcessing.enabled | bool | `true` |  |
| monitoring.prometheusRule.rules.slowProcessing.for | string | `"5m"` |  |
| monitoring.prometheusRule.rules.slowProcessing.severity | string | `"warning"` |  |
| monitoring.prometheusRule.rules.slowProcessing.threshold | int | `10` |  |
| monitoring.serviceMonitor.annotations | object | `{}` |  |
| monitoring.serviceMonitor.enabled | bool | `false` |  |
| monitoring.serviceMonitor.interval | string | `"30s"` |  |
| monitoring.serviceMonitor.jobLabel | string | `""` |  |
| monitoring.serviceMonitor.labels | object | `{}` |  |
| monitoring.serviceMonitor.metricRelabelings | list | `[]` |  |
| monitoring.serviceMonitor.namespace | string | `""` |  |
| monitoring.serviceMonitor.path | string | `"/metrics"` |  |
| monitoring.serviceMonitor.relabelings | list | `[]` |  |
| monitoring.serviceMonitor.scrapeTimeout | string | `"10s"` |  |
| monitoring.serviceMonitor.selector | object | `{}` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext | object | `{}` |  |
| readinessProbe.failureThreshold | int | `3` |  |
| readinessProbe.httpGet.path | string | `"/healthz"` |  |
| readinessProbe.httpGet.port | string | `"http"` |  |
| readinessProbe.initialDelaySeconds | int | `5` |  |
| readinessProbe.periodSeconds | int | `5` |  |
| readinessProbe.timeoutSeconds | int | `3` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| secrets.env[0].key | string | `"MISSKEY_HOOK_SECRET"` |  |
| secrets.env[0].name | string | `"MISSKEY_HOOK_SECRET"` |  |
| secrets.env[10].key | string | `"IFTTT_KEY"` |  |
| secrets.env[10].name | string | `"IFTTT_KEY"` |  |
| secrets.env[1].key | string | `"IFTTT_HOOK_SECRET"` |  |
| secrets.env[1].name | string | `"IFTTT_HOOK_SECRET"` |  |
| secrets.env[2].key | string | `"MISSKEY_HOST"` |  |
| secrets.env[2].name | string | `"MISSKEY_HOST"` |  |
| secrets.env[3].key | string | `"MISSKEY_TOKEN"` |  |
| secrets.env[3].name | string | `"MISSKEY_TOKEN"` |  |
| secrets.env[4].key | string | `"MISSKEY_MEDIA_HOST"` |  |
| secrets.env[4].name | string | `"MISSKEY_MEDIA_HOST"` |  |
| secrets.env[5].key | string | `"API_KEY"` |  |
| secrets.env[5].name | string | `"API_KEY"` |  |
| secrets.env[6].key | string | `"API_KEY_SECRET"` |  |
| secrets.env[6].name | string | `"API_KEY_SECRET"` |  |
| secrets.env[7].key | string | `"ACCESS_TOKEN"` |  |
| secrets.env[7].name | string | `"ACCESS_TOKEN"` |  |
| secrets.env[8].key | string | `"ACCESS_TOKEN_SECRET"` |  |
| secrets.env[8].name | string | `"ACCESS_TOKEN_SECRET"` |  |
| secrets.env[9].key | string | `"IFTTT_EVENT"` |  |
| secrets.env[9].name | string | `"IFTTT_EVENT"` |  |
| secrets.secretName | string | `""` |  |
| securityContext | object | `{}` |  |
| service.port | int | `8080` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.annotations | object | `{}` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `""` |  |
| tolerations | list | `[]` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
