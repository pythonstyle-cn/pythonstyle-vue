# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-07-08
'''
import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading

class AsyncServiceBase:
    def __init__(self, max_workers= 10):
        self._executor = ThreadPoolExecutor(max_workers=max_workers)
        self._loop = asyncio.new_event_loop()
        self._loop_thread = threading.Thread(target=self._loop.run_forever, daemon=True)
        self._loop_thread.start()

    def run_coroutine_threadsafe(self, coro):
        return asyncio.run_coroutine_threadsafe(coro, self._loop)