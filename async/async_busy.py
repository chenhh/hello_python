import asyncio
import threading

from time import sleep


def hard_work():
    print('thread id:', threading.get_ident())
    sleep(3)


async def do_async_job():
    hard_work()
    await asyncio.sleep(1)
    print('job done!')


async def main():
    task1 = asyncio.create_task(do_async_job())
    task2 = asyncio.create_task(do_async_job())
    task3 = asyncio.create_task(do_async_job())
    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    # ask1, task2, task3 其實都各花 3 秒在 sleep ，
    # 同時也阻塞其他工作的進行，因此造成這個範例花費約 9 秒
    asyncio.run(main())
