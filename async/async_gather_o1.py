import asyncio
import threading
from datetime import datetime
import random

async def do_async_job() -> int:
    await asyncio.sleep(2)
    print(datetime.now().isoformat(), 'thread id', threading.current_thread().ident)
    return random.randint(1, 10)

async def main() ->None:
    # 依順序進行，每一次都會sleep，沒有切換工作
    # await do_async_job()
    # await do_async_job()
    # await do_async_job()

    # 使用gather使task可非同步切換
    job1 = do_async_job()
    job2 = do_async_job()
    job3 = do_async_job()
    return_values = await asyncio.gather(job1, job2, job3)
    for v in return_values:
        print(f'result => {v}')

    # 也可用list包裝
    jobs = [do_async_job() for _ in range(3)]
    return_values = await asyncio.gather(*jobs)
    for v in return_values:
        print(f'result2 => {v}')


asyncio.run(main())