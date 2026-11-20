# 1-Click WireGuard & Tailscale Secure Remote Access Stack

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Get%20Kit%20($4.99)-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/dimiboy/shop)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

Turnkey dual-VPN remote access stack combining **WireGuard-Easy** (ultra-fast self-hosted VPN with web UI & QR codes) and **Tailscale** (mesh VPN with zero port forwarding subnet routing) plus an automated WAN & health alert watchdog.

> **🛒 Available on [Ko-fi Shop](https://ko-fi.com/dimiboy/shop)** (or Pay-What-You-Want).

---

## 📦 What's Inside

- **`docker-compose.yml`**: Pre-configured WireGuard-Easy Web UI + Tailscale subnet router + Sentinel watchdog container.
- **`.env.example`**: Clean environment template with secure defaults.
- **`watchdog/monitor.py`**: Auto-detects public WAN IP shifts, internet drops, and sends instant Telegram alerts.
- **`QUICKSTART.md`**: 3-minute setup guide with QR code mobile connection instructions.

---

## 💡 Support the Project
Created by [DimusTech](https://youtube.com/c/dimustech) / [Dima K.](https://ko-fi.com/dimiboy).
Check out our other developer kits on [Ko-fi Shop](https://ko-fi.com/dimiboy/shop).
