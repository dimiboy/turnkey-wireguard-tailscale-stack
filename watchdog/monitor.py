"""
Sentinel VPN & Remote Access Health Monitor
Checks gateway ping, public IP changes, and delivers instant Telegram alerts.
"""
import os
import time
import urllib.request
import json
import socket

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()
INTERVAL = int(os.getenv("CHECK_INTERVAL_SECONDS", "60"))

def send_telegram(message: str):
    if not BOT_TOKEN or not CHAT_ID:
        print(f"[LOG] Alert suppressed (no bot credentials): {message}")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            pass
    except Exception as e:
        print(f"[ERR] Failed to send Telegram alert: {e}")

def get_public_ip():
    try:
        with urllib.request.urlopen("https://api.ipify.org", timeout=5) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception:
        return None

def main():
    print("VPN Sentinel Watchdog started.")
    last_ip = get_public_ip()
    send_telegram(f"🛡️ <b>Remote Access Sentinel Online</b>\nInitial WAN IP: <code>{last_ip or 'Unknown'}</code>\nHost: <code>{socket.gethostname()}</code>")

    consecutive_failures = 0

    while True:
        time.sleep(INTERVAL)
        current_ip = get_public_ip()
        
        if current_ip is None:
            consecutive_failures += 1
            if consecutive_failures == 3:
                send_telegram("⚠️ <b>WAN Alert: Home internet gateway unreachable!</b>\nWireGuard / Tailscale tunnels may be offline.")
        else:
            if consecutive_failures >= 3:
                send_telegram(f"✅ <b>WAN Restored: Home internet connection is back online.</b>\nCurrent IP: <code>{current_ip}</code>")
            consecutive_failures = 0
            
            if last_ip and current_ip != last_ip:
                send_telegram(f"🔄 <b>Public WAN IP Changed</b>\nOld: <code>{last_ip}</code>\nNew: <code>{current_ip}</code>\n<i>Verify DDNS record or WireGuard WG_HOST.</i>")
                last_ip = current_ip
            elif not last_ip:
                last_ip = current_ip

if __name__ == "__main__":
    main()
