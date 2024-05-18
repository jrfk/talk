""" $ python simple_websocket_server.py """
import asyncio
import random
import websockets
from websockets.server import WebSocketServerProtocol

async def random_number_generator() -> int:
    """Generate a random number between 0 to 9"""
    return random.randint(0, 9)

async def handler(websocket: WebSocketServerProtocol) -> None:
    """Handle the incoming WebSocket connection."""
    while True:
        await asyncio.sleep(random.uniform(0.1, 0.5))  # Wait for a random duration between 1 and 5 seconds
        number = await random_number_generator()
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
