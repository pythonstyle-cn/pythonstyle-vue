# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pythonstyle.libs.result import Result
from pythonstyle.common import utils
from pythonstyle.modules.system.entity.role import RoleEntity
from pythonstyle.modules.system.entity.role_menu import RoleMenuEntity
from pythonstyle.config.log_config import Log

class role(Result):

    def role_list(self):
        '''
        描述：获取角色分页列表
        '''
        params = utils.getRequestJson()
        # 获取角色列表
        roleList = RoleEntity.get_role_list(params)
        roleCount = RoleEntity.get_count()
        totalPage = utils.getCeil(roleCount / int(params['pageSize']))
        data = {
            'list': roleList,
            'total': roleCount,
            'pageNum': int(params['pageNum']),
            'pageSize': int(params['pageSize']),
            'totalPage': totalPage
        }
        return Result.success(msg='操作成功', data=data)

    def public_role_select_list(self):
        '''
        描述：获取角色列表
        '''
        roleList = RoleEntity.get_role_all_list()
        return Result.success(msg='操作成功', data=roleList)

    def public_get_info(self):
        role_id = utils.getRequest('role_id')
        info_data = RoleEntity.get_roleinfo_by_id(role_id)
        menu_ids = self.get_menu_roleid(role_id)
        data = {
            'role_info':info_data,
            'menu_ids':menu_ids,
        }
        return Result.success(msg='操作成功', data=data)

    @Log
    def role_add(self):
        params = utils.postRequestJson()
        params = utils.dictNullToempty(params)

        # 用户拥有的菜单权限
        menu_ids = params.pop('menu_ids')
        result = RoleMenuEntity.add_data(params, menu_ids)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    @Log
    def role_update(self):
        params = utils.postRequestJson()
        if params['role_id'] == None:
            return Result.error(code=201, msg='修改失败，缺少主键参数！')
        params['update_time'] = utils.formatDate()
        # 用户拥有的菜单权限
        try:
            menu_ids = params.pop('menu_ids')
            create_time = params.pop('create_time')
        except Exception as e:
            return Result.error(code=202, msg='请选择角色权限')
        #将字典里面为Null的转换成空字符串
        params = utils.dictNullToempty(params)

        result = RoleMenuEntity.edit_data(params, menu_ids)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    def update_status(self):
        params = utils.postRequestJson()
        param = {'role_id':params['role_id'],'status':params['status']}
        result = RoleEntity.edit_data(param)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')
    def update_listorder(self):
        params = utils.postRequestJson()
        param = {'role_id':params['role_id'],'listorder':params['listorder']}
        result = RoleEntity.edit_data(param)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    @Log
    def role_delete(self):
        role_id = utils.getRequest('role_id')
        if int(role_id) == 1:
            return Result.error(code=201, msg='操作失败,原始超级管理员不能删除！')
        rst = RoleEntity.delete_by_id(int(role_id))
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    @Log
    def role_mult_delete(self):
        params = utils.postRequestJson()
        role_ids = params['role_ids']
        if 1 in role_ids:
            return Result.error(code=201, msg='操作失败,原始超级管理员不能删除！')

        rst = RoleEntity.delete_by_ids(role_ids)
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    def get_menu_roleid(self, role_id):
        rst = RoleEntity.get_role_menu_by_roleid(role_id)
        return rst