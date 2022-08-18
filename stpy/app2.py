import asyncio
import time


# def thinking() -> str:
#     """考え中のお客様が悩んだ末、注文するコルーチン"""
#     time.sleep(1)  # お客様の長い待ち時間
#     return "ざるそば"


# def order() -> None:
#     """注文を聞きに行く"""
#     print("ご注文は？")
#     result: str = thinking()
#     print(result)

# order()


"""動くコルーチン"""
async def thinking() -> str:
    """考え中のお客様が悩んだ末、注文するコルーチン"""
    await asyncio.sleep(1)  # お客様の長い待ち時間
    return "ざるそば"


async def order() -> None:
    """注文を聞きに行く"""
    print("ご注文は？")
    result: str = await thinking()
    print(result)


asyncio.run(order())
