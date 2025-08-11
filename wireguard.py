import subprocess
import random
import time
import os
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

current_tunnel = [None] 

def activate_tunnel(tunnel_path):
    tunnel_name = os.path.splitext(os.path.basename(tunnel_path))[0]
    current_tunnel[0] = tunnel_name

    print(f"Activating tunnel: {tunnel_name}")
    subprocess.run([WIREGUARD_EXE, "/uninstalltunnelservice", tunnel_name], check=False)
    subprocess.run([WIREGUARD_EXE, "/installtunnelservice", tunnel_path], check=True)
    print(f"Connected to tunnel: {tunnel_name}")

async def fetch(session, url):
    last_choice = None
    while True:
        try:
            async with session.get(url) as response:
                if response.status in {429, 403, 401}:
                    print(f"Blocked or rate limited ({response.status}). Switching tunnel...")
                    selected = random.choice(tunnels)
                    while selected == last_choice:
                        selected = random.choice(tunnels)
                    activate_tunnel(selected)
                    last_choice = selected
                    await asyncio.sleep(5) 
                    continue
                text = await response.text()
                return text
        except Exception as e:
            print(f"Request failed: {e}. Retrying...")
            await asyncio.sleep(3)

async def fetch_all(session):
    url = "Add your desired URL"
    tasks = [asyncio.create_task(fetch(session, url)) for _ in range(10000)] 
    results = await asyncio.gather(*tasks)
    return results

async def main():
    async with aiohttp.ClientSession() as session:
        results = await fetch_all(session)
        print(f"Fetched {len(results)} pages successfully.")

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"The operation on tunnel {current_tunnel[0]} took {end - start:.2f} seconds.")
