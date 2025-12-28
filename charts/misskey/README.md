# misskey

![Version: 0.1.1](https://img.shields.io/badge/Version-0.1.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2025.12.2](https://img.shields.io/badge/AppVersion-2025.12.2-informational?style=flat-square)

A Helm chart for Misskey - A decentralized social networking platform

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| externalPostgresql.database | string | `"misskey"` | External PostgreSQL database |
| externalPostgresql.existingSecret | string | `""` | Use existing secret for password (if set, misskey.existingConfigSecret is also required) |
| externalPostgresql.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| externalPostgresql.extra | object | `{}` | Extra connection options |
| externalPostgresql.host | string | `""` | External PostgreSQL host |
| externalPostgresql.password | string | `""` | External PostgreSQL password (required if existingSecret is not set) |
| externalPostgresql.port | int | `5432` | External PostgreSQL port |
| externalPostgresql.ssl | bool | `false` | Enable SSL |
| externalPostgresql.username | string | `"misskey"` | External PostgreSQL username |
| externalRedis.db | int | `0` | Redis database number |
| externalRedis.existingSecret | string | `""` | Use existing secret for password |
| externalRedis.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| externalRedis.family | int | `0` | IP family (0=Both, 4=IPv4, 6=IPv6) |
| externalRedis.host | string | `""` | External Redis host |
| externalRedis.password | string | `""` | External Redis password |
| externalRedis.port | int | `6379` | External Redis port |
| externalRedis.prefix | string | `""` | Key prefix |
| fullnameOverride | string | `""` | Override the full name of the chart |
| ingress.annotations | object | `{}` | Ingress annotations |
| ingress.className | string | `""` | Ingress class name |
| ingress.enabled | bool | `true` | Enable ingress |
| ingress.hosts | list | `[{"host":"misskey.example.com","paths":[{"path":"/","pathType":"Prefix"}]}]` | Ingress hosts |
| ingress.tls | list | `[]` | Ingress TLS configuration |
| misskey.allowedPrivateNetworks | list | `[]` | Allowed private networks for file upload |
| misskey.chmodSocket | string | `""` | Permission for socket file (e.g. '777') |
| misskey.clusterLimit | int | `1` | Number of worker processes (cluster limit) |
| misskey.deliverJobConcurrency | string | `""` | Deliver job concurrency per worker |
| misskey.deliverJobMaxAttempts | string | `""` | Max attempts for deliver jobs |
| misskey.deliverJobPerSec | string | `""` | Deliver jobs per second |
| misskey.disableHsts | bool | `false` | Whether to disable HSTS |
| misskey.existingConfigSecret | string | `""` | Use existing secret for the entire Misskey configuration (default.yml) If set, all other misskey.* settings are ignored and this secret is used |
| misskey.fulltextSearch | object | `{"provider":"sqlLike"}` | Fulltext search provider (sqlLike, sqlPgroonga, meilisearch) |
| misskey.id | string | `"aidx"` | ID generation method (aid, aidx, meid, ulid, objectid) ONCE YOU HAVE STARTED THE INSTANCE, DO NOT CHANGE THIS |
| misskey.inboxJobConcurrency | string | `""` | Inbox job concurrency per worker |
| misskey.inboxJobMaxAttempts | string | `""` | Max attempts for inbox jobs |
| misskey.inboxJobPerSec | string | `""` | Inbox jobs per second |
| misskey.logging.sql.disableQueryTruncation | bool | `false` | Disable query truncation in logs |
| misskey.logging.sql.enableQueryParamLogging | bool | `false` | Enable query parameter logging |
| misskey.maxFileSize | int | `262144000` | Maximum file size for uploads (bytes) |
| misskey.mediaProxy | string | `""` | Media proxy URL |
| misskey.meilisearch.apiKey | string | `""` |  |
| misskey.meilisearch.enabled | bool | `false` |  |
| misskey.meilisearch.host | string | `""` |  |
| misskey.meilisearch.index | string | `""` |  |
| misskey.meilisearch.port | int | `7700` |  |
| misskey.meilisearch.scope | string | `"local"` |  |
| misskey.meilisearch.ssl | bool | `false` |  |
| misskey.outgoingAddress | string | `""` | Local address used for outgoing requests |
| misskey.outgoingAddressFamily | string | `""` | IP address family for outgoing requests (ipv4, ipv6, dual) |
| misskey.pidFile | string | `""` | PID file path |
| misskey.port | int | `3000` | Port for Misskey to listen on |
| misskey.proxy | string | `""` | Proxy settings for outgoing HTTP/HTTPS requests |
| misskey.proxyBypassHosts | list | `["api.deepl.com","api-free.deepl.com","www.recaptcha.net","hcaptcha.com","challenges.cloudflare.com"]` | Hosts that should bypass the proxy |
| misskey.proxySmtp | string | `""` | Proxy for SMTP/SMTPS connections |
| misskey.publishTarballInsteadOfProvideRepositoryUrl | bool | `false` | Publish tarball instead of repository URL (for AGPL compliance) |
| misskey.relationshipJobConcurrency | string | `""` | Relationship job concurrency per worker |
| misskey.relationshipJobPerSec | string | `""` | Relationship jobs per second |
| misskey.sentry.backend | object | `{"dsn":"","enableNodeProfiling":false,"enabled":false}` | Enable Sentry for backend |
| misskey.sentry.frontend | object | `{"dsn":"","enabled":false}` | Enable Sentry for frontend |
| misskey.setupPassword | string | `""` | Setup password for initial admin account setup Be sure to change this when setting up Misskey via the Internet |
| misskey.socket | string | `""` | Use UNIX domain socket instead of port |
| misskey.trustProxy | bool | `true` | Trust proxy settings for reverse proxy Can be boolean or array of CIDR ranges |
| misskey.url | string | `"https://misskey.example.tld"` | The URL of your Misskey instance (REQUIRED) IMPORTANT: Once you have started the instance, DO NOT CHANGE THIS |
| misskey.videoThumbnailGenerator | string | `""` | Video thumbnail generator URL |
| nameOverride | string | `""` | Override the name of the chart |
| postgresql.database | string | `"misskey"` | PostgreSQL database name |
| postgresql.disableCache | bool | `false` | Disable query caching |
| postgresql.enabled | bool | `true` | Enable internal PostgreSQL |
| postgresql.existingSecret | string | `""` | Use existing secret for password |
| postgresql.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| postgresql.extra | object | `{}` | Extra connection options |
| postgresql.image.pullPolicy | string | `"IfNotPresent"` | Image pull policy |
| postgresql.image.repository | string | `"postgres"` | PostgreSQL image repository |
| postgresql.image.tag | string | `"18-alpine"` | PostgreSQL image tag |
| postgresql.password | string | `"you-should-change-this-password"` | PostgreSQL password (required if existingSecret is not set) |
| postgresql.persistence.accessModes | list | `["ReadWriteOnce"]` | Access modes |
| postgresql.persistence.enabled | bool | `true` | Enable persistence for PostgreSQL |
| postgresql.persistence.existingClaim | string | `""` | Existing claim to use |
| postgresql.persistence.size | string | `"10Gi"` | Size of the PVC |
| postgresql.persistence.storageClass | string | `""` | Storage class |
| postgresql.replication.enabled | bool | `false` | Enable database replication |
| postgresql.replication.slaves | list | `[]` | Slave database configurations Each slave can use existingSecret/existingSecretKey for password |
| postgresql.resources | object | `{}` | Resource limits and requests |
| postgresql.service.port | int | `5432` | PostgreSQL service port |
| postgresql.username | string | `"misskey"` | PostgreSQL username |
| redis.db | int | `0` | Redis database number |
| redis.enabled | bool | `true` | Enable internal Redis |
| redis.existingSecret | string | `""` | Use existing secret for password |
| redis.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| redis.family | int | `0` | IP family (0=Both, 4=IPv4, 6=IPv6) |
| redis.image.pullPolicy | string | `"IfNotPresent"` | Image pull policy |
| redis.image.repository | string | `"redis"` | Redis image repository |
| redis.image.tag | string | `"7-alpine"` | Redis image tag |
| redis.password | string | `""` | Redis password (leave empty for no password) |
| redis.persistence.accessModes | list | `["ReadWriteOnce"]` | Access modes |
| redis.persistence.enabled | bool | `true` | Enable persistence for Redis |
| redis.persistence.existingClaim | string | `""` | Existing claim to use |
| redis.persistence.size | string | `"2Gi"` | Size of the PVC |
| redis.persistence.storageClass | string | `""` | Storage class |
| redis.prefix | string | `""` | Key prefix |
| redis.resources | object | `{}` | Resource limits and requests |
| redis.service.port | int | `6379` | Redis service port |
| redisForJobQueue.db | int | `0` | Redis database number |
| redisForJobQueue.enabled | bool | `false` | Enable separate Redis for Job Queue |
| redisForJobQueue.existingSecret | string | `""` | Use existing secret for password |
| redisForJobQueue.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| redisForJobQueue.family | int | `0` | IP family (0=Both, 4=IPv4, 6=IPv6) |
| redisForJobQueue.host | string | `""` | Redis host |
| redisForJobQueue.password | string | `""` | Redis password |
| redisForJobQueue.port | int | `6379` | Redis port |
| redisForJobQueue.prefix | string | `""` | Key prefix |
| redisForPubsub.db | int | `0` | Redis database number |
| redisForPubsub.enabled | bool | `false` | Enable separate Redis for PubSub |
| redisForPubsub.existingSecret | string | `""` | Use existing secret for password |
| redisForPubsub.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| redisForPubsub.family | int | `0` | IP family (0=Both, 4=IPv4, 6=IPv6) |
| redisForPubsub.host | string | `""` | Redis host |
| redisForPubsub.password | string | `""` | Redis password |
| redisForPubsub.port | int | `6379` | Redis port |
| redisForPubsub.prefix | string | `""` | Key prefix |
| redisForReactions.db | int | `0` | Redis database number |
| redisForReactions.enabled | bool | `false` | Enable separate Redis for Reactions |
| redisForReactions.existingSecret | string | `""` | Use existing secret for password |
| redisForReactions.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| redisForReactions.family | int | `0` | IP family (0=Both, 4=IPv4, 6=IPv6) |
| redisForReactions.host | string | `""` | Redis host |
| redisForReactions.password | string | `""` | Redis password |
| redisForReactions.port | int | `6379` | Redis port |
| redisForReactions.prefix | string | `""` | Key prefix |
| redisForTimelines.db | int | `0` | Redis database number |
| redisForTimelines.enabled | bool | `false` | Enable separate Redis for Timelines |
| redisForTimelines.existingSecret | string | `""` | Use existing secret for password |
| redisForTimelines.existingSecretKey | string | `"password"` | Key in existing secret containing the password |
| redisForTimelines.family | int | `0` | IP family (0=Both, 4=IPv4, 6=IPv6) |
| redisForTimelines.host | string | `""` | Redis host |
| redisForTimelines.password | string | `""` | Redis password |
| redisForTimelines.port | int | `6379` | Redis port |
| redisForTimelines.prefix | string | `""` | Key prefix |
| serviceAccount.annotations | object | `{}` | Annotations for service account |
| serviceAccount.create | bool | `true` | Create service account |
| serviceAccount.name | string | `""` | Service account name |
| web.affinity | object | `{}` | Affinity rules |
| web.extraEnv | list | `[]` | Additional environment variables |
| web.extraEnvFrom | list | `[]` | Additional environment variables from secrets/configmaps |
| web.image.pullPolicy | string | `"IfNotPresent"` | Image pull policy |
| web.image.repository | string | `"misskey/misskey"` | Image repository |
| web.image.tag | string | `""` | Image tag (defaults to Chart.appVersion) |
| web.imagePullSecrets | list | `[]` | Image pull secrets |
| web.livenessProbe | object | `{"httpGet":{"path":"/healthz","port":"http"},"initialDelaySeconds":60,"periodSeconds":30,"timeoutSeconds":10}` | Liveness probe configuration |
| web.nodeSelector | object | `{}` | Node selector |
| web.persistence.accessModes | list | `["ReadWriteOnce"]` | Access modes |
| web.persistence.annotations | object | `{}` | Annotations for the PVC |
| web.persistence.enabled | bool | `true` | Enable persistence for files |
| web.persistence.existingClaim | string | `""` | Existing claim to use |
| web.persistence.size | string | `"10Gi"` | Size of the PVC |
| web.persistence.storageClass | string | `""` | Storage class |
| web.podAnnotations | object | `{}` | Pod annotations |
| web.podLabels | object | `{}` | Pod labels |
| web.podSecurityContext | object | `{"fsGroup":991}` | Security context for the pod |
| web.readinessProbe | object | `{"httpGet":{"path":"/healthz","port":"http"},"initialDelaySeconds":30,"periodSeconds":10,"timeoutSeconds":5}` | Readiness probe configuration |
| web.replicaCount | int | `1` | Number of replicas |
| web.resources | object | `{}` | Resource limits and requests |
| web.securityContext | object | `{"runAsGroup":991,"runAsNonRoot":true,"runAsUser":991}` | Security context for the container |
| web.service.port | int | `3000` | Service port |
| web.service.type | string | `"ClusterIP"` | Service type |
| web.tolerations | list | `[]` | Tolerations |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
