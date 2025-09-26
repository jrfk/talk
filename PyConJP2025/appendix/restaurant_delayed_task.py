import asyncio
import random

async def customer(time: int):
    await waiter(time)


async def waiter(time: int):
    await chef(time)


async def chef(time: int):
    await cooking(time)
    # x = asyncio.create_task(cooking(time), name="cooking-2.1")
    # x2 = asyncio.create_task(cooking(time), name="cooking-2.2")
    # await asyncio.gather(x2, x, return_exceptions=True)


async def cooking(time: int):
    # await monitor()
    await asyncio.sleep(time)



async def monitor():
    # asyncio.print_call_graph(None, depth=1, limit=5)
    # asyncio.format_call_graph(None, depth=1, limit=5)
    # graph = asyncio.format_call_graph()
    # for frame in graph.call_stack:
    #     print(frame)

    # asyncio.capture_call_graph(None, depth=1, limit=5)
    graph = asyncio.capture_call_graph()
    for frame in graph.call_stack:
        print(frame)


async def restaurant():
    await asyncio.sleep(20)
    async with asyncio.taskgroups.TaskGroup() as tg:
        tg.create_task(customer(random.randint(1, 5)), name="customer1")
        tg.create_task(customer(random.randint(1, 5)), name="customer2")
        tg.create_task(customer(random.randint(1, 5)), name="customer3")
        tg.create_task(customer(30), name="customer4")  # 1つだけ遅いタスクを特定する
        tg.create_task(customer(random.randint(1, 5)), name="customer5")
        tg.create_task(customer(random.randint(1, 5)), name="customer6")
        tg.create_task(customer(random.randint(1, 5)), name="customer7")
        tg.create_task(customer(random.randint(1, 5)), name="customer8")
        tg.create_task(customer(random.randint(1, 5)), name="customer9")
        await asyncio.sleep(1000)


asyncio.run(restaurant())
