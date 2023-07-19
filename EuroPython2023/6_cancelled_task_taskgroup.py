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
        await asyncio.sleep(1)
        raise asyncio.CancelledError
        # Note: Without 'raise asyncio.CancelledError' after catching CancelledError, the task's state becomes FINISHED.


async def main():
    try:
        async with asyncio.TaskGroup() as g:
            task1 = g.create_task(coro_success())
            task2 = g.create_task(coro_value_err())
            task3 = asyncio.create_task(coro_long(), name="Coroutine to remain")  # Naming tasks for better clarity
        results = [task1.result(), task2.result(), task3.result()]
        print(f"{results=}")
    except* BaseException as err:
        print(f"{err=}")

    print(f"State of Task 1 {task1._state=}")
    print(f"State of Task 2 {task2._state=}")
    print(f"State of Task 3 {task3._state=}")


asyncio.run(main())
