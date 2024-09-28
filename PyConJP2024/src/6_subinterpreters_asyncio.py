# /// script
# requires-python = ">=3.12"
# ///
"""subinterpreters asyncio

cf. https://speakerdeck.com/jrfk/python3-dot-11xin-ji-neng-asyncio-dot-taskgroup-to2022nian-asynciono-hello-ish-world
"""

import asyncio
import threading
import _xxsubinterpreters as interpreters  # Python 3.12 から導入


# サブインタプリタで実行する関数
def run_sub_interpreter():
    interp_id = interpreters.create()
    interpreters.run_string(
        interp_id,
        """
import asyncio

async def async_task():
    for i in range(5):
        print(f"Sub-interpreter: {i}")
        await asyncio.sleep(1)

async def main():
    await async_task()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
""",
    )


# メインスレッドで実行するasyncioタスク
async def main_task():
    for i in range(5):
        print(f"Main interpreter: {i}")
        await asyncio.sleep(1)


# サブインタプリタをスレッドで実行
sub_interpreter_thread = threading.Thread(target=run_sub_interpreter)
sub_interpreter_thread.start()

# メインスレッドでイベントループを実行
asyncio.run(main_task())

# サブインタプリタのスレッドが完了するまで待機
sub_interpreter_thread.join()
