import asyncio
import random

async def customer(time: int):
    await waiter(time)


async def waiter(time: int):
    await chef(time)


async def chef(time: int):
    await cooking(time)


async def cooking(time: int):
    await asyncio.sleep(time)


async def restaurant():
    await asyncio.sleep(20)
    async with asyncio.taskgroups.TaskGroup() as tg:
        tg.create_task(customer(random.randint(1, 5)), name="customer1")
        tg.create_task(customer(random.randint(1, 5)), name="customer2")
        tg.create_task(customer(random.randint(1, 5)), name="customer3")
        tg.create_task(cooking(2), name="cooking2.0")  # irregular task 想定外に直接料理している
        await asyncio.sleep(1000)


asyncio.run(restaurant())
