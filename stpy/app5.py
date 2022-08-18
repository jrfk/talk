import asyncio
import time
import requests as requests


"""コルーチンでasyncio対応していないライブラリを使用するダメな例
pip install requests してください
"""
async def thinking(user: int) -> str:
    """考え中のお客様が悩んだ末、注文するコルーチン"""
    print(f"何しようかな... {user}人目")
    response = requests.get("https://www.google.com/search?q=おいしいお蕎麦は？")
    # await asyncio.sleep(thinking_time)  # お客様の長い待ち時間
    print("決まった！")  # 追加
    return response, "ざるそば"


async def order() -> None:
    """注文を聞きに行く"""
    start = time.time()
    print("ご注文は？")
    tasks = [
        thinking(1),
        thinking(2),
        thinking(3)
    ]
    result: list = await asyncio.gather(*tasks)
    print(f"{result=}")
    print(f"time: {time.time() - start}")  # 終了までにかかった時間を出力


asyncio.run(order(), debug=True)
