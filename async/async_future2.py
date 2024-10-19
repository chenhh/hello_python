# -*- coding: UTF-8 -*-

import asyncio
def c() -> None:
    print("inner c")
    return 12

loop = asyncio.get_event_loop()
# None指的是預設的executor
future = loop.run_in_executor(None, c)
# inner c<Future pending cb=[_chain_future.<locals>._call_check_cancel() at /usr/lib64/python3.11/asyncio/futures.py:387]>
# 雖然c已經執行了，但是狀態還是 pending。
print(future)
# False, # 還沒有完成
print(future.done())




