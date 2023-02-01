{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "ingress-nginx.name" -}}
{{- .Chart.Name | trimSuffix "-app" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
TODO remove this legacy helper once switched to "ingress-nginx.name" everywhere.
*/}}
{{- define "name" -}}
{{- include "ingress-nginx.name" . -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "ingress-nginx.labels" -}}
app: {{ include "name" . | quote }}
{{ include "ingress-nginx.selectorLabels" . }}
app.kubernetes.io/managed-by: {{ .Release.Service | quote }}
app.kubernetes.io/name: {{ include "name" . | quote }}
app.kubernetes.io/instance: {{ .Release.Name | quote }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/part-of: {{ template "name" . }}
giantswarm.io/service-type: "managed"
application.giantswarm.io/team: {{ index .Chart.Annotations "application.giantswarm.io/team" | quote }}
helm.sh/chart: {{ include "chart" . | quote }}
{{- end -}}

{{/*
Selector labels
*/}}
{{- define "ingress-nginx.selectorLabels" -}}
k8s-app: {{ .Release.Name | quote }}
{{- end -}}

{{/*
Create the name of the controller service account to use
*/}}
{{- define "ingress-nginx.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
    {{ default (include "ingress-nginx.fullname" .) .Values.serviceAccount.name }}
{{- else -}}
    {{ default "default" .Values.serviceAccount.name }}
{{- end -}}
{{- end -}}

{{/*
Return the appropriate apiGroup for PodSecurityPolicy.
*/}}
{{- define "podSecurityPolicy.apiGroup" -}}
{{- if semverCompare ">=1.14-0" .Capabilities.KubeVersion.GitVersion -}}
{{- print "policy" -}}
{{- else -}}
{{- print "extensions" -}}
{{- end -}}
{{- end -}}

{{/*
Create a name stem for resource names
When pods for deployments are created they have an additional 16 character
suffix appended, e.g. "-957c9d6ff-pkzgw". Given that Kubernetes allows 63
characters for resource names, the stem is truncated to 47 characters to leave
room for such suffix.
*/}}
{{- define "ingress-nginx.fullname" -}}
{{- .Release.Name | replace "." "-" | trunc 47 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified controller name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "ingress-nginx.controller.fullname" -}}
{{ include "ingress-nginx.fullname" . }}
{{- end -}}

{{/*
Construct a unique electionID.
Users can provide an override for an explicit electionID if they want via `.Values.controller.electionID`
*/}}
{{- define "ingress-nginx.controller.electionID" -}}
{{- $defElectionID := printf "%s-leader" (include "ingress-nginx.fullname" .) -}}
{{- $electionID := default $defElectionID .Values.controller.electionID -}}
{{- print $electionID -}}
{{- end -}}

{{/*
LB Service name.
*/}}
{{- define "resource.controller-service.name" -}}
{{ include "ingress-nginx.fullname" . }}{{ .Values.controller.service.suffix }}
{{- end -}}

{{/*
Internal LB Service name.
*/}}
{{- define "resource.controller-service-internal.name" -}}
{{ include "ingress-nginx.fullname" . }}-internal{{ .Values.controller.service.internal.suffix }}
{{- end -}}

{{/*
IngressClass parameters.
*/}}
{{- define "ingressClass.parameters" -}}
  {{- if .Values.controller.ingressClassResource.parameters -}}
          parameters:
{{ toYaml .Values.controller.ingressClassResource.parameters | indent 4}}
  {{ end }}
{{- end -}}

{{/*
Create a default fully qualified default backend name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "ingress-nginx.defaultBackend.fullname" -}}
{{- printf "%s-%s" (include "ingress-nginx.fullname" .) .Values.defaultBackend.name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create the name of the backend service account to use - only used when podsecuritypolicy is also enabled
*/}}
{{- define "ingress-nginx.defaultBackend.serviceAccountName" -}}
{{- if .Values.defaultBackend.serviceAccount.create -}}
    {{ default (printf "%s-backend" (include "ingress-nginx.fullname" .)) .Values.defaultBackend.serviceAccount.name }}
{{- else -}}
    {{ default "default-backend" .Values.defaultBackend.serviceAccount.name }}
{{- end -}}
{{- end -}}
