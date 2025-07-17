# Vulnerability Assessment Pipeline

![Pipeline Status](https://img.shields.io/badge/status-beta-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


A lightweight, local, CI‑style security automation pipeline for web applications that brings vulnerability scanning directly into your development workflow. Whenever a developer pushes code, the system automatically invokes an OWASP ZAP scan (running in Docker) against any target web application you configure. Findings are captured in timestamped HTML reports in the reports/ directory, enabling teams to identify and remediate high‑severity issues before code merges.

## 🚀 Features

* **Automated Scanning**: Triggers OWASP ZAP baseline scans on Git push events.
* **Manual Control**: Start/stop the pipeline daemon with simple commands.
* **Containerized Scanner**: Runs ZAP in Docker (`--network=host`) for isolation.
* **Clear Reporting**: Generates timestamped HTML reports in the `reports/` directory.
* **Lightweight & Local**: No cloud services or external CI/CD required.

## 🚀 Key Benefits

* **Shift‑Left Security**: Integrates security testing into the development lifecycle—just push code to trigger scans.
* **On‑Demand Control**: Start and stop the monitoring service as needed; no continuous resource usage.
* **Containerized Scanning**: Leverages OWASP ZAP in Docker for isolation and easy updates.
* **Extensible**: Swap or add scanners (e.g., Nikto, Nuclei) by adjusting scripts.
* **Clear Reporting**: Generates human‑readable, timestamped HTML reports in `reports/`.

## 🧰 Prerequisites

Before you begin, ensure you have:

* **Kali Linux** (or any Debian‑based Linux)
* **Docker** (with permissions to run containers)
* **Git**
* **Python 3**

Optional, for editing:

* A text editor (e.g., `nano`, `vim`, `code`)

## ⚙️ Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/vatsa709/vuln-pipeline.git
   cd vuln-pipeline
   ```

2. **Install Docker** (if not already):

   ```bash
   sudo apt update
   sudo apt install -y docker.io
   sudo systemctl enable --now docker
   ```

3. **Add your user to the Docker group** (to run without `sudo`):

   ```bash
   sudo usermod -aG docker $USER
   newgrp docker
   ```

4. **Ensure Python dependencies** (if you extend scripts):

   ```bash
   pip3 install GitPython weasyprint
   ```

## 🏁 Quick Start

1. **Launch the target app** (OWASP Juice Shop) via Docker:

   ```bash
   cd app
   docker-compose up -d
   ```

   Juice Shop will be available at `http://localhost:3000`.

2. **Start the pipeline service**:

   ```bash
   cd scripts
   ./pipeline.py start
   ```

3. **Trigger a scan** by pushing a commit to the app repo:

   ```bash
   cd ../app/juice-shop
   git add .
   git commit -m "Trigger ZAP scan"
   git push origin main
   ```

4. **View reports**:

   ```bash
   ls ../reports
   xdg-open ../reports/zap_report_<timestamp>.html
   ```

5. **Stop the pipeline** when done:

   ```bash
   ./pipeline.py stop
   ```

## 📂 Directory Structure

```
vuln-pipeline/
├── app/                  # OWASP Juice Shop source & docker-compose
├── config/               # Scanner and threshold configurations
├── scripts/              # Pipeline orchestration scripts
│   ├── pipeline.py       # Start/stop/status controller
│   ├── git_monitor.py    # Watches for Git pushes
│   └── scan_zap.sh       # Runs ZAP via Docker
├── reports/              # Generated HTML reports
└── logs/                 # Runtime logs
```

## ⚙️ Configuration

* **`config/thresholds.yaml`**: Defines severity levels (e.g., fail on `High` & `Critical`).
* **`scan_zap.sh`**: Adjust `TARGET` or Docker image tag as needed.

## 🛠 Troubleshooting

* **ZAP container can’t reach the app**: Ensure Juice Shop is running on `localhost:3000` and `--network=host` is set.
* **Permission denied on push**: Use a GitHub Personal Access Token (PAT) instead of a password.
* **`pipeline already running`**: Run `./pipeline.py stop` and delete stale `pipeline.pid` & `pipeline.enabled` files.

## 🤝 Contributing

1. Fork this repository.
2. Create your feature branch (`git checkout -b feature/MyFeature`).
3. Commit your changes (`git commit -m 'Add MyFeature'`).
4. Push to the branch (`git push origin feature/MyFeature`).
5. Open a Pull Request.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
