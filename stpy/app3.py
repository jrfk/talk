import asyncio
import time


"""並行にならない"""
async def thinking(thinking_time: int) -> str:
    """考え中のお客様が悩んだ末、注文するコルーチン"""
    await asyncio.sleep(thinking_time)  # お客様の長い待ち時間
    return "ざるそば"


async def order() -> None:
    """注文を聞きに行く"""
    start = time.time()
    print("ご注文は？")
    result1: str = await thinking(1)
    result2: str = await thinking(2)
    result3: str = await thinking(3)

    # コルーチンは実行するだけでは並行にはならない
    # 並行にするためにはタスクが必要
    print([result1, result2, result3])
    print(f"time: {time.time() - start}")  # 終了までにかかった時間を出力


asyncio.run(order())