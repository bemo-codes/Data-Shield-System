# Data Shield System – Automated Backup & File Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/Automation-Backup-orange)
![Monitoring](https://img.shields.io/badge/File-Monitoring-green)
![Checksum](https://img.shields.io/badge/Security-MD5%20Checksum-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

An automated file backup and monitoring system built with Python to securely manage and synchronize important data directories using MD5 checksum comparison and periodic task scheduling.

## Features

- Developed automated file backup and directory synchronization
- Implemented checksum (MD5 hash) based file comparison to detect newly added or modified files efficiently
- Integrated scheduling automation for periodic backup execution
- Designed a command-line utility with real-time reporting and detailed log generation
- Preserves folder structures recursively during destination sync

## Demo

### Backup Execution

![Backup Execution](screenshots/backup.png)

### Synchronized Logs

![Backup Log](screenshots/log-report.png)

## Technologies Used

- Python
- OS Module
- hashlib
- shutil
- schedule
- Automation Scripting

## Project Structure

```text
Data-Shield-System/
│
├── DataShieldSystem.py
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
└── screenshots/
    ├── backup.png
    └── log-report.png