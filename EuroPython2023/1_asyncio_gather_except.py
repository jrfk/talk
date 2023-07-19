import asyncio


async def coro_success():
    return "success"


async def coro_value_err():
    raise ValueError


async def coro_type_err():
    raise TypeError


async def main():
    """return_exceptions False"""
    try:
        results = await asyncio.gather(
            coro_success(), coro_value_err(), coro_type_err()
        )
        print(f"{results=}")
    except ValueError as err:
        print(f"{err=}")
    except TypeError as err:
        print(f"{err=}")


asyncio.run(main())
