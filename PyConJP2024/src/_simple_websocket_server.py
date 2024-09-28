# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "websockets",
# ]
# ///
"""シンプルなWebSocketサーバーが起動しますランダムに0から9までの数字を送信します

$ uv run _simple_websocket_server.py"""

import asyncio
import random
import websockets
from websockets.server import WebSocketServerProtocol


async def handler(websocket: WebSocketServerProtocol) -> None:
    """Handle the incoming WebSocket connection."""
    while True:
        number = random.randint(1, 4)
        await asyncio.sleep(number)
        await websocket.send(str(number))
        print(f"Sent: {number}")


async def main() -> None:
    """Start the WebSocket server."""
    async with websockets.serve(handler, "localhost", 8888):
        print("WebSocket server started on ws://localhost:8888")
        await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except* KeyboardInterrupt:
        print("Interrupted!")
