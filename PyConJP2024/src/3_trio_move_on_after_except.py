# /// script
# dependencies = [
#     "trio<0.26",
# ]
# ///
"""trio.move_on_after でタイムアウト"""

import trio
from _common_module_trio import (
    triplet_nap,
)  # サンプルのコルーチンをインポート


async def main():
    try:
        with trio.move_on_after(1) as cancel_scope:  # 1秒でタイムアウト
            await triplet_nap()
    except* Exception as err:
        print(f"{err.exceptions=}")  # ここには来ない
        print("ちゃんとおきてね")
    print("おわり")


if __name__ == "__main__":
    trio.run(main)
