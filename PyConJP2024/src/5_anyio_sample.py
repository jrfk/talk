# /// script
# dependencies = [
#     "anyio",
#     "trio",
# ]
# ///
"""anyio"""

import anyio

async def child():
    print("👶子コルーチン こんにちは")
    await grandchild()
    print("👶 さようなら")


async def grandchild():
    print("👶👶孫コルーチン こんにちは")
    await anyio.sleep(0.1)
    print("👶👶 さようなら")


async def main():
    async with anyio.create_task_group() as task_group:
        task_group.start_soon(child)
        task_group.start_soon(child)
        task_group.start_soon(child)
        task_group.start_soon(child)
    print("閉園")


if __name__ == "__main__":
    anyio.run(main, backend="asyncio")  # これをtrioに変えるだけで動く
