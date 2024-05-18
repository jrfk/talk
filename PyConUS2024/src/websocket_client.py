import trio
from trio_websocket import open_websocket_url


class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.websocket = None

    async def connect(self):
        self.websocket = await open_websocket_url(self.url)

    async def send_message(self, message):
        if self.websocket:
            await self.websocket.send_message(message)

    async def receive_message(self):
        if self.websocket:
            return await self.websocket.get_message()

    async def disconnect(self):
        if self.websocket:
            await self.websocket.aclose()
            self.websocket = None
