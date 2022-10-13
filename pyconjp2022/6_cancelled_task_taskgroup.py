import asyncio


async def coro_success():
    return "成功"


async def coro_value_err():
    raise ValueError


async def coro_long():
    try:
        await asyncio.sleep(1)
        print("完了していないタスクが出力しています")
        return "成功？"
    except asyncio.CancelledError as err:
        print("キャンセルされたタスクが出力しています")
        await asyncio.sleep(1)
        raise asyncio.CancelledError


async def main():
    try:
        async with asyncio.TaskGroup() as g:
            task1 = g.create_task(coro_success())
            task2 = g.create_task(coro_value_err())
            task3 = g.create_task(coro_long(), name="残るコルーチン")
        results = [task1.result(), task2.result(), task3.result()]
        print(f"{results=}")
    except* BaseException as err:
        print(f"{err=}")

    print(f"タスク1の状態 {task1._state=}")
    print(f"タスク2の状態 {task2._state=}")
    print(f"タスク3の状態 {task3._state=}")
    # memo CancelledErrorを捕捉後 raise asyncio.CancelledErrorがないとタスクの状態がFINISHEDになる


asyncio.run(main())
