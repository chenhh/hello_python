# -*- coding: UTF-8 -*-
import asyncio


async def cancel_me():
    print('cancel_me(): sleep')
    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')


async def main():
    print('main(): running')
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 5 second
    print('main(): sleep')
    await asyncio.sleep(5)

    print('main(): call cancel')
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print('main(): cancel_me is cancelled now')


if __name__ == '__main__':
    asyncio.run(main())

    # main(): running
    # main(): sleep
    # cancel_me(): sleep
    # main(): call
    # cancel
    # cancel_me(): cancel
    # sleep
    # cancel_me(): after
    # sleep
    # main(): cancel_me is cancelled
    # now
