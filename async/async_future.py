import asyncio


async def do_async_job(fut):
    await asyncio.sleep(2)
    fut.set_result('Hello future')


async def main():
    loop = asyncio.get_running_loop()

    future = loop.create_future()
    loop.create_task(do_async_job(future))

    # Wait until future has a result
    await future

    print(future.result())


if __name__ == '__main__':
    asyncio.run(main())
