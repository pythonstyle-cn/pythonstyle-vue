# -*- coding: utf-8 -*-
'''
    描述：异步日志类
    作者: chinacsj@139.com
    日期: 2024-07-04
'''
import asyncio
from pythonstyle.libs.async_service_base import AsyncServiceBase
from pythonstyle.modules.system.entity.login_log import LoginLogEntity
from pythonstyle.modules.system.entity.operation_log import OperationLogEntity

class AsyncLogService(AsyncServiceBase):

    # 记录登录日志
    def add_login_log(self, param):
        self.run_coroutine_threadsafe(self._add_log_async(param))

    # 记录操作日志
    def add_action_log(self, param):
        self.run_coroutine_threadsafe(self._add_action_async(param))


    # 异步记录登录日志
    async def _add_log_async(self, param):
        try:
            result = await asyncio.get_running_loop().run_in_executor(self._executor, LoginLogEntity.add_data, param)
            return result
        except Exception as e:
            print(f"记录登录日志时发生错误: {e}")

    # 异步记录操作日志
    async def _add_action_async(self, param):
        try:
            result = await asyncio.get_running_loop().run_in_executor(self._executor, OperationLogEntity.add_data, param)
            return result
        except Exception as e:
            print(f"记录操作日志时发生错误: {e}")