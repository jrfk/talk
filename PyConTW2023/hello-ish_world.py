# Experimental code in Python 3.11.3
import asyncio


async def some_coro():
    return "success"


async def another_coro():
    return "success"


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(some_coro(...))
            task2 = tg.create_task(another_coro(...))
    except* BaseException as e:
        print(f"{e=}")


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
