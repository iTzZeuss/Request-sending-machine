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
current_tunnel = []

def activate_tunnel(tunnel_path):
    tunnel_name = os.path.splitext(os.path.basename(tunnel_path))[0]
    current_tunnel[0] = tunnel_name
    
    subprocess.run([WIREGUARD_EXE, "/uninstalltunnelservice", tunnel_name])

    subprocess.run([WIREGUARD_EXE, "/installtunnelservice", tunnel_path])
    print(f"Connected to tunnel: {tunnel_name}")

async def fetch(s, url):
    
    async with s.get(url) as r:
        if r.status == 429 or 403 or 401:
            while True:
                last_choice = None
                selected = random.choice(tunnels)
                while selected == last_choice:
                    selected = random.choice(tunnels)
                activate_tunnel(selected)
                selected = last_choice       
    return await r.text()
    
async def fetch_all(s):
    tasks = []
    for url in range(10000):
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
        
    res = await asyncio.gather(*tasks)
    return res
            
async def main(s, urls):
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session)

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(fetch_all())
    end = time.perf_counter()
    print(f"The operation on tunnel {current_tunnel[0]} took {end - start} seconds.")
