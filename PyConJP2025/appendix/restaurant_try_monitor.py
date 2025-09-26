import asyncio

async def customer():
    await waiter()

async def waiter():
    await chef()

async def chef():
    await cooking()

async def cooking():
    await monitor()  # try monitor
    await asyncio.sleep(500)  # 調理中

async def monitor():
    asyncio.print_call_graph(None, depth=1, limit=5)
    # asyncio.format_call_graph(None, depth=1, limit=5)

    # graph = asyncio.format_call_graph()
    # for frame in graph.call_stack:
    #     print(frame)


async def restaurant():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(customer(), name="customer1.0")  # タスク名を customer1.0 に設定
        await asyncio.sleep(1000)

asyncio.run(restaurant())