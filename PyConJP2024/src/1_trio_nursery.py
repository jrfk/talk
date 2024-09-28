# /// script
# dependencies = [
#     "trio",
# ]
# ///
"""trio.nursery のサンプル"""

import trio
from _common_module_trio import child  # サンプルのコルーチンをインポート


async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(child)
        nursery.start_soon(child)
        nursery.start_soon(child)
        nursery.start_soon(child)
    print("閉園")


if __name__ == "__main__":
    trio.run(main)
