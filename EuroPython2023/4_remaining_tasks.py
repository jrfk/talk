import asyncio


async def coro_success():
    return "success"


async def coro_value_err():
    raise ValueError


async def coro_long():
    await asyncio.sleep(1)
    print("coro_long: Task is still running.")
    return "DONE?"


async def main():
    try:
        task1 = asyncio.create_task(coro_success())
        task2 = asyncio.create_task(coro_value_err())
        task3 = asyncio.create_task(coro_long(), name="Coroutine to remain")  # Naming tasks for better clarity

        results = await asyncio.gather(*[task1, task2, task3])
        print(f"{results=}")
    except ValueError as err:
        print(f"{err=}")
    print("DONE")
    print(f"State of Task 1 {task1._state=}")
    print(f"State of Task 2 {task2._state=}")
    print(f"State of Task 3 {task3._state=}")
    await asyncio.sleep(1.5)  # Wait for 1.5 seconds to ensure that coro_log() continues to work even after an Exception occurs.


asyncio.run(main())
