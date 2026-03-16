# Helm Chart 実装仕様書

このリポジトリに含まれる Helm Chart の設計方針・実装パターンをまとめた仕様書です。
新規チャートの作成や既存チャートの修正時には、この仕様に従って実装してください。

---

## 目次

1. [リポジトリ構成](#リポジトリ構成)
2. [Chart.yaml](#chartyaml)
3. [ディレクトリ・ファイル構成](#ディレクトリファイル構成)
4. [\_helpers.tpl](#_helperstpl)
5. [values.yaml](#valuesyaml)
6. [テンプレートファイル](#テンプレートファイル)
7. [シークレット管理](#シークレット管理)
8. [依存コンポーネントの内包](#依存コンポーネントの内包)
9. [監視・アラート](#監視アラート)
10. [CronJob チャート](#cronjob-チャート)
11. [命名規則](#命名規則)
12. [CI/CD・自動化](#cicd自動化)

---

## リポジトリ構成

```
helm-charts/
├── charts/                        # 各 Helm Chart のルート
│   └── <chart-name>/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── _helpers.tpl
│           ├── deployment.yaml    # または cronjob.yaml
│           ├── service.yaml
│           ├── ingress.yaml
│           ├── serviceaccount.yaml
│           └── ...
├── scripts/
│   ├── bump_chart_version.py      # SemVer バンプスクリプト
│   └── update_readme.py           # README テーブル更新スクリプト
├── .github/workflows/
│   ├── release.yaml               # チャート公開パイプライン
│   └── auto-bump-chart-version.yaml
├── renovate.json5
└── README.md
```

Helm リポジトリは GitHub Pages (`https://soli0222.github.io/helm-charts`) で公開しています。

---

## Chart.yaml

### 必須フィールド

```yaml
apiVersion: v2
name: <chart-name>
description: <One-line description in English>
type: application
version: "0.1.0"        # チャート自体のバージョン (SemVer)
# renovate: image=<registry>/<image>
appVersion: "<image-tag>"  # デプロイするアプリのバージョン
```

### ルール

- `apiVersion` は常に `v2`
- `type` は常に `application`
- `version` は SemVer に従う
- `appVersion` はクォートで囲む
- `appVersion` の直前行に Renovate アノテーションを記述し、コンテナイメージの自動追跡を有効にする

```yaml
# renovate: image=ghcr.io/soli0222/my-app
appVersion: "1.2.3"
```

サードパーティイメージを追跡する場合も同じパターンを使う:

```yaml
# renovate: image=docker.io/library/nginx
appVersion: "1.27.0"
```

---

## ディレクトリ・ファイル構成

### Web サービス系（標準構成）

```
templates/
├── _helpers.tpl
├── deployment.yaml
├── service.yaml
├── ingress.yaml
├── serviceaccount.yaml
├── secret.yaml            # シークレットを自前で作成する場合
├── configmap.yaml         # 設定ファイルを ConfigMap にまとめる場合
├── pvc.yaml               # 永続ボリュームが必要な場合
├── servicemonitor.yaml    # Prometheus 連携を提供する場合
└── prometheusrule.yaml    # アラートルールを提供する場合
```

### CronJob 系

```
templates/
├── _helpers.tpl
├── cronjob.yaml
└── secret.yaml
```

### マルチコンポーネント系

複数のサービスを 1 チャートで扱う場合は、コンポーネント名をプレフィックスに付けてファイルを分割する:

```
templates/
├── _helpers.tpl
├── <component-a>-deployment.yaml
├── <component-a>-service.yaml
├── <component-a>-pvc.yaml
├── <component-b>-deployment.yaml
├── <component-b>-service.yaml
└── ...
```

---

## \_helpers.tpl

すべてのチャート（`_helpers.tpl` を持つもの）は以下 **6 つの名前付きテンプレート** を定義する。
プレフィックスはチャート名 (`<chart-name>.`) とする。

```gotmpl
{{/*
Expand the name of the chart.
*/}}
{{- define "<chart-name>.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "<chart-name>.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "<chart-name>.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "<chart-name>.labels" -}}
helm.sh/chart: {{ include "<chart-name>.chart" . }}
{{ include "<chart-name>.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "<chart-name>.selectorLabels" -}}
app.kubernetes.io/name: {{ include "<chart-name>.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "<chart-name>.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "<chart-name>.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}
```

### 拡張ヘルパー

複雑なチャートでは、以下のような追加ヘルパーを定義することがある:

- **ホスト/ポート解決**: 内包コンポーネントと外部サービスを切り替えるロジック
  ```gotmpl
  {{- define "<chart-name>.postgres.host" -}}
  {{- if .Values.postgresql.enabled }}
  {{- include "<chart-name>.fullname" . }}-postgresql
  {{- else }}
  {{- .Values.externalPostgres.host }}
  {{- end }}
  {{- end }}
  ```
- **PVC 名解決**: `existingClaim` の有無で名前を切り替える
- **シークレット名解決**: 外部シークレットか自前作成かを切り替える

---

## values.yaml

### 標準フィールド（全チャート共通）

以下の順序で定義する:

```yaml
nameOverride: ""
fullnameOverride: ""

image:
  repository: <registry/image>
  tag: ""            # 空のとき .Chart.AppVersion を使用する
  pullPolicy: IfNotPresent

imagePullSecrets: []

serviceAccount:
  create: true
  annotations: {}
  name: ""

podAnnotations: {}
podLabels: {}
podSecurityContext: {}
securityContext: {}

replicaCount: 1

service:
  type: ClusterIP
  port: <app-port>

ingress:
  enabled: false
  className: ""
  annotations: {}
  hosts:
    - host: example.tld
      paths:
        - path: /
          pathType: ImplementationSpecific
  tls: []

resources: {}
nodeSelector: {}
tolerations: []
affinity: {}

livenessProbe:
  httpGet:
    path: /
    port: http
readinessProbe:
  httpGet:
    path: /
    port: http
```

### アプリ固有設定

アプリケーション固有の設定は `config:` キー配下にまとめる:

```yaml
config:
  someKey: someValue
  anotherKey: ""
```

### 永続ボリューム

```yaml
persistence:
  enabled: false
  existingClaim: ""
  storageClass: ""
  size: 1Gi
  accessModes:
    - ReadWriteOnce
```

### 外部サービス

内包コンポーネント（PostgreSQL, Redis, Valkey 等）に対応する外部サービスの切り替え:

```yaml
postgresql:
  enabled: true          # true のとき内包コンポーネントを使用する

externalPostgres:
  host: ""
  port: 5432
  database: ""
  user: ""
  existingSecret: ""
  existingSecretKey: ""
```

### 監視

```yaml
serviceMonitor:
  enabled: false
  namespace: ""
  labels: {}
  annotations: {}
  interval: 30s
  scrapeTimeout: 10s
  relabelings: []
  metricRelabelings: []

prometheusRule:
  enabled: false
  namespace: ""
  labels: {}
  annotations: {}
  rules: []
```

---

## テンプレートファイル

### deployment.yaml

標準的な `Deployment` テンプレートの骨格:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "<chart-name>.fullname" . }}
  labels:
    {{- include "<chart-name>.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "<chart-name>.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      annotations:
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
        # ConfigMap を使う場合はチェックサムアノテーションを追加する
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
      labels:
        {{- include "<chart-name>.selectorLabels" . | nindent 8 }}
        {{- with .Values.podLabels }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ include "<chart-name>.serviceAccountName" . }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      containers:
        - name: {{ .Chart.Name }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: <app-port>
              protocol: TCP
          {{- with .Values.livenessProbe }}
          livenessProbe:
            {{- toYaml . | nindent 12 }}
          {{- end }}
          {{- with .Values.readinessProbe }}
          readinessProbe:
            {{- toYaml . | nindent 12 }}
          {{- end }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
```

### ingress.yaml

```yaml
{{- if .Values.ingress.enabled -}}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ include "<chart-name>.fullname" . }}
  labels:
    {{- include "<chart-name>.labels" . | nindent 4 }}
  {{- with .Values.ingress.annotations }}
  annotations:
    {{- toYaml . | nindent 4 }}
  {{- end }}
spec:
  {{- if .Values.ingress.className }}
  ingressClassName: {{ .Values.ingress.className }}
  {{- end }}
  {{- if .Values.ingress.tls }}
  tls:
    {{- toYaml .Values.ingress.tls | nindent 4 }}
  {{- end }}
  rules:
    {{- range .Values.ingress.hosts }}
    - host: {{ .host | quote }}
      http:
        paths:
          {{- range .paths }}
          - path: {{ .path }}
            pathType: {{ .pathType }}
            backend:
              service:
                name: {{ include "<chart-name>.fullname" $ }}
                port:
                  number: {{ $.Values.service.port }}
          {{- end }}
    {{- end }}
{{- end }}
```

### pvc.yaml

```yaml
{{- if and .Values.persistence.enabled (not .Values.persistence.existingClaim) }}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ include "<chart-name>.fullname" . }}
  labels:
    {{- include "<chart-name>.labels" . | nindent 4 }}
spec:
  accessModes:
    {{- toYaml .Values.persistence.accessModes | nindent 4 }}
  {{- if .Values.persistence.storageClass }}
  storageClassName: {{ .Values.persistence.storageClass }}
  {{- end }}
  resources:
    requests:
      storage: {{ .Values.persistence.size }}
{{- end }}
```

---

## シークレット管理

チャートではシークレットを作成せず、事前に作成済みの Secret を参照する (`existingSecret`) パターンを採用する。

```yaml
# values.yaml
config:
  existingSecret: ""        # Secret 名
  existingSecretKey: ""     # Secret 内のキー名
```

```yaml
# deployment.yaml (env)
env:
  - name: MY_SECRET
    valueFrom:
      secretKeyRef:
        name: {{ .Values.config.existingSecret }}
        key: {{ .Values.config.existingSecretKey }}

---

## 依存コンポーネントの内包

Helm サブチャートを使わず、依存サービス（PostgreSQL, Redis, Valkey 等）を
テンプレートとして内包する場合のパターン:

1. **値の構造**: コンポーネントごとにトップレベルキーを用意し、`enabled` フラグで内包/外部を切り替える
2. **ファイル分割**: `<component>-deployment.yaml`, `<component>-service.yaml`, `<component>-pvc.yaml`
3. **ガード**: 各ファイルを `{{- if .Values.<component>.enabled }}` で囲む
4. **ラベル**: `app.kubernetes.io/component: <component>` を追加
5. **名前**: `{{ include "<chart-name>.fullname" . }}-<component>`

```yaml
# values.yaml
valkey:
  enabled: true
  image:
    repository: valkey/valkey
    tag: "8"
  persistence:
    enabled: true
    size: 1Gi
```

```yaml
# valkey-deployment.yaml
{{- if .Values.valkey.enabled }}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "<chart-name>.fullname" . }}-valkey
  labels:
    {{- include "<chart-name>.labels" . | nindent 4 }}
    app.kubernetes.io/component: valkey
...
{{- end }}
```

---

## 監視・アラート

### ServiceMonitor

`monitoring.coreos.com/v1` を使用:

```yaml
{{- if .Values.serviceMonitor.enabled }}
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: {{ include "<chart-name>.fullname" . }}
  {{- if .Values.serviceMonitor.namespace }}
  namespace: {{ .Values.serviceMonitor.namespace }}
  {{- end }}
  labels:
    {{- include "<chart-name>.labels" . | nindent 4 }}
    {{- with .Values.serviceMonitor.labels }}
    {{- toYaml . | nindent 4 }}
    {{- end }}
spec:
  selector:
    matchLabels:
      {{- include "<chart-name>.selectorLabels" . | nindent 6 }}
  endpoints:
    - port: http
      {{- with .Values.serviceMonitor.interval }}
      interval: {{ . }}
      {{- end }}
      {{- with .Values.serviceMonitor.scrapeTimeout }}
      scrapeTimeout: {{ . }}
      {{- end }}
      {{- with .Values.serviceMonitor.relabelings }}
      relabelings:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.serviceMonitor.metricRelabelings }}
      metricRelabelings:
        {{- toYaml . | nindent 8 }}
      {{- end }}
{{- end }}
```

### PrometheusRule

アラートルールは `for:`, `severity:`, `summary:`, `description:` を統一して設定する:

```yaml
{{- if .Values.prometheusRule.enabled }}
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: {{ include "<chart-name>.fullname" . }}
spec:
  groups:
    - name: {{ include "<chart-name>.fullname" . }}
      rules:
        - alert: <AlertName>
          expr: <PromQL>
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "<summary>"
            description: "<description>"
{{- end }}
```

---

## CronJob チャート

### 基本骨格

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: {{ include "<chart-name>.fullname" . }}
  labels:
    {{- include "<chart-name>.labels" . | nindent 4 }}
spec:
  schedule: {{ .Values.schedule | quote }}
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      template:
        metadata:
          labels:
            {{- include "<chart-name>.selectorLabels" . | nindent 12 }}
        spec:
          restartPolicy: OnFailure
          containers:
            - name: {{ .Chart.Name }}
              image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
              imagePullPolicy: {{ .Values.image.pullPolicy }}
```

### Helm フック（DB マイグレーション等）

インストール/アップグレード後に一度だけ実行する Job:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ include "<chart-name>.fullname" . }}-migrate
  annotations:
    "helm.sh/hook": post-install,post-upgrade
    "helm.sh/hook-delete-policy": hook-succeeded
```

---

## 命名規則

| リソース | 命名パターン |
|---|---|
| 基本リソース | `{{ include "<chart>.fullname" . }}` |
| コンポーネントリソース | `{{ include "<chart>.fullname" . }}-<component>` |
| PVC (単一) | `{{ include "<chart>.fullname" . }}` |
| PVC (複数) | `{{ include "<chart>.fullname" . }}-<purpose>` |
| Secret | `{{ include "<chart>.fullname" . }}-secret` |
| ConfigMap | `{{ include "<chart>.fullname" . }}` |
| Helm フック Job | `{{ include "<chart>.fullname" . }}-<action>` |

- リソース名はすべて 63 文字以内 (`trunc 63 | trimSuffix "-"`)
- `nameOverride` / `fullnameOverride` を介してオーバーライド可能にする

---

## CI/CD・自動化

### チャートリリース

- `main` ブランチの `charts/**` への push をトリガーに `helm/chart-releaser-action` で GitHub Pages へ公開
- 公開前に `scripts/update_readme.py` でルート `README.md` のチャート一覧テーブルを自動更新

### バージョン管理

チャートの `version` は PR 単位でバンプする:

- PR に `/bump` (パッチ), `/bump-minor`, `/bump-major` とコメントすることでバンプ
- `scripts/bump_chart_version.py` が SemVer を自動更新
- バンプ後に `helm-docs` でチャートごとの `README.md` を再生成

### Renovate

`renovate.json5` で以下を自動管理:

- `values.yaml` の `repository:` / `tag:` パターンを検出してイメージタグを追跡
- `Chart.yaml` の `# renovate: image=<registry>/<image>` アノテーションで `appVersion` を追跡
- GitHub Actions は自動マージ; Docker イメージ更新は手動レビューが必要
