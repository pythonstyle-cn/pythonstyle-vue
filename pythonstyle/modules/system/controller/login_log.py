# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pythonstyle.libs.result import Result
from pythonstyle.common import utils
from pythonstyle.modules.system.entity.login_log import LoginLogEntity

class login_log(Result):

    def get_list(self):
        '''
        描述：获取日志分页列表
        '''
        params = utils.getRequestJson()
        # 获取日志列表
        dataList = LoginLogEntity.get_data_list(params)
        dataCount = LoginLogEntity.get_count(params)
        totalPage = utils.getCeil(dataCount / int(params['pageSize']))
        data = {
            'list': dataList,
            'total': dataCount,
            'pageNum': int(params['pageNum']),
            'pageSize': int(params['pageSize']),
            'totalPage': totalPage
        }
        return Result.success(msg='操作成功', data=data)


    def get_info(self):
        id = utils.getRequest('id')
        dataInfo = LoginLogEntity.get_datainfo_by_id(id)
        return Result.success(msg='操作成功', data=dataInfo)
