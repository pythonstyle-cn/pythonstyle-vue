# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pythonstyle.libs.result import Result
from pythonstyle.common import utils
from pythonstyle.modules.system.entity.post import PostEntity
from pythonstyle.config.log_config import Log

class post(Result):

    def get_list(self):
        '''
        描述：获取角色分页列表
        '''
        params = utils.getRequestJson()
        # 获取角色列表
        dataList = PostEntity.get_data_list(params)
        dataCount = PostEntity.get_count()
        totalPage = utils.getCeil(dataCount / int(params['pageSize']))
        data = {
            'list': dataList,
            'total': dataCount,
            'pageNum': int(params['pageNum']),
            'pageSize': int(params['pageSize']),
            'totalPage': totalPage
        }
        return Result.success(msg='操作成功', data=data)

    def public_get_select_list(self):
        '''
        描述：获取角色列表
        '''
        postList = PostEntity.get_post_all_list()
        return Result.success(msg='操作成功', data=postList)

    def get_info(self):
        post_id = utils.getRequest('post_id')
        dataInfo = PostEntity.get_datainfo_by_id(post_id)
        return Result.success(msg='操作成功', data=dataInfo)
    @Log
    def add(self):
        params = utils.postRequestJson()
        params = utils.dictNullToempty(params)
        result = PostEntity.add_data(params)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    @Log
    def update(self):
        params = utils.postRequestJson()
        params['update_time'] = utils.formatDate()
        #将字典里面为Null的转换成空字符串
        params = utils.dictNullToempty(params)

        result = PostEntity.edit_data(params)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    @Log
    def updateStatus(self):
        params = utils.postRequestJson()
        param = {'post_id':params['post_id'],'status':params['status']}
        result = PostEntity.edit_data(param)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    @Log
    def delete(self):
        post_id = utils.getRequest('post_id')
        rst = PostEntity.delete_by_id(post_id)
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    @Log
    def mult_delete(self):
        params = utils.postRequestJson()
        post_ids = params['post_ids']
        rst = PostEntity.delete_by_ids(post_ids)
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')