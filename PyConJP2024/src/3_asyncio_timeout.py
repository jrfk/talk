# /// script
# requires-python = ">=3.11"
# ///
"""asyncio.timeoutのサンプル"""

import asyncio
from _common_module_asyncio import (
    coro_success,
    coro_value_err,
    coro_type_err,
    triplet_nap,
)  # サンプルのコルーチンをインポート


async def main():
    try:
        async with asyncio.timeout(1):
            await triplet_nap()
    except TimeoutError as err:
        print(f"{err=}")
        print("ちゃんとおきてね")
    print("おわり")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
