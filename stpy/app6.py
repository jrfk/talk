import asyncio
import time
import httpx


"""asyncio対応のライブラリを利用した並行処理の例
pip install httpx してください
"""
async def thinking(client: httpx.AsyncClient, user: int) -> str:
    """考え中のお客様が悩んだ末、注文するコルーチン"""
    print(f"何しようかな... {user}人目")
    response = await client.get("https://www.google.com/search?q=スタ蕎麦で一番おいしいお蕎麦は？")
    # await asyncio.sleep(thinking_time)  # お客様の長い待ち時間
    print("決まった！")  # 追加
    return response, "ざるそば"


async def order() -> None:
    """注文を聞きに行く"""
    start = time.time()
    print("ご注文は？")
    async with httpx.AsyncClient() as client:
        tasks = [thinking(client, 1), thinking(client, 2), thinking(client, 3)]
        result: list = await asyncio.gather(*tasks)
    print(f"{result=}")
    print(f"time: {time.time() - start}")  # 終了までにかかった時間を出力


asyncio.run(order())
