# /// script
# dependencies = [
#     "trio<0.22",
# ]
# ///
"""trio.nursery で複数のエラーをMultiErrorで受け取るサンプル

0.25 で MultiError なくなっている
"""

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

    except trio.MultiError as err:
        print(f"同時に発生したエラー: {err}")

    await trio.sleep(5)  # 👶👶👶がprintされないことを確認
    print("閉園")


if __name__ == "__main__":
    trio.run(main)
