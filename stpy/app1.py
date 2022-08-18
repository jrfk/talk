import asyncio
import time

# 逐次関数
# def thinking() -> str:
#     """考え中のお客様が悩んだ末、注文するコルーチン"""
#     time.sleep(1)  # お客様の長い待ち時間
#     return "ざるそば"


# result: str = thinking()
# print(result)

"""動かないコルーチン"""
async def thinking() -> str:
    """考え中のお客様が悩んだ末、注文するコルーチン"""
    await asyncio.sleep(1)  # お客様の長い待ち時間
    return "ざるそば"


result: str = thinking()
print(result)

## エラーを見てみる
# result = await thinking()
# print(result)
