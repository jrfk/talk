import asyncio
import time


"""printとデバッグで並行になる動きを見てみよう"""
async def thinking(thinking_time: int) -> str:
    """考え中のお客様が悩んだ末、注文するコルーチン"""
    print("何しようかな...")  # 追加
    await asyncio.sleep(thinking_time)  # お客様の長い待ち時間
    print("決まった！")  # 追加
    return "ざるそば"


async def order() -> None:
    """注文を聞きに行く"""
    start = time.time()
    print("ご注文は？")
    task1: asyncio.Task = asyncio.create_task(thinking(1))
    task2: asyncio.Task = asyncio.create_task(thinking(2))
    task3: asyncio.Task = asyncio.create_task(thinking(3))
    print("ご注文は？")  # 追加
    result1: str = await task1
    print(f"{result1=}")  # 追加
    result2: str = await task2
    print(f"{result2=}")  # 追加
    result3: str = await task3
    print(f"{result3=}")  # 追加
    print([result1, result2, result3])
    print(f"time: {time.time() - start}")  # 終了までにかかった時間を出力

    # タスクが順に実行され、すでにtask1のawait時点でtask2,task3も実行されることがわかります。
    # キーになるのはタスクとawait、これがasyncioの並行処理の鍵となります。

    # 6.これを書く さらにgatherです。これはタスクを渡しても良いのですが、コルーチンをまとめて渡すこともできます。
    # 内部でまとめてタスクにしてくれてさらに、渡した順番通りに結果を返してくれるものです。
    # tasks = [thinking(i) for i in range(3)]
    # tasks = [
    #     thinking(1),
    #     thinking(2),
    #     thinking(3)
    # ]
    # result: list = await asyncio.gather(*tasks)
    # print(f"{result=}")


asyncio.run(order())