FROM golang:1.21 AS build-tests

WORKDIR /app

RUN go install github.com/onsi/ginkgo/v2/ginkgo@latest

ADD go.mod go.sum ./
RUN go mod tidy

ADD . .
RUN ginkgo build --skip-package /X -r ./


FROM debian:bookworm-slim

WORKDIR /app

RUN apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y ca-certificates \
  && rm -rf /var/lib/apt/lists/*

COPY --from=build-tests /app /app
COPY --from=build-tests /go/bin/ginkgo /usr/local/bin/ginkgo

COPY <<EOF /app/entrypoint.sh
#!/usr/bin/env bash
SUITES_TO_RUN=$(find \$1 -name '*.test' | xargs)
shift
REPORT_DIR=\${REPORT_DIR:-/tmp/reports}
mkdir -p \${REPORT_DIR}
ginkgo --output-dir=\${REPORT_DIR} --junit-report=test-results.xml --timeout 4h --keep-going -v -r $@ \${SUITES_TO_RUN}
EOF

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
