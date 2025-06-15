#!/usr/bin/env python3
import sys, json, yaml, os
from datetime import datetime
from weasyprint import HTML

# args: <scan_dir>
scan_dir = sys.argv[1]
zap_file = os.path.join(scan_dir, 'zap_results.json')

# Load thresholds
with open('config/thresholds.yaml') as f:
    thresholds = yaml.safe_load(f)['fail_on']

# Load ZAP JSON
with open(zap_file) as f:
    data = json.load(f)

issues = data.get('site', [])[0].get('alerts', [])
new_high = [i for i in issues if i['risk'] in thresholds]

# Build simple HTML
html = f"""
<h1>Vulnerability Report: {datetime.now().isoformat()}</h1>
<p>Total Alerts: {len(issues)}</p>
<p>High/Critical: {len(new_high)}</p>
<ul>
"""
for i in new_high:
    html += f"<li><strong>{i['alert']}</strong> (Risk: {i['risk']}) - {i['url']}</li>"
html += "</ul>"

# Write HTML & convert
report_html = os.path.join(scan_dir, 'report.html')
report_pdf  = os.path.join(scan_dir, 'report.pdf')
with open(report_html, 'w') as f:
    f.write(html)
HTML(report_html).write_pdf(report_pdf)

# Exit code: 1 if any high-risk found
sys.exit(1 if new_high else 0)
