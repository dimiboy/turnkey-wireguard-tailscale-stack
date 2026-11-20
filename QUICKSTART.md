# 3-Minute Quickstart Guide

## Step 1: Clone & Configure
```bash
git clone https://github.com/dimiboy/turnkey-wireguard-tailscale-stack.git
cd turnkey-wireguard-tailscale-stack
cp .env.example .env
```
Edit `.env` with your preferred password and DDNS / WAN hostname:
```bash
nano .env
```

---

## Step 2: Launch Containers
```bash
docker compose up -d
```

---

## Step 3: Access WireGuard Web UI
1. Open your browser: `http://localhost:51821` (or `http://YOUR_SERVER_IP:51821`).
2. Enter your password configured in `.env`.
3. Click **+ New Client** (e.g. `Phone`, `Laptop`).
4. Scan the QR code with the official WireGuard app or download the `.conf` file.

---

## Step 4: Tailscale Subnet Routing (Zero Port-Forwarding)
1. Add your Tailscale Auth Key to `.env` (`TS_AUTHKEY=your_tailscale_auth_key_here`).
2. Run `docker compose restart tailscale`.
3. In your Tailscale Admin Console (`login.tailscale.com/admin/machines`):
   - Find `homelab-gateway`.
   - Click **...** → **Edit route settings** → Approve subnet routes (`192.168.1.0/24`).
   - You now have secure, encrypted remote access to all your local home network devices from anywhere in the world!
