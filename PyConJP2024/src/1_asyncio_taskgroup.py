# /// script
# requires-python = ">=3.11"
# ///
"""asyncio.TaskGroupで複数のエラーをexcept*で受け取るサンプル

cf. https://speakerdeck.com/jrfk/python3-dot-11xin-ji-neng-asyncio-dot-taskgroup-to2022nian-asynciono-hello-ish-world
"""

import asyncio
from _common_module_asyncio import child  # サンプルのコルーチンをインポート


async def main():
    async with asyncio.TaskGroup() as g:
        g.create_task(child())
        g.create_task(child())
        g.create_task(child())
        g.create_task(child(), name="よく寝てる")
    print("閉園")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
