# Experimental code in Python 3.11.0rc2
import asyncio


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(some_coro(...))
            task2 = tg.create_task(another_coro(...))
    except* BaseException as e:
        print(f"{e=}")


with asyncio.Runner() as runner:
    runner.run(main())
