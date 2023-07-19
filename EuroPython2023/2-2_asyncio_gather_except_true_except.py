import asyncio


async def coro_success():
    return "success"


async def coro_value_err():
    raise ValueError


async def coro_type_err():
    raise TypeError


async def main():
    """return_exceptions=True"""
    results = await asyncio.gather(
        coro_success(), coro_value_err(), coro_type_err(), return_exceptions=True
    )
    print(f"{results=}")

    for result in results:
        match result:
            case ValueError():
                print("ValueError")
            case TypeError():
                print("TypeError")


asyncio.run(main())
