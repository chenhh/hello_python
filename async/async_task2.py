# -*- coding: UTF-8 -*-

import asyncio
import time


async def say_after(delay: int, what: str) -> None:
    await asyncio.sleep(delay)
    print(what)


async def main_coroutine() -> None:
    await say_after(1, 'hello')
    await say_after(2, 'world')
    # coroutine沒經過task包裝不會節省時間, 3秒


async def main_create_task() -> None:
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))
    await task1
    await task2
    # 經過task包裝可節省時間, 2秒

async def main_gather() -> None:
    c1 = say_after(1, 'hello')
    c2 = say_after(2, 'world')
    await asyncio.gather(c1, c2)
    # 使用gather可節省時間, 2秒


def time_elapsed(func: callable) -> None:
    start = time.perf_counter()
    asyncio.run(func())
    print(f"used: {time.perf_counter() - start:.2f} s")


if __name__ == '__main__':
    time_elapsed(main_coroutine)
    time_elapsed(main_create_task)
    time_elapsed(main_gather)

