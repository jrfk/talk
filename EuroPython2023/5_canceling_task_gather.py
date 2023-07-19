import asyncio


async def coro_success():
    return "success"


async def coro_value_err():
    raise ValueError


async def coro_long():
    try:
        await asyncio.sleep(1)
        print("coro_long: Task is still running.")
        return "success?"
    except asyncio.CancelledError as err:
        print("coro_long: Task was cancelled.")
        raise asyncio.CancelledError


async def main():
    try:
        task1 = asyncio.create_task(coro_success())
        task2 = asyncio.create_task(coro_value_err())
        task3 = asyncio.create_task(coro_long(), name="Coroutine to remain")  # Naming tasks for better clarity

        results = await asyncio.gather(*[task1, task2, task3])
        print(f"{results=}")
    except ValueError as err:
        print(f"{err=}")
    print(f"State of Task 1 {task1._state=}")
    print(f"State of Task 2 {task2._state=}")
    print(f"Initial state of Task 3 {task3._state=}")  # Not cancelled yet.
    for task in [task1, task2, task3]:
        if task.done() is False:
            task.cancel()  # Cancel uncompleted tasks
    print(
        f"Subsequent state of Task 3 {task3._state=}"
    )  # At this point, cancellation is only requested, not yet effected.

    await asyncio.sleep(1)
    # asyncio.gather() to wait for cancellation
    # results = await asyncio.gather(*[task3], return_exceptions=True)  # If another exception occurs during the cancel...

    print(f"Final state of Task 3 {task3._state=}")  # After the CancelledError process is complete, it will be cancelled.


asyncio.run(main())
