# -*- coding: UTF-8 -*-
import asyncio


# 函數前宣告async即為coroutine
async def myfunc():
    await asyncio.sleep(1)
    print('hello')


if __name__ == '__main__':
    # myfunc() #RuntimeWarning: coroutine 'myfunc' was never awaited
    # coroutine必須用run執行，無法直接執行函數
    asyncio.run(myfunc())
