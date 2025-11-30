# spotify-nowplaying

![Version: 2.0.1](https://img.shields.io/badge/Version-2.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.1.0](https://img.shields.io/badge/AppVersion-3.1.0-informational?style=flat-square)

A Helm chart for the Spotify Now Playing application

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| containerPort | int | `8080` |  |
| env[0].name | string | `"PORT"` |  |
| env[0].value | string | `"8080"` |  |
| env[1].name | string | `"METRICS_PORT"` |  |
| env[1].value | string | `"9090"` |  |
| env[2].name | string | `"SERVER_URI"` |  |
| env[2].value | string | `"example.tld"` |  |
| env[3].name | string | `"SPOTIFY_REDIRECT_URI_NOTE"` |  |
| env[3].value | string | `"https://example.tld/note/callback"` |  |
| env[4].name | string | `"SPOTIFY_REDIRECT_URI_TWEET"` |  |
| env[4].value | string | `"https://example.tld/tweet/callback"` |  |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"ghcr.io/soli0222/spotify-nowplaying"` |  |
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
| livenessProbe.httpGet.path | string | `"/status"` |  |
| livenessProbe.httpGet.port | string | `"http"` |  |
| livenessProbe.initialDelaySeconds | int | `10` |  |
| livenessProbe.periodSeconds | int | `10` |  |
| livenessProbe.timeoutSeconds | int | `5` |  |
| metricsPort | int | `9090` |  |
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
| monitoring.prometheusRule.rules.slowApiResponse.enabled | bool | `true` |  |
| monitoring.prometheusRule.rules.slowApiResponse.for | string | `"5m"` |  |
| monitoring.prometheusRule.rules.slowApiResponse.severity | string | `"warning"` |  |
| monitoring.prometheusRule.rules.slowApiResponse.threshold | int | `10` |  |
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
| readinessProbe.httpGet.path | string | `"/status"` |  |
| readinessProbe.httpGet.port | string | `"http"` |  |
| readinessProbe.initialDelaySeconds | int | `5` |  |
| readinessProbe.periodSeconds | int | `5` |  |
| readinessProbe.timeoutSeconds | int | `3` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| secrets.env[0].key | string | `"SPOTIFY_CLIENT_ID"` |  |
| secrets.env[0].name | string | `"SPOTIFY_CLIENT_ID"` |  |
| secrets.env[1].key | string | `"SPOTIFY_CLIENT_SECRET"` |  |
| secrets.env[1].name | string | `"SPOTIFY_CLIENT_SECRET"` |  |
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
