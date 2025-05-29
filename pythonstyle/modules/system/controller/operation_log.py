# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pythonstyle.libs.result import Result
from pythonstyle.common import utils
from pythonstyle.modules.system.entity.operation_log import OperationLogEntity

class operation_log(Result):

    def get_list(self):
        '''
        描述：获取角色分页列表
        '''
        params = utils.getRequestJson()
        # 获取角色列表
        dataList = OperationLogEntity.get_data_list(params)
        dataCount = OperationLogEntity.get_count(params)
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
        post_id = utils.getRequest('id')
        dataInfo = OperationLogEntity.get_datainfo_by_id(post_id)
        return Result.success(msg='操作成功', data=dataInfo)
