# /// script
# dependencies = [
#     "trio",
# ]
# ///
"""共通で使うコルーチンを定義するモジュール"""

import trio


async def coro_success():
    return "成功"


async def coro_value_err():
    raise ValueError


async def coro_type_err():
    raise TypeError


async def triplet_nap():
    print("長いコルーチン 開始")
    await trio.sleep(3)
    print("👶👶👶")
    return "閉園だから帰りましょう"


async def child():
    print("👶子コルーチン こんにちは")
    await grandchild()
    print("👶 さようなら")


async def grandchild():
    print("👶👶孫コルーチン こんにちは")
    await trio.sleep(0.1)
    print("👶👶 さようなら")
