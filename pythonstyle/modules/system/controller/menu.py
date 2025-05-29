# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pythonstyle.libs.result import Result
from pythonstyle.common import utils
from pythonstyle.config.log_config import Log
from pythonstyle.modules.system.entity.role import RoleEntity
from pythonstyle.modules.system.entity.menu import MenuEntity

class menu(Result):
    def menu_list(self):
        menu_list = MenuEntity.get_menu_list()
        menu_list_data = self.build_all_menu_tree(menu_list)
        return Result.success(msg='操作成功', data = menu_list_data)

    def public_menu_list(self):
        menu_list = MenuEntity.get_menu_list()
        menu_list_data = self.build_all_menu_tree(menu_list)
        return Result.success(msg='操作成功', data = menu_list_data)

    def get_info(self):
        id = utils.getRequest('menu_id')
        dataInfo = MenuEntity.get_datainfo_by_id(id)
        return Result.success(msg='操作成功', data=dataInfo)

    @Log
    def menu_add(self):
        params = utils.postRequestJson()
        params = utils.dictNullToempty(params)
        result = MenuEntity.add_data(params)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    @Log
    def update(self):
        params = utils.postRequestJson()
        params['update_time'] = utils.formatDate()
        # 将字典里面为Null的转换成空字符串
        params = utils.dictNullToempty(params)
        if params['menu_type'] == 'M':
            params['perms'] = ''
            params['query'] = ''
        if params['menu_type'] == 'F':
            params['path'] = ''
            params['query'] = ''
        result = MenuEntity.edit_data(params)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    def updateStatus(self):
        params = utils.postRequestJson()
        param = {'menu_id':params['menu_id'],'status':params['status']}
        result = MenuEntity.edit_data(param)
        if result:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201,msg='操作失败')

    @Log
    def delete(self):
        id = utils.getRequest('menu_id')
        not_delete = [1,100,101,102,103,104,108,500,501]
        if int(id) in (not_delete):
            return Result.error(code=202, msg='操作失败,演示系统不允许删除操作！')
        countChildren = self.is_has_children(id)
        if countChildren:
            return Result.error(code=201, msg='操作失败,有子菜单，不允许删除！')
        rst = MenuEntity.delete_by_id(id)
        if rst:
            return Result.success(msg='操作成功')
        else:
            return Result.error(code=201, msg='操作失败')

    def public_get_role_menu(self):
        data = utils.postRequestJson()
        user_roles = utils.filter_xss(data['role_ids'])

        menu_data = {}
        roleInfos_list = RoleEntity.get_rolelist_by_ids(user_roles)
        if len(roleInfos_list) > 0:
            menu_data['roles_info'] = roleInfos_list
        else:
            return Result.error(1007, msg='获取信息失败，请联系管理员！', data=[])
        role_menu_lists = MenuEntity.get_role_menu_by_roleids(user_roles)
        if len(role_menu_lists) > 0:
            menu_tree, menu_permission = self.build_menu_tree(role_menu_lists)
            menu_data['routers'] = menu_tree
            if 1 in user_roles:
                menu_data['permissions'] = ['*:*:*']
            else:
                menu_data['permissions'] = menu_permission
        else:
            return Result.error(1008, msg='获取失败，请分配菜单！', data=[])
        return Result.success(msg='获取成功！', data=menu_data)

    def build_all_menu_tree(self,menu_list, parent_id=0):
        menu_tree = []
        for menu in menu_list:
            if menu['parent_id'] == parent_id:
                children = self.build_all_menu_tree(menu_list, menu['menu_id'])
                if children:
                    menu['children'] = children
                menu_tree.append(menu)
        return menu_tree

    def build_menu_tree(self,menu_list, parent_id=0):
        menu_tree = []
        menu_permission = []
        for menu in menu_list:
            if menu['menu_type'] == 'F':
                menu_permission.append(menu['perms'])
                continue
            if menu['parent_id'] == parent_id:
                children_data, menu_permission_data = self.build_menu_tree(menu_list, menu['menu_id'])
                if children_data:
                    menu['children'] = children_data
                menu_tree.append(menu)
        return menu_tree,menu_permission

    def is_has_children(self, id):
        rst = MenuEntity.has_children(int(id))
        if rst > 0:
            return True
        else:
            return False