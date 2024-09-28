# /// script
# requires-python = ">=3.11"
# ///
"""asyncio.TaskGroupで複数のエラーをexcept*で受け取るサンプル

cf. https://speakerdeck.com/jrfk/python3-dot-11xin-ji-neng-asyncio-dot-taskgroup-to2022nian-asynciono-hello-ish-world
"""

import asyncio
from _common_module_asyncio import (
    coro_success,
    coro_value_err,
    coro_type_err,
    triplet_nap,
)  # サンプルのコルーチンをインポート


async def main():
    try:
        async with asyncio.TaskGroup() as g:
            task1 = g.create_task(coro_success())
            task2 = g.create_task(coro_value_err())
            task3 = g.create_task(coro_type_err())
            task4 = g.create_task(triplet_nap(), name="よく寝てる")
        results = [task1.result(), task2.result(), task3.result()]
        print(f"{results=}")
    except* Exception as err:
        print(f"{err.exceptions=}")

    # print(f"完了していないタスク {task1._state=}")
    # print(f"完了していないタスク {task2._state=}")
    # print(f"完了していないタスク {task3._state=}")
    # print(f"完了していないタスク {task4._state=}")
    await asyncio.sleep(5)  # 👶👶👶がprintされないことを確認
    print("閉園")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
