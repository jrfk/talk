# /// script
# requires-python = ">=3.11"
# ///
"""asyncio.timeoutで複数のエラーをexcept*で受け取れないサンプル"""

import asyncio
from _common_module_asyncio import (
    coro_success,
    coro_value_err,
    coro_type_err,
    triplet_nap,
)  # サンプルのコルーチンをインポート


async def main():
    try:
        task1 = asyncio.create_task(coro_success())
        task2 = asyncio.create_task(coro_value_err())
        task3 = asyncio.create_task(coro_type_err())
        task4 = asyncio.create_task(triplet_nap())
        async with asyncio.timeout(1):
            await task1
            await task2
            await task3
            await task4
    except* Exception as err:
        print(f"{err.exceptions=}")

    print(f"タスクの状態 {task1._state=}")
    print(f"タスクの状態 {task2._state=}")
    print(f"タスクの状態 {task3._state=}")
    print(f"タスクの状態 {task4._state=}")
    await asyncio.sleep(5)
    print("完了")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
