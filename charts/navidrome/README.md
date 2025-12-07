# navidrome

![Version: 2.0.1](https://img.shields.io/badge/Version-2.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.59.0](https://img.shields.io/badge/AppVersion-0.59.0-informational?style=flat-square)

A Helm chart for Navidrome - A modern Music Server and Streamer

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| config.address | string | `""` |  |
| config.agents | string | `"lastfm,spotify,deezer"` |  |
| config.albumPlayCountMode | string | `"absolute"` |  |
| config.artistArtPriority | string | `"artist.*, album/artist.*, external"` |  |
| config.authRequestLimit | int | `5` |  |
| config.authWindowLength | string | `"20s"` |  |
| config.autoImportPlaylists | bool | `true` |  |
| config.autoTranscodeDownload | bool | `false` |  |
| config.backup.count | int | `0` |  |
| config.backup.path | string | `""` |  |
| config.backup.schedule | string | `""` |  |
| config.baseUrl | string | `""` |  |
| config.cacheFolder | string | `""` |  |
| config.coverArtPriority | string | `"cover.*, folder.*, front.*, embedded, external"` |  |
| config.coverJpegQuality | int | `75` |  |
| config.dataFolder | string | `"/data"` |  |
| config.deezer.enabled | bool | `true` |  |
| config.defaultDownloadableShare | bool | `false` |  |
| config.defaultDownsamplingFormat | string | `"opus"` |  |
| config.defaultLanguage | string | `"ja"` |  |
| config.defaultPlaylistPublicVisibility | bool | `false` |  |
| config.defaultShareExpiration | string | `"8760h"` |  |
| config.defaultTheme | string | `"Dark"` |  |
| config.defaultUIVolume | int | `100` |  |
| config.enableArtworkPrecache | bool | `true` |  |
| config.enableCoverAnimation | bool | `true` |  |
| config.enableDownloads | bool | `true` |  |
| config.enableExternalServices | bool | `true` |  |
| config.enableFavourites | bool | `true` |  |
| config.enableGravatar | bool | `false` |  |
| config.enableInsightsCollector | bool | `true` |  |
| config.enableLogRedacting | bool | `true` |  |
| config.enableMediaFileCoverArt | bool | `true` |  |
| config.enableNowPlaying | bool | `true` |  |
| config.enableReplayGain | bool | `true` |  |
| config.enableSharing | bool | `false` |  |
| config.enableStarRating | bool | `true` |  |
| config.enableTranscodingConfig | bool | `false` |  |
| config.enableUserEditing | bool | `true` |  |
| config.enabled | bool | `true` |  |
| config.ffmpegPath | string | `""` |  |
| config.gaTrackingID | string | `""` |  |
| config.httpSecurityHeaders.customFrameOptionsValue | string | `"DENY"` |  |
| config.ignoredArticles | string | `"The El La Los Las Le Les Os As O A"` |  |
| config.imageCacheSize | string | `"100MB"` |  |
| config.jukebox.adminOnly | bool | `true` |  |
| config.jukebox.default | string | `""` |  |
| config.jukebox.devices | list | `[]` |  |
| config.jukebox.enabled | bool | `false` |  |
| config.lastfm.apiKey | string | `""` |  |
| config.lastfm.enabled | bool | `true` |  |
| config.lastfm.language | string | `"en"` |  |
| config.lastfm.scrobbleFirstArtistOnly | bool | `false` |  |
| config.lastfm.secret | string | `""` |  |
| config.listenBrainz.baseURL | string | `"https://api.listenbrainz.org/1/"` |  |
| config.listenBrainz.enabled | bool | `true` |  |
| config.logFile | string | `""` |  |
| config.logLevel | string | `"info"` |  |
| config.lyricsPriority | string | `".lrc,.txt,embedded"` |  |
| config.maxSidebarPlaylists | int | `100` |  |
| config.mpvCmdTemplate | string | `"mpv --audio-device=%d --no-audio-display --pause %f --input-ipc-server=%s"` |  |
| config.mpvPath | string | `""` |  |
| config.musicFolder | string | `"/music"` |  |
| config.pid.album | string | `"musicbrainz_albumid|albumartistid,album,albumversion,releasedate"` |  |
| config.pid.track | string | `"musicbrainz_trackid|albumid,discnumber,tracknumber,title"` |  |
| config.playlistsPath | string | `""` |  |
| config.port | int | `4533` |  |
| config.preferSortTags | bool | `false` |  |
| config.prometheus.enabled | bool | `true` |  |
| config.prometheus.metricsPath | string | `"/metrics"` |  |
| config.prometheus.password | string | `""` |  |
| config.recentlyAddedByModTime | bool | `false` |  |
| config.scanner.artistJoiner | string | `" • "` |  |
| config.scanner.enabled | bool | `true` |  |
| config.scanner.followSymlinks | bool | `true` |  |
| config.scanner.purgeMissing | string | `"never"` |  |
| config.scanner.scanOnStartup | bool | `true` |  |
| config.scanner.schedule | string | `"0"` |  |
| config.scanner.watcherWait | string | `"5s"` |  |
| config.searchFullString | bool | `false` |  |
| config.sessionTimeout | string | `"48h"` |  |
| config.shareURL | string | `""` |  |
| config.smartPlaylistRefreshDelay | string | `"5s"` |  |
| config.spotify.id | string | `""` |  |
| config.spotify.secret | string | `""` |  |
| config.subsonic.appendSubtitle | bool | `true` |  |
| config.subsonic.artistParticipations | bool | `false` |  |
| config.subsonic.defaultReportRealPath | bool | `false` |  |
| config.subsonic.legacyClients | string | `"DSub"` |  |
| config.transcodingCacheSize | string | `"100MB"` |  |
| config.uiLoginBackgroundUrl | string | `""` |  |
| config.uiWelcomeMessage | string | `""` |  |
| config.unixSocketPerm | string | `"0660"` |  |
| containerPort | int | `4533` |  |
| env | list | `[]` |  |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"deluan/navidrome"` |  |
| image.tag | string | `"0.59.0"` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations | object | `{}` |  |
| ingress.className | string | `""` |  |
| ingress.enabled | bool | `true` |  |
| ingress.hosts[0].host | string | `"example.tld"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| ingress.tls | list | `[]` |  |
| livenessProbe | object | `{}` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| persistence.data.accessModes[0] | string | `"ReadWriteOnce"` |  |
| persistence.data.enabled | bool | `true` |  |
| persistence.data.existingClaim | string | `""` |  |
| persistence.data.size | string | `"10Gi"` |  |
| persistence.data.storageClass | string | `""` |  |
| persistence.music.accessModes[0] | string | `"ReadWriteOnce"` |  |
| persistence.music.createPv | bool | `false` |  |
| persistence.music.enabled | bool | `true` |  |
| persistence.music.existingClaim | string | `""` |  |
| persistence.music.existingVolume | string | `""` |  |
| persistence.music.nfs.mountOptions[0] | string | `"nfsvers=4.1"` |  |
| persistence.music.nfs.path | string | `""` |  |
| persistence.music.nfs.server | string | `""` |  |
| persistence.music.size | string | `"50Gi"` |  |
| persistence.music.storageClass | string | `""` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext | object | `{}` |  |
| readinessProbe | object | `{}` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| securityContext | object | `{}` |  |
| service.port | int | `4533` |  |
| service.targetPort | int | `4533` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.annotations | object | `{}` |  |
| serviceAccount.create | bool | `false` |  |
| serviceAccount.name | string | `""` |  |
| serviceMonitor.annotations | object | `{}` |  |
| serviceMonitor.enabled | bool | `false` |  |
| serviceMonitor.interval | string | `"30s"` |  |
| serviceMonitor.jobLabel | string | `""` |  |
| serviceMonitor.labels | object | `{}` |  |
| serviceMonitor.metricRelabelings | list | `[]` |  |
| serviceMonitor.namespace | string | `""` |  |
| serviceMonitor.relabelings | list | `[]` |  |
| serviceMonitor.scrapeTimeout | string | `"10s"` |  |
| serviceMonitor.selector | object | `{}` |  |
| tolerations | list | `[]` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)
