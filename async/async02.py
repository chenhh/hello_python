# -*- coding: UTF-8 -*-
# python 3.11
import asyncio
import time


def block_do_something(idx: int):
    print(f"第 {idx} 次開始")
    time.sleep(1)    # 會在此處阻塞
    print(f"第 {idx} 次結束")


def block_main():
    start = time.time()
    for i in range(5):
        block_do_something(i + 1)
    # 5 secs，因為每次呼叫函數都阻塞1秒
    print(f"block time: {(time.time() - start):.2f} (s)")


async def do_something(idx: int):
    print(f"第 {idx} 次開始")
    await asyncio.sleep(1)
    print(f"第 {idx} 次結束")


def async_main():
    start = time.time()
    # 包裝成tasks, 不可直接傳coroutine
    tasks = [asyncio.create_task(do_something(i + 1)) for i in range(5)]
    asyncio.run(asyncio.wait(tasks))
    # 1 sec, 因為每次呼叫函數時，只要sleep就釋放所有權處理下一個函數，因此等待時間重疊。
    print(f"async time: {(time.time() - start):.2f} (s)")


if __name__ == "__main__":
    # block_main()
    async_main()