# -*- coding: UTF-8 -*-
import asyncio


async def coro():
    print('hello')
    await asyncio.sleep(1)
    print('world')


if __name__ == '__main__':
    # 取得事件迴圈後再run
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(coro())
    # loop.run_until_complete(task)

    # 也可直接用run
    asyncio.run(coro())
