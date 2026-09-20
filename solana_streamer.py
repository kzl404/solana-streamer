import asyncio
import json
import sys
import websockets


SOLANA_WS_URL = "wss://api.mainnet-beta.solana.com"

async def main():
    async with websockets.connect(SOLANA_WS_URL, ping_interval=20, ping_timeout=20) as ws:
        print("[+] Connected to Solana WebSocket API")
        
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "slotSubscribe",
            "params": []
        }
        await ws.send(json.dumps(payload))
        
        
        raw_subscription_response = await ws.recv()
        subscription_response = json.loads(raw_subscription_response)
        print(f"[+] Subscription confirmed: {subscription_response}")
        
        async for msg in ws:
            response = json.loads(msg)
            
            params = response.get("params")
            if params:
                slot = params.get("result", {}).get("slot")
                if slot:
                    print(f"[>] New Slot: {slot}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[-] Terminated by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[-] Unexpected error: {e}")
        sys.exit(1)
