# -*- coding: utf-8 -*-
'''
    描述：
    作者: chinacsj@139.com
    日期: 2024-02-29
'''
from pony.orm import *
from pythonstyle.config.db_config import create_db
db = create_db('mysql')
# 导入实体类
from pythonstyle.modules.system.entity.menu import MenuEntity
from pythonstyle.modules.system.entity.user import UserEntity
from pythonstyle.modules.system.entity.user_role import UserRoleEntity
from pythonstyle.modules.system.entity.user_post import UserPostEntity
from pythonstyle.modules.system.entity.role import RoleEntity
from pythonstyle.modules.system.entity.role_menu import RoleMenuEntity
from pythonstyle.modules.system.entity.post import PostEntity
from pythonstyle.modules.system.entity.dept import DeptEntity
from pythonstyle.modules.system.entity.operation_log import OperationLogEntity
from pythonstyle.modules.system.entity.login_log import LoginLogEntity

#set_sql_debug(True)
db.generate_mapping(create_tables=True)
