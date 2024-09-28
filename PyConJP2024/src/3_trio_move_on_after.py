# /// script
# dependencies = [
#     "trio<0.22",
# ]
# ///
"""trio.move_on_after でタイムアウト"""

import trio
from _common_module_trio import (
    triplet_nap,
)  # サンプルのコルーチンをインポート


async def main():
    with trio.move_on_after(1) as cancel_scope:  # 1秒でタイムアウト
        await triplet_nap()
    if cancel_scope.cancelled_caught:
        print("ちゃんとおきてね")
    print("おわり")


if __name__ == "__main__":
    trio.run(main)
