import asyncio


async def coro_success():
    return "成功"


async def coro_value_err():
    raise ValueError


async def coro_long():
    await asyncio.sleep(1)
    print("完了していないタスクが出力しています")
    return "成功？"


async def main():
    try:
        task1 = asyncio.create_task(coro_success())
        task2 = asyncio.create_task(coro_value_err())
        task3 = asyncio.create_task(coro_long(), name="残るコルーチン")  # 分かりやすくするためタスクに名づけ

        results = await asyncio.gather(*[task1, task2, task3])
        print(f"{results=}")
    except ValueError as err:
        print(f"{err=}")
    print("終了")
    print(f"タスク1の状態 {task1._state=}")
    print(f"タスク2の状態 {task2._state=}")
    print(f"タスク3の状態 {task3._state=}")
    await asyncio.sleep(1.5)  # 1.5秒待つことでException発生後にcoro_log()が動いていることを確認できる


asyncio.run(main())
