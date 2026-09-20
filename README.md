# solana-streamer

Minimalist asynchronous Python client for tracking Solana mainnet slots via WebSocket.

## Architecture
* **Protocol:** JSON-RPC 2.0 over Secure WebSockets (`wss://`)
* **Method:** `slotSubscribe`
* **Runtime:** Python `asyncio` event loop

## Setup & Running

1. Install required transport library:
```bash
pip install -r requirements.txt
```

2. Execute the script:
```bash
python solana_streamer.py
```

## JSON-RPC Payload Structure
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "slotSubscribe",
  "params": []
}
```
