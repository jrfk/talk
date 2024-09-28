# /// script
# dependencies = [
#     "trio-util",
#     "trio-websocket",
#     "trio<0.22",
# ]
# ///
"""AsyncValueで複数の入力を待つ"""

import trio
from trio_util import AsyncValue, compose_values
from trio_websocket import connect_websocket


async def fetch(ws: connect_websocket, event1: AsyncValue, event2: AsyncValue):
    while True:
        try:
            message = await ws.get_message()
            # print(f"websocketからの値: {message}")
            if int(message) / 2 % 1:
                event1.value = "👶 :" + message + "を受け取ったよ"
                event2.value = ""
            else:
                event1.value = ""
                event2.value = "🍼 :" + message + "を受け取ったよ"
        except trio.EndOfChannel:
            print("Connection closed")
            break


async def main():
    async with trio.open_nursery() as nursery:
        ws = await connect_websocket(
            nursery=nursery, host="localhost", port=8888, resource="/", use_ssl=False
        )
        event1 = AsyncValue("👶")
        event2 = AsyncValue("🍼")
        nursery.start_soon(fetch, ws, event1, event2)

        with compose_values(event1=event1, event2=event2) as composite_event:
            async for v in composite_event.eventual_values():
                print(f"{v=}")


if __name__ == "__main__":
    try:
        trio.run(main)
    except* KeyboardInterrupt:
        print("Interrupted!")
