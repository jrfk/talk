# pip install httpx
import asyncio
from time import time
import httpx

URL = "https://pokeapi.co/api/v2/pokemon/"


async def access_url_poke(client, num: int) -> str:
    r = await client.get(f"{URL}{num}")
    pokemon = r.json()  # JSONパース
    return pokemon["name"]  # ポケ名を抜く


async def main_poke():
    """httpxでポケモン151匹引っこ抜く"""
    start = time()
    async with httpx.AsyncClient() as client:
        try:
            async with asyncio.TaskGroup() as tg:
                tasks = [
                    tg.create_task(access_url_poke(client, number))
                    for number in range(1, 151)
                ]
        except* BaseException as e:
            print(f"{e=}")

    results = [task.result() for task in tasks]
    print(results)
    print("time: ", time() - start)


asyncio.run(main_poke())
