import asyncio


async def coro_success():
    return "成功"


async def coro_value_err():
    raise ValueError


async def coro_type_err():
    raise TypeError


async def main():
    """return_exceptions=Trueあり"""
    results = await asyncio.gather(
        coro_success(), coro_value_err(), coro_type_err(), return_exceptions=True)
    print(f"{results=}")


asyncio.run(main())
