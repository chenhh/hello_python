# -*- coding: UTF-8 -*-
# async 3.11
import asyncio
import time


def block_dosomething(i):
    print(f"第 {i} 次開始")
    time.sleep(1)
    print(f"第 {i} 次結束")


def block_main():
    start = time.time()
    for i in range(5):
        block_dosomething(i + 1)
    # 5 secs
    print(f"block time: {(time.time() - start):.2f} (s)")


async def dosomething(i: int, delay: int):
    print(f"第 {i} 次開始")
    await asyncio.sleep(i, delay)
    print(f"第 {i} 次結束")


def async_main():
    start = time.time()
    # 包裝成tasks, 不可直接傳coroutine
    # tasks = [dosomething(i + 1, i + 1) for i in range(5)]
    tasks = [asyncio.create_task(dosomething(i + 1, i + 1)) for i in range(5)]
    asyncio.run(asyncio.wait(tasks))
    # 5 sec
    print(f"async time: {(time.time() - start):.2f} (s)")


async def echo(msg: str, delay: float):
    await asyncio.sleep(delay)
    print(msg)


def async_main2():
    start = time.time()
    tasks = [
        asyncio.create_task(
            echo('此作業需要1秒', 1))
        , asyncio.create_task(
            echo('此作業需要2秒', 2))
    ]
    # await task1
    # await task2
    # tasks = (task1, task2)
    # loop = asyncio.new_event_loop()  # Here
    # asyncio.set_event_loop(loop)  # Here
    # loop.run_until_complete(tasks)
    asyncio.run(asyncio.wait(tasks))
    print(f'共計 {(time.time() - start):.2f} (s)')


if __name__ == "__main__":
    # block_main()
    async_main()
    # async_main2()
