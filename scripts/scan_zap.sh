#!/bin/bash

# Variables
TARGET="http://localhost:3000"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
REPORT_DIR="$HOME/vuln-pipeline/reports"
REPORT_NAME="zap_report_$TIMESTAMP.html"

# Ensure the report directory exists
mkdir -p "$REPORT_DIR"

# Run the scan
docker run --rm \
  --network="host" \
  -v "$REPORT_DIR:/zap/wrk" \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t "$TARGET" \
  -r "zap_report_$TIMESTAMP.html"
