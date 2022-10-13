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
        raise asyncio.CancelledError


async def main():
    try:
        task1 = asyncio.create_task(coro_success())
        task2 = asyncio.create_task(coro_value_err())
        task3 = asyncio.create_task(coro_long(), name="残るコルーチン")  # 分かりやすくするためタスクに名づけ

        results = await asyncio.gather(*[task1, task2, task3])
        print(f"{results=}")
    except ValueError as err:
        print(f"{err=}")
    print(f"タスク1の状態 {task1._state=}")
    print(f"タスク2の状態 {task2._state=}")
    print(f"タスク3の状態 {task3._state=}")  # この時点ではキャンセルされていない
    for task in [task1, task2, task3]:
        if task.done() is False:
            task.cancel()  # 未完了のタスクをキャンセル
    print(f"タスク3の状態 {task3._state=}")  # この時点でもキャンセル依頼されただけでキャンセルされていない

    await asyncio.sleep(1)
    # キャンセルを待ち合わせるための asyncio.gather()
    # results = await asyncio.gather(*[task3], return_exceptions=True)  # もしキャンセル中に別の例外が発生したら...

    print(f"タスク3の状態 {task3._state=}")  # CancelledError内の処理が完了後、キャンセルになる


asyncio.run(main())
