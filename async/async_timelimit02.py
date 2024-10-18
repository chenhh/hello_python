import asyncio


async def do_async_job():
    await asyncio.sleep(2)
    print("do async job 1")

async def do_async_job_2nd_plan():
    await asyncio.sleep(1)
    print("do async job 2")


async def main():
    try:
        await asyncio.wait_for(do_async_job(), timeout=1)
    except asyncio.TimeoutError:
        await asyncio.wait_for(do_async_job_2nd_plan(), timeout=2)


if __name__ == '__main__':
    asyncio.run(main())
    # do async job 2
