# /// script
# dependencies = [
#     "trio>0.25",
# ]
# ///
"""trio.nursery で複数のエラーをexcept*で受け取るサンプル"""

import trio
from _common_module_trio import (
    coro_success,
    coro_value_err,
    coro_type_err,
    triplet_nap,
)  # サンプルのコルーチンをインポート


async def main():
    try:
        async with trio.open_nursery() as nursery:
            nursery.start_soon(coro_success)
            nursery.start_soon(coro_value_err)
            nursery.start_soon(coro_type_err)
            nursery.start_soon(triplet_nap)  # よく寝てる
    except* Exception as err:
        print(f"{err.exceptions=}")
    await trio.sleep(5)  # 👶👶👶がprintされないことを確認
    print("閉園")


if __name__ == "__main__":
    trio.run(main)
