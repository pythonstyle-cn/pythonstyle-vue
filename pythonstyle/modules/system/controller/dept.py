# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pythonstyle.libs.result import Result
from pythonstyle.common import utils
from pythonstyle.config.log_config import Log
from pythonstyle.modules.system.entity.dept import DeptEntity

class dept(Result):

    def get_list(self):
        '''
        描述：获取角色分页列表
        '''
        param = {}
        dataList = DeptEntity.get_data_list()
        dept_list_data = self.build_all_dept_tree(dataList)
        return Result.success(msg='操作成功', data=dept_list_data)

    def public_get_info(self):
        id = utils.getRequest('dept_id')
        dataInfo = DeptEntity.get_datainfo_by_id(id)
        return Result.success(msg='操作成功', data=dataInfo)

    @Log
    def add(self):
        params = utils.postRequestJson()
        params = utils.dictNullToempty(params)
        #现根据parent_id 获取上级部门的path 如果为0 则为0
        if params['parent_id'] != 0:
            dataInfo = DeptEntity.get_datainfo_by_id(params['parent_id'])
            if dataInfo:
                params['path'] = str(dataInfo['path'])+','+str(dataInfo['dept_id'])
        else:
            params['path'] = 0
        result = DeptEntity.add_data(params)
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

        result = DeptEntity.edit_data(params)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    def updateStatus(self):
        params = utils.postRequestJson()
        param = {'dept_id':params['dept_id'],'status':params['status']}
        result = DeptEntity.edit_data(param)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    @Log
    def delete(self):
        id = utils.getRequest('dept_id')
        countChildren = self.is_has_children(id)
        if countChildren:
            return Result.error(code=201, msg='操作失败,有子部门，不允许删除！')
        rst = DeptEntity.delete_by_id(id)
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    @Log
    def mult_delete(self):
        params = utils.postRequestJson()
        ids = params['dept_ids']
        rst = DeptEntity.delete_by_ids(ids)
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    def build_all_dept_tree(self,data_list, parent_id=0):
        data_tree = []
        for item in data_list:
            if item['parent_id'] == parent_id:
                children = self.build_all_dept_tree(data_list, item['dept_id'])
                if children:
                    item['children'] = children
                data_tree.append(item)
        return data_tree

    def is_has_children(self, id):
        rst = DeptEntity.has_children(id)
        if rst > 0:
            return True
        else:
            return False