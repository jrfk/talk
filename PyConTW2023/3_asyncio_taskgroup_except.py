import asyncio


async def coro_success():
    return "success"


async def coro_value_err():
    raise ValueError(444)


async def coro_type_err():
    raise TypeError(123)


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(coro_success())
            task2 = tg.create_task(coro_value_err())
            task3 = tg.create_task(coro_type_err())
        results = [task1.result(), task2.result(), task3.result()]
    except* ValueError as err:
        print(f"{err=}")
    except* TypeError as err:
        print(f"{err=}")


asyncio.run(main())
