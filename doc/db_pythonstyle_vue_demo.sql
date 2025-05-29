/*
Navicat MySQL Data Transfer

Source Server         : 47.97.222.35-python
Source Server Version : 80040
Source Host           : 47.97.222.35:3306
Source Database       : db_pythonstyle_vue_demo

Target Server Type    : MYSQL
Target Server Version : 80040
File Encoding         : 65001

Date: 2024-12-11 17:04:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sys_dept
-- ----------------------------
DROP TABLE IF EXISTS `sys_dept`;
CREATE TABLE `sys_dept` (
  `dept_id` bigint NOT NULL AUTO_INCREMENT COMMENT '部门id',
  `parent_id` bigint DEFAULT '0' COMMENT '父部门id',
  `path` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '' COMMENT '祖级列表',
  `dept_name` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '' COMMENT '部门名称',
  `listorder` int DEFAULT '0' COMMENT '显示顺序',
  `leader` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT '负责人',
  `phone` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT '联系电话',
  `email` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT '邮箱',
  `status` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '0' COMMENT '部门状态（0正常 1停用）',
  `del_flag` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '0' COMMENT '删除标志（0代表存在 2代表删除）',
  `create_user` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb3 COMMENT='部门表';

-- ----------------------------
-- Records of sys_dept
-- ----------------------------
INSERT INTO `sys_dept` VALUES ('100', '0', '0', '贵阳thinkstyle科技', '0', 'thinkstyle', '15888888888', 'thinkstyle@139.com', '0', '0', 'admin', '2023-08-06 19:26:25', '', '2024-04-28 11:44:50');
INSERT INTO `sys_dept` VALUES ('101', '100', '0,100', '深圳分公司', '1', 'thinkstyle', '15888888888', 'thinkstyle@139.com', '0', '0', 'admin', '2023-08-06 19:26:25', '', '2024-04-28 11:44:50');
INSERT INTO `sys_dept` VALUES ('102', '100', '0,100', '长沙分公司', '2', 'thinkpython', '15888888888', 'ry@qq.com', '0', '1', 'admin', '2023-08-06 19:26:25', '', null);
INSERT INTO `sys_dept` VALUES ('103', '101', '0,100,101', '研发部门', '1', 'thinkpython', '15888888888', 'thinkstyle@139.com', '0', '0', 'admin', '2023-08-06 19:26:25', '', '2024-04-28 11:44:50');
INSERT INTO `sys_dept` VALUES ('104', '101', '0,100,101', '市场部门', '2', 'thinkpython', '15888888888', 'thinkstyle@139.com', '1', '0', 'admin', '2023-08-06 19:26:25', '', '2024-04-28 11:44:50');
INSERT INTO `sys_dept` VALUES ('111', '0', '0', '感定将积组', '72', 'ali', '18161151172', 'k.whwzhz@qq.com', '0', '1', '', '2024-04-11 14:02:42', '', null);
INSERT INTO `sys_dept` VALUES ('112', '0', '0', '几信么物在', '96', 'ad', '13294629581', 'b.ppkvegb@qq.com', '1', '1', '', '2024-04-11 14:02:42', '', null);
INSERT INTO `sys_dept` VALUES ('113', '103', '0,100,101,104', '测试部门', '96', 'ad', '13294629581', 'thinkstyle@139.com', '0', '0', '', '2024-04-11 14:09:11', '', '2024-12-02 06:02:35');
INSERT INTO `sys_dept` VALUES ('114', '111', '0,111', '几信么物在', '96', 'ad', '13294629581', 'b.ppkvegb@qq.com', '0', '1', '', '2024-04-11 14:09:11', '', null);
INSERT INTO `sys_dept` VALUES ('115', '114', '0,111,114', '几信么物在', '96', 'ad', '13294629581', 'b.ppkvegb@qq.com', '0', '0', '', '2024-04-11 14:09:11', '', null);
INSERT INTO `sys_dept` VALUES ('116', '0', '0', 'test', '1', 'tset', '15190909090', '1@qq.com', '0', '1', '', '2024-04-19 00:33:43', '', null);
INSERT INTO `sys_dept` VALUES ('117', '0', '0', 'test', '1', 'tset', '15190909090', '1@qq.com', '0', '1', '', '2024-04-19 00:33:43', '', null);
INSERT INTO `sys_dept` VALUES ('118', '0', '0', 'test', '1', 'tset', '15190909090', '1@qq.com', '0', '1', '', '2024-04-19 00:33:43', '', null);
INSERT INTO `sys_dept` VALUES ('119', '0', '0', 'test', '1', 'test', '15180809092', '1@qq.com', '0', '1', '', '2024-04-19 00:33:43', '', null);
INSERT INTO `sys_dept` VALUES ('120', '115', '0,111,114,115', 'tst', '1', 'test', '16189890909', null, '0', '1', '', '2024-04-19 00:33:43', '', null);
INSERT INTO `sys_dept` VALUES ('121', '103', '0,100,101,103', '灌灌灌灌灌', '1', '方法', null, null, '0', '1', '', '2024-04-21 06:02:00', '', null);
INSERT INTO `sys_dept` VALUES ('122', '101', '0,100,101,103', '通天塔', '1', '', '', '', '0', '1', '', '2024-04-21 06:02:00', '', '2024-04-21 06:02:00');
INSERT INTO `sys_dept` VALUES ('123', '0', '0', 'trstttt', '1', 'testst', null, null, '0', '1', '', '2024-04-30 11:40:18', '', null);
INSERT INTO `sys_dept` VALUES ('124', '113', '0,100,101,104,113', 'test', '1', 'terst', 'test', 'test', '0', '1', '', '2024-05-07 10:20:55', '', null);

-- ----------------------------
-- Table structure for sys_login_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_login_log`;
CREATE TABLE `sys_login_log` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '登录账号',
  `ip_address` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `login_location` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '登录地址',
  `browser` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '设备浏览器',
  `os` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '设备系统',
  `status` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '登录状态（0成功 1失败）',
  `return_code` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '返回状态码',
  `create_time` datetime DEFAULT NULL COMMENT '登录时间',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of sys_login_log
-- ----------------------------
INSERT INTO `sys_login_log` VALUES ('94', 'admin', '111.121.75.3', '', '\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"', '\"Windows\"', '0', '200', '2024-12-02 06:15:11');
INSERT INTO `sys_login_log` VALUES ('93', 'admin', '1.204.65.228', '', '\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"', '\"Windows\"', '0', '200', '2024-12-02 06:15:11');
INSERT INTO `sys_login_log` VALUES ('92', 'admin', '1.204.65.228', '', '\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"', '\"Windows\"', '1', '1002', '2024-12-02 06:15:11');
INSERT INTO `sys_login_log` VALUES ('91', 'admin', '117.189.8.131', '', '\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"', '\"Windows\"', '0', '200', '2024-12-02 06:15:11');

-- ----------------------------
-- Table structure for sys_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_menu`;
CREATE TABLE `sys_menu` (
  `menu_id` bigint NOT NULL AUTO_INCREMENT COMMENT '菜单ID',
  `menu_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '菜单名称',
  `parent_id` bigint DEFAULT '0' COMMENT '父菜单ID',
  `listorder` int DEFAULT '0' COMMENT '显示顺序',
  `path` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '路由地址',
  `component` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '组件路径',
  `query` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '路由参数',
  `is_link` int DEFAULT '0' COMMENT '是否为外链（1是 0否）',
  `is_cache` int DEFAULT '0' COMMENT '是否缓存（1缓存 0不缓存）',
  `menu_type` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '菜单类型（M目录 C菜单 F按钮）',
  `visible` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '菜单状态（0显示 1隐藏）',
  `status` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '菜单状态（0正常 1停用）',
  `perms` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '权限标识',
  `icon` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '#' COMMENT '菜单图标',
  `create_user` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `remark` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '备注',
  PRIMARY KEY (`menu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1067 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='菜单权限表';

-- ----------------------------
-- Records of sys_menu
-- ----------------------------
INSERT INTO `sys_menu` VALUES ('1', '系统管理', '0', '1', 'location', null, '', '0', '0', 'M', '0', '0', '', 'menu', 'admin', '2023-01-05 15:51:47', '', null, '系统管理目录');
INSERT INTO `sys_menu` VALUES ('100', '用户管理', '1', '1', 'user', 'system/user/index', '', '0', '0', 'C', '0', '0', 'system:user:get_list', 'user', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '用户管理菜单');
INSERT INTO `sys_menu` VALUES ('101', '角色管理', '1', '2', 'role', 'system/role/index', '', '0', '0', 'C', '0', '0', 'system:role:role_list', 'peoples', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '角色管理菜单');
INSERT INTO `sys_menu` VALUES ('102', '菜单管理', '1', '3', 'menu', 'system/menu/index', '', '0', '0', 'C', '0', '0', 'system:menu:menu_list', 'tree-table', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '菜单管理菜单');
INSERT INTO `sys_menu` VALUES ('103', '部门管理', '1', '4', 'dept', 'system/dept/index', '', '0', '0', 'C', '0', '0', 'system:dept:get_list', 'tree', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '部门管理菜单');
INSERT INTO `sys_menu` VALUES ('104', '岗位管理', '1', '5', 'post', 'system/post/index', '', '0', '0', 'C', '0', '0', 'system:post:get_list', 'post', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '岗位管理菜单');
INSERT INTO `sys_menu` VALUES ('108', '日志管理', '1', '9', 'log', '', '', '0', '0', 'M', '0', '0', '', 'log', 'admin', '2023-01-05 15:51:47', '', null, '日志管理菜单');
INSERT INTO `sys_menu` VALUES ('500', '操作日志', '108', '1', 'operlog', 'monitor/operationlog/index', '', '0', '0', 'C', '0', '0', 'system:operlog:get_list', 'form', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '操作日志菜单');
INSERT INTO `sys_menu` VALUES ('501', '登录日志', '108', '2', 'logininfor', 'monitor/logininfo/index', '', '0', '0', 'C', '0', '0', 'system:login_log:get_list', 'logininfor', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '登录日志菜单');
INSERT INTO `sys_menu` VALUES ('1000', '用户详情', '100', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:admin:get_userinfo', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1001', '用户新增', '100', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:user:add', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1002', '用户修改', '100', '3', '', '', '', '0', '0', 'F', '0', '0', 'system:user:update', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 17:10:14', '');
INSERT INTO `sys_menu` VALUES ('1003', '用户删除', '100', '4', '', '', '', '0', '0', 'F', '0', '0', 'system:user:user_delete', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 17:10:14', '');
INSERT INTO `sys_menu` VALUES ('1004', '用户导出', '100', '5', '', '', '', '0', '0', 'F', '0', '0', 'system:user:export', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1005', '状态更改', '100', '6', '', '', '', '0', '0', 'F', '0', '0', 'system:user:updateStatus', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1006', '重置密码', '100', '7', '', '', '', '0', '0', 'F', '0', '0', 'system:user:resetPwd', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1007', '角色列表', '101', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:role:role_list', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1008', '角色新增', '101', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:role:role_add', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1009', '角色修改', '101', '3', '', '', '', '0', '0', 'F', '0', '0', 'system:role:role_update', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1010', '角色删除', '101', '4', '', '', '', '0', '0', 'F', '0', '0', 'system:role:role_delete', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1011', '角色导出', '101', '5', '', '', '', '0', '0', 'F', '0', '0', 'system:role:export', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1012', '菜单列表', '102', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:menu:menu_list', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1013', '菜单新增', '102', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:menu:menu_add', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1014', '菜单修改', '102', '3', '', '', '', '0', '0', 'F', '0', '0', 'system:menu:update', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1015', '菜单删除', '102', '4', '', '', '', '0', '0', 'F', '0', '0', 'system:menu:delete', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1016', '部门列表', '103', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:dept:get_list', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1017', '部门新增', '103', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:dept:add', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1018', '部门修改', '103', '3', '', '', '', '0', '0', 'F', '0', '0', 'system:dept:update', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1019', '部门删除', '103', '4', '', '', '', '0', '0', 'F', '0', '0', 'system:dept:delete', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1020', '岗位列表', '104', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:post:get_list', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1021', '岗位新增', '104', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:post:add', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1022', '岗位修改', '104', '3', '', '', '', '0', '0', 'F', '0', '0', 'system:post:update', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1023', '岗位删除', '104', '4', '', '', '', '0', '0', 'F', '0', '0', 'system:post:delete', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-06 18:23:43', '');
INSERT INTO `sys_menu` VALUES ('1024', '己公老商气', '18', '47', '#', 'in adipisicing', 'ullamco ipsum', '4', '55', 'F', '', '', 'nostrud velit labore', 'http://dummyimage.com/100x100', 'admin', '2023-01-05 15:51:47', 'ex eu sint', '2024-04-12 15:59:05', 'anim esse deserunt voluptate');
INSERT INTO `sys_menu` VALUES ('1025', '字典查询', '105', '1', '#', '', '', '0', '0', 'F', '0', '0', 'system:dict:query', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1026', '字典新增', '105', '2', '#', '', '', '0', '0', 'F', '0', '0', 'system:dict:add', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1027', '字典修改', '105', '3', '#', '', '', '0', '0', 'F', '0', '0', 'system:dict:edit', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1028', '字典删除', '105', '4', '#', '', '', '0', '0', 'F', '0', '0', 'system:dict:remove', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1029', '字典导出', '105', '5', '#', '', '', '0', '0', 'F', '0', '0', 'system:dict:export', '#', 'admin', '2023-01-05 15:51:47', '', null, '');
INSERT INTO `sys_menu` VALUES ('1039', '操作查询', '500', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:operation_log:get_list', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '');
INSERT INTO `sys_menu` VALUES ('1040', '操作删除', '500', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:operation_log:remove', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '');
INSERT INTO `sys_menu` VALUES ('1041', '日志导出', '500', '3', '', '', '', '0', '0', 'F', '0', '0', 'system:operation_log:export', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '');
INSERT INTO `sys_menu` VALUES ('1042', '登录查询', '501', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:login_log:get_list', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-28 11:40:35', '');
INSERT INTO `sys_menu` VALUES ('1043', '登录删除', '501', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:login_log:delete', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '');
INSERT INTO `sys_menu` VALUES ('1044', '日志导出', '501', '3', '', '', '', '0', '0', 'F', '0', '0', 'system:login_log:export', '#', 'admin', '2023-01-05 15:51:47', '', '2024-05-07 10:20:55', '');
INSERT INTO `sys_menu` VALUES ('1047', '用户列表', '100', '2', '', '', '', '0', '0', 'F', '0', '0', 'system:user:get_list', '#', '', '2024-05-06 18:23:43', '', '2024-12-02 05:59:56', '');
INSERT INTO `sys_menu` VALUES ('1048', '用户信息', '100', '1', '', '', '', '0', '0', 'F', '0', '0', 'system:user:public_get_info', '#', '', '2024-05-06 18:23:43', '', '2024-05-08 15:40:18', '');
INSERT INTO `sys_menu` VALUES ('1053', '角色状态', '101', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:role:update_status', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1054', '角色排序', '101', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:role:update_listorder', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1055', '批量删除', '101', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:role:role_mult_delete', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1056', '菜单详情', '102', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:menu:get_info', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1057', '菜单状态', '102', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:menu:updateStatus', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1059', '部门状态', '103', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:dept:updateStatus', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1060', '批量删除', '103', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:dept:mult_delete', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1062', '岗位详情', '104', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:post:get_info', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1063', '岗位状态', '104', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:post:updateStatus', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1064', '批量删除', '104', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:post:mult_delete', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1065', '日志详情', '500', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:operation_log:get_info', '#', '', '2024-05-06 18:23:43', '', null, '');
INSERT INTO `sys_menu` VALUES ('1066', '日志详情', '501', '1', '', null, null, '0', '0', 'F', '0', '0', 'system:login_log:get_list', '#', '', '2024-05-06 18:23:43', '', null, '');

-- ----------------------------
-- Table structure for sys_operation_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_operation_log`;
CREATE TABLE `sys_operation_log` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '日志主键',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '模块标题',
  `business_type` int DEFAULT '0' COMMENT '业务类型（0其它 1新增 2修改 3删除 4查看）',
  `method` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '方法名称',
  `request_method` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '请求方式',
  `op_type` int DEFAULT '0' COMMENT '操作类别（0其它 1后台用户 2手机端用户）',
  `op_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '操作人员',
  `dept_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '部门名称',
  `op_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '请求URL',
  `op_ip` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '主机地址',
  `op_location` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '操作地点',
  `op_param` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '请求参数',
  `json_result` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '返回参数',
  `status` int DEFAULT '0' COMMENT '操作状态（0正常 1异常）',
  `error_msg` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '错误消息',
  `create_time` datetime DEFAULT NULL COMMENT '操作时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='操作日志记录';

-- ----------------------------
-- Records of sys_operation_log
-- ----------------------------
INSERT INTO `sys_operation_log` VALUES ('78', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/menu/update', '172.16.15.200', '', '{\'menu_id\': 1047, \'menu_name\': \'用户列表\', \'parent_id\': 100, \'listorder\': 2, \'path\': \'\', \'component\': \'\', \'query\': \'\', \'is_link\': 0, \'is_cache\': 0, \'menu_type\': \'F\', \'visible\': \'0\', \'status\': \'0\', \'perms\': \'system:user:get_list\', \'icon\': \'#\', \'create_user\': \'\', \'create_time\': \'2024-05-06 18:23:43\', \'update_user\': \'\', \'update_time\': \'2024-12-02 05:59:56\', \'remark\': \'\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 05:59:56');
INSERT INTO `sys_operation_log` VALUES ('79', 'system模块', '3', 'delete', 'GET', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/dept/delete?dept_id=124', '172.16.15.200', '', '{\'dept_id\': \'124\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('80', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/dept/update', '172.16.15.200', '', '{\'dept_id\': 113, \'parent_id\': 103, \'path\': \'0,100,101,104\', \'dept_name\': \'测试部门\', \'leader\': \'ad\', \'phone\': \'13294629581\', \'email\': \'thinkstyle@139.com\', \'status\': \'0\', \'del_flag\': \'0\', \'listorder\': 96, \'create_user\': \'\', \'create_time\': \'2024-04-11 14:09:11\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:02:35\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('81', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/dept/update', '172.16.15.200', '', '{\'dept_id\': 113, \'parent_id\': 103, \'path\': \'0,100,101,104\', \'dept_name\': \'测试部门\', \'leader\': \'ad\', \'phone\': \'13294629581\', \'email\': \'thinkstyle@139.com\', \'status\': \'0\', \'del_flag\': \'0\', \'listorder\': 96, \'create_user\': \'\', \'create_time\': \'2024-04-11 14:09:11\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:02:35\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('82', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/dept/update', '172.16.15.200', '', '{\'dept_id\': 113, \'parent_id\': 103, \'path\': \'0,100,101,104\', \'dept_name\': \'测试部门\', \'leader\': \'ad\', \'phone\': \'13294629581\', \'email\': \'thinkstyle@139.com\', \'status\': \'0\', \'del_flag\': \'0\', \'listorder\': 96, \'create_user\': \'\', \'create_time\': \'2024-04-11 14:09:11\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:02:35\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('83', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/dept/update', '172.16.15.200', '', '{\'dept_id\': 113, \'parent_id\': 103, \'path\': \'0,100,101,104\', \'dept_name\': \'测试部门\', \'leader\': \'ad\', \'phone\': \'13294629581\', \'email\': \'thinkstyle@139.com\', \'status\': \'0\', \'del_flag\': \'0\', \'listorder\': 96, \'create_user\': \'\', \'create_time\': \'2024-04-11 14:09:11\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:02:35\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('84', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/dept/update', '172.16.15.200', '', '{\'dept_id\': 113, \'parent_id\': 103, \'path\': \'0,100,101,104\', \'dept_name\': \'测试部门\', \'leader\': \'ad\', \'phone\': \'13294629581\', \'email\': \'thinkstyle@139.com\', \'status\': \'0\', \'del_flag\': \'0\', \'listorder\': 96, \'create_user\': \'\', \'create_time\': \'2024-04-11 14:09:11\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:02:35\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('85', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/dept/update', '172.16.15.200', '', '{\'dept_id\': 113, \'parent_id\': 103, \'path\': \'0,100,101,104\', \'dept_name\': \'测试部门\', \'leader\': \'ad\', \'phone\': \'13294629581\', \'email\': \'thinkstyle@139.com\', \'status\': \'0\', \'del_flag\': \'0\', \'listorder\': 96, \'create_user\': \'\', \'create_time\': \'2024-04-11 14:09:11\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:02:35\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('86', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/post/update', '172.16.15.200', '', '{\'post_id\': 13, \'post_code\': \'123\', \'post_name\': \'总经理\', \'listorder\': 3, \'status\': \'0\', \'create_user\': \'\', \'create_time\': \'2024-04-11 11:58:59\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:02:35\', \'remark\': \'测试添加123\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:02:35');
INSERT INTO `sys_operation_log` VALUES ('87', 'system模块', '2', 'update', 'POST', '1', 'admin', '贵阳thinkstyle科技', 'http://demo1.pythonstyle.cn/system/post/update', '117.189.8.131', '', '{\'post_id\': 13, \'post_code\': \'123\', \'post_name\': \'总经理\', \'listorder\': 3, \'status\': \'0\', \'create_user\': \'\', \'create_time\': \'2024-04-11 11:58:59\', \'update_user\': \'\', \'update_time\': \'2024-12-02 06:15:11\', \'remark\': \'测试修改\'}', '{\'code\': 200, \'msg\': \'操作成功\', \'data\': []}', '0', '', '2024-12-02 06:15:11');

-- ----------------------------
-- Table structure for sys_post
-- ----------------------------
DROP TABLE IF EXISTS `sys_post`;
CREATE TABLE `sys_post` (
  `post_id` bigint NOT NULL AUTO_INCREMENT COMMENT '岗位ID',
  `post_code` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '岗位编码',
  `post_name` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '岗位名称',
  `listorder` int NOT NULL DEFAULT '1' COMMENT '显示顺序',
  `status` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '0' COMMENT '状态（0正常 1停用）',
  `create_user` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(64) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `remark` varchar(500) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3 COMMENT='岗位信息表';

-- ----------------------------
-- Records of sys_post
-- ----------------------------
INSERT INTO `sys_post` VALUES ('1', 'ceo', '董事长', '7', '0', 'admin', '2023-08-06 19:26:25', '', '2024-05-07 10:20:55', '');
INSERT INTO `sys_post` VALUES ('3', 'hr', '人力资源', '3', '0', 'admin', '2023-08-06 19:26:25', '', null, '');
INSERT INTO `sys_post` VALUES ('4', 'user', '普通员工', '5', '0', 'admin', '2023-08-06 19:26:25', '', '2024-05-07 10:20:55', '');
INSERT INTO `sys_post` VALUES ('13', '123', '总经理', '3', '0', '', '2024-04-11 11:58:59', '', '2024-12-02 06:15:11', '测试修改');

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role` (
  `role_id` bigint NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `role_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色名称',
  `listorder` int DEFAULT '1' COMMENT '显示顺序',
  `data_scope` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '1' COMMENT '数据范围（1：全部数据权限 2：自定数据权限 3：本部门数据权限 4：本部门及以下数据权限）',
  `menu_check_strictly` tinyint(1) DEFAULT '1' COMMENT '菜单树选择项是否关联显示',
  `dept_check_strictly` tinyint(1) DEFAULT '1' COMMENT '部门树选择项是否关联显示',
  `status` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '角色状态（0正常 1停用）',
  `del_flag` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '删除标志（0代表存在 1代表删除）',
  `create_user` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL,
  `update_user` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `remark` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='角色信息表';

-- ----------------------------
-- Records of sys_role
-- ----------------------------
INSERT INTO `sys_role` VALUES ('1', '超级管理员', '2', '1', '1', '1', '0', '0', 'admin', null, '', '2024-04-04 08:53:19', '超级管理员');
INSERT INTO `sys_role` VALUES ('2', '普通角色', '-1', '2', '1', '1', '0', '0', 'admin', null, '', '2024-05-08 15:59:29', '普通角色');
INSERT INTO `sys_role` VALUES ('3', '发布角色', '1', '1', '1', '1', '0', '0', 'admin', null, '', '2024-12-02 05:58:10', '测试');
INSERT INTO `sys_role` VALUES ('4', 'test', '0', '1', '1', '1', '1', '1', '', null, '', '2024-04-04 08:53:19', '');
INSERT INTO `sys_role` VALUES ('5', 'test', '1', '1', '1', '1', '1', '1', '', null, '', '2024-04-15 17:31:10', null);
INSERT INTO `sys_role` VALUES ('6', '所发生的', '1', '1', '1', '1', '0', '1', '', null, '', null, null);
INSERT INTO `sys_role` VALUES ('7', 'test3333', '2', '1', '1', '1', '0', '1', '', '2024-04-22 04:10:59', '', '2024-04-22 05:40:24', '');
INSERT INTO `sys_role` VALUES ('8', '士大夫', '2', '1', '1', '1', '0', '1', '', '2024-04-25 15:59:00', '', '2024-04-30 11:40:18', '');

-- ----------------------------
-- Table structure for sys_role_dept
-- ----------------------------
DROP TABLE IF EXISTS `sys_role_dept`;
CREATE TABLE `sys_role_dept` (
  `role_id` bigint NOT NULL COMMENT '角色ID',
  `dept_id` bigint NOT NULL COMMENT '部门ID',
  PRIMARY KEY (`role_id`,`dept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='角色和部门关联表';

-- ----------------------------
-- Records of sys_role_dept
-- ----------------------------
INSERT INTO `sys_role_dept` VALUES ('2', '100');
INSERT INTO `sys_role_dept` VALUES ('2', '101');
INSERT INTO `sys_role_dept` VALUES ('2', '105');

-- ----------------------------
-- Table structure for sys_role_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_role_menu`;
CREATE TABLE `sys_role_menu` (
  `role_id` bigint NOT NULL COMMENT '角色ID',
  `menu_id` bigint NOT NULL COMMENT '菜单ID',
  PRIMARY KEY (`role_id`,`menu_id`),
  KEY `idx_sys_role_menu__menu_id` (`menu_id`) USING BTREE,
  CONSTRAINT `fk_sys_role_menu__menu_id` FOREIGN KEY (`menu_id`) REFERENCES `sys_menu` (`menu_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_sys_role_menu__role_id` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`role_id`) ON DELETE CASCADE,
  CONSTRAINT `sys_role_menu_ibfk_1` FOREIGN KEY (`menu_id`) REFERENCES `sys_menu` (`menu_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_role_menu_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`role_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_role_menu_ibfk_3` FOREIGN KEY (`menu_id`) REFERENCES `sys_menu` (`menu_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_role_menu_ibfk_4` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`role_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='角色和菜单关联表';

-- ----------------------------
-- Records of sys_role_menu
-- ----------------------------
INSERT INTO `sys_role_menu` VALUES ('2', '1');
INSERT INTO `sys_role_menu` VALUES ('6', '1');
INSERT INTO `sys_role_menu` VALUES ('7', '1');
INSERT INTO `sys_role_menu` VALUES ('8', '1');
INSERT INTO `sys_role_menu` VALUES ('2', '100');
INSERT INTO `sys_role_menu` VALUES ('6', '100');
INSERT INTO `sys_role_menu` VALUES ('7', '100');
INSERT INTO `sys_role_menu` VALUES ('2', '101');
INSERT INTO `sys_role_menu` VALUES ('6', '101');
INSERT INTO `sys_role_menu` VALUES ('7', '101');
INSERT INTO `sys_role_menu` VALUES ('2', '102');
INSERT INTO `sys_role_menu` VALUES ('6', '102');
INSERT INTO `sys_role_menu` VALUES ('8', '102');
INSERT INTO `sys_role_menu` VALUES ('2', '103');
INSERT INTO `sys_role_menu` VALUES ('6', '103');
INSERT INTO `sys_role_menu` VALUES ('8', '103');
INSERT INTO `sys_role_menu` VALUES ('2', '104');
INSERT INTO `sys_role_menu` VALUES ('5', '104');
INSERT INTO `sys_role_menu` VALUES ('6', '104');
INSERT INTO `sys_role_menu` VALUES ('8', '104');
INSERT INTO `sys_role_menu` VALUES ('2', '108');
INSERT INTO `sys_role_menu` VALUES ('6', '108');
INSERT INTO `sys_role_menu` VALUES ('8', '108');
INSERT INTO `sys_role_menu` VALUES ('2', '500');
INSERT INTO `sys_role_menu` VALUES ('6', '500');
INSERT INTO `sys_role_menu` VALUES ('8', '500');
INSERT INTO `sys_role_menu` VALUES ('2', '501');
INSERT INTO `sys_role_menu` VALUES ('6', '501');
INSERT INTO `sys_role_menu` VALUES ('2', '1000');
INSERT INTO `sys_role_menu` VALUES ('6', '1000');
INSERT INTO `sys_role_menu` VALUES ('7', '1000');
INSERT INTO `sys_role_menu` VALUES ('2', '1001');
INSERT INTO `sys_role_menu` VALUES ('6', '1001');
INSERT INTO `sys_role_menu` VALUES ('7', '1001');
INSERT INTO `sys_role_menu` VALUES ('2', '1002');
INSERT INTO `sys_role_menu` VALUES ('6', '1002');
INSERT INTO `sys_role_menu` VALUES ('7', '1002');
INSERT INTO `sys_role_menu` VALUES ('2', '1003');
INSERT INTO `sys_role_menu` VALUES ('6', '1003');
INSERT INTO `sys_role_menu` VALUES ('7', '1003');
INSERT INTO `sys_role_menu` VALUES ('2', '1004');
INSERT INTO `sys_role_menu` VALUES ('6', '1004');
INSERT INTO `sys_role_menu` VALUES ('7', '1004');
INSERT INTO `sys_role_menu` VALUES ('2', '1005');
INSERT INTO `sys_role_menu` VALUES ('6', '1005');
INSERT INTO `sys_role_menu` VALUES ('7', '1005');
INSERT INTO `sys_role_menu` VALUES ('2', '1006');
INSERT INTO `sys_role_menu` VALUES ('6', '1006');
INSERT INTO `sys_role_menu` VALUES ('7', '1006');
INSERT INTO `sys_role_menu` VALUES ('2', '1007');
INSERT INTO `sys_role_menu` VALUES ('6', '1007');
INSERT INTO `sys_role_menu` VALUES ('7', '1007');
INSERT INTO `sys_role_menu` VALUES ('2', '1008');
INSERT INTO `sys_role_menu` VALUES ('6', '1008');
INSERT INTO `sys_role_menu` VALUES ('7', '1008');
INSERT INTO `sys_role_menu` VALUES ('2', '1009');
INSERT INTO `sys_role_menu` VALUES ('6', '1009');
INSERT INTO `sys_role_menu` VALUES ('7', '1009');
INSERT INTO `sys_role_menu` VALUES ('2', '1010');
INSERT INTO `sys_role_menu` VALUES ('6', '1010');
INSERT INTO `sys_role_menu` VALUES ('7', '1010');
INSERT INTO `sys_role_menu` VALUES ('6', '1011');
INSERT INTO `sys_role_menu` VALUES ('7', '1011');
INSERT INTO `sys_role_menu` VALUES ('2', '1012');
INSERT INTO `sys_role_menu` VALUES ('3', '1012');
INSERT INTO `sys_role_menu` VALUES ('6', '1012');
INSERT INTO `sys_role_menu` VALUES ('8', '1012');
INSERT INTO `sys_role_menu` VALUES ('6', '1013');
INSERT INTO `sys_role_menu` VALUES ('8', '1013');
INSERT INTO `sys_role_menu` VALUES ('6', '1014');
INSERT INTO `sys_role_menu` VALUES ('6', '1015');
INSERT INTO `sys_role_menu` VALUES ('8', '1015');
INSERT INTO `sys_role_menu` VALUES ('2', '1016');
INSERT INTO `sys_role_menu` VALUES ('3', '1016');
INSERT INTO `sys_role_menu` VALUES ('6', '1016');
INSERT INTO `sys_role_menu` VALUES ('2', '1017');
INSERT INTO `sys_role_menu` VALUES ('6', '1017');
INSERT INTO `sys_role_menu` VALUES ('8', '1017');
INSERT INTO `sys_role_menu` VALUES ('2', '1018');
INSERT INTO `sys_role_menu` VALUES ('6', '1018');
INSERT INTO `sys_role_menu` VALUES ('6', '1019');
INSERT INTO `sys_role_menu` VALUES ('3', '1020');
INSERT INTO `sys_role_menu` VALUES ('6', '1020');
INSERT INTO `sys_role_menu` VALUES ('8', '1020');
INSERT INTO `sys_role_menu` VALUES ('2', '1021');
INSERT INTO `sys_role_menu` VALUES ('6', '1021');
INSERT INTO `sys_role_menu` VALUES ('8', '1021');
INSERT INTO `sys_role_menu` VALUES ('6', '1022');
INSERT INTO `sys_role_menu` VALUES ('6', '1023');
INSERT INTO `sys_role_menu` VALUES ('8', '1023');
INSERT INTO `sys_role_menu` VALUES ('2', '1039');
INSERT INTO `sys_role_menu` VALUES ('6', '1039');
INSERT INTO `sys_role_menu` VALUES ('8', '1039');
INSERT INTO `sys_role_menu` VALUES ('2', '1040');
INSERT INTO `sys_role_menu` VALUES ('6', '1040');
INSERT INTO `sys_role_menu` VALUES ('8', '1040');
INSERT INTO `sys_role_menu` VALUES ('2', '1041');
INSERT INTO `sys_role_menu` VALUES ('6', '1041');
INSERT INTO `sys_role_menu` VALUES ('8', '1041');
INSERT INTO `sys_role_menu` VALUES ('2', '1042');
INSERT INTO `sys_role_menu` VALUES ('6', '1042');
INSERT INTO `sys_role_menu` VALUES ('2', '1043');
INSERT INTO `sys_role_menu` VALUES ('6', '1043');
INSERT INTO `sys_role_menu` VALUES ('2', '1044');
INSERT INTO `sys_role_menu` VALUES ('6', '1044');
INSERT INTO `sys_role_menu` VALUES ('2', '1047');
INSERT INTO `sys_role_menu` VALUES ('2', '1048');
INSERT INTO `sys_role_menu` VALUES ('2', '1065');
INSERT INTO `sys_role_menu` VALUES ('2', '1066');

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user` (
  `user_id` bigint NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `dept_id` bigint DEFAULT NULL COMMENT '部门ID',
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户账号',
  `nick_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户昵称',
  `user_type` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '用户类型',
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '用户邮箱',
  `phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '手机号码',
  `sex` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '用户性别（0男 1女 2未知）',
  `avatar` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '头像地址',
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '密码',
  `status` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '帐号状态（0正常 1停用）',
  `del_flag` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '0' COMMENT '删除标志（0代表存在 1代表删除）',
  `login_ip` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '最后登录IP',
  `login_date` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '最后登录时间',
  `create_user` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '创建者',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '更新者',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `remark` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户信息表';

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES ('1', '100', 'admin', 'PythonStyle', '0', '924965282@139.com', '15888888888', '1', '', 'cb9244cccf7a180e05254ee97a85b510', '0', '0', '', '', 'admin', null, '', null, '超级管理员');
INSERT INTO `sys_user` VALUES ('2', '100', 'test', 'test', '0', '', '13888888888', '0', '', 'cb9244cccf7a180e05254ee97a85b510', '0', '1', '', '', 'admin', null, '', '2024-07-08 18:07:51', '普通管理员ggggg');
INSERT INTO `sys_user` VALUES ('3', '100', 'root', 'root', '0', '', '13888888888', '0', '', 'cb9244cccf7a180e05254ee97a85b510', '0', '0', '', '', 'admin', null, '', null, '发布人员');
INSERT INTO `sys_user` VALUES ('4', '100', '胡娟', '贾秀兰', '2', 'i.klkae@qq.com', '18148340073', '0', '', 'b20034e4e06ceed6e1e5994bfb87c669', '0', '1', '', '', 'dolo', '2024-04-15 11:11:14', '', null, 'commodo aliqua');
INSERT INTO `sys_user` VALUES ('5', '100', '胡娟', '贾秀兰', '2', 'i.klkae@qq.com', '18148340073', '0', '', 'b20034e4e06ceed6e1e5994bfb87c669', '0', '1', '', '', 'dolo', '2024-04-15 11:14:23', '', null, 'commodo aliqua');
INSERT INTO `sys_user` VALUES ('8', '100', '胡娟', '贾秀兰', '2', 'i.klkae@qq.com', '18148340073', '0', '', 'b20034e4e06ceed6e1e5994bfb87c669', '0', '1', '', '', 'dolo', '2024-04-15 11:45:02', '', null, 'commodo aliqua');
INSERT INTO `sys_user` VALUES ('9', '100', '胡娟', '贾秀兰', '2', 'i.klkae@qq.com', '18148340073', '0', '', 'b20034e4e06ceed6e1e5994bfb87c669', '1', '1', '', '', 'dolo', '2024-04-15 11:48:21', '', null, 'commodo aliqua');
INSERT INTO `sys_user` VALUES ('16', '100', '唐静', '方秀英', '1', 'w.yns@qq.com', '18144397928', '0', '', 'dolor', '1', '1', '', '', 'Ut e', '2024-04-15 11:59:23', '', '2024-04-15 16:48:00', 'Excepteur laborum proident');
INSERT INTO `sys_user` VALUES ('17', '111', 'test', 'test', '0', '111', '111', '0', '', '22fd2246f08e8426875e0e4913c82c69', '0', '1', '', '', '', '2024-04-26 03:01:19', '', null, '11111');
INSERT INTO `sys_user` VALUES ('18', '111', 'test', 'test', '0', '111', '111', '0', '', '22fd2246f08e8426875e0e4913c82c69', '0', '1', '', '', '', '2024-04-26 03:12:51', '', '2024-04-28 06:21:02', '11111');
INSERT INTO `sys_user` VALUES ('19', null, 'test', 'test', '0', '11111', '11111', '0', '', '22fd2246f08e8426875e0e4913c82c69', '0', '1', '', '', '', '2024-04-26 03:21:44', '', null, '');
INSERT INTO `sys_user` VALUES ('20', '113', 'chinacsj', 'chinacsj', '0', '1@q.com', '15180809090', '0', '', 'cb9244cccf7a180e05254ee97a85b510', '0', '1', '', '', '', '2024-04-28 06:47:11', '', '2024-05-06 18:23:43', '普通角色');

-- ----------------------------
-- Table structure for sys_user_post
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_post`;
CREATE TABLE `sys_user_post` (
  `user_id` bigint NOT NULL COMMENT '用户ID',
  `post_id` bigint NOT NULL COMMENT '岗位ID',
  PRIMARY KEY (`user_id`,`post_id`),
  KEY `idx_sys_user_post__post_id` (`post_id`) USING BTREE,
  CONSTRAINT `fk_sys_user_post__post_id` FOREIGN KEY (`post_id`) REFERENCES `sys_post` (`post_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_sys_user_post__user_id` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `sys_user_post_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `sys_post` (`post_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_post_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`user_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_post_ibfk_3` FOREIGN KEY (`post_id`) REFERENCES `sys_post` (`post_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_post_ibfk_4` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`user_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户与岗位关联表';

-- ----------------------------
-- Records of sys_user_post
-- ----------------------------
INSERT INTO `sys_user_post` VALUES ('1', '1');
INSERT INTO `sys_user_post` VALUES ('2', '1');
INSERT INTO `sys_user_post` VALUES ('20', '1');
INSERT INTO `sys_user_post` VALUES ('18', '3');
INSERT INTO `sys_user_post` VALUES ('20', '3');
INSERT INTO `sys_user_post` VALUES ('2', '13');

-- ----------------------------
-- Table structure for sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_role`;
CREATE TABLE `sys_user_role` (
  `user_id` bigint NOT NULL COMMENT '用户ID',
  `role_id` bigint NOT NULL COMMENT '角色ID',
  PRIMARY KEY (`user_id`,`role_id`),
  KEY `idx_sys_user_role__role_id` (`role_id`) USING BTREE,
  CONSTRAINT `fk_sys_user_role__role_id` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`role_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_sys_user_role__user_id` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `sys_user_role_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`role_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_role_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`user_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_role_ibfk_3` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`role_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_role_ibfk_4` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`user_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户和角色关联表';

-- ----------------------------
-- Records of sys_user_role
-- ----------------------------
INSERT INTO `sys_user_role` VALUES ('1', '1');
INSERT INTO `sys_user_role` VALUES ('3', '1');
INSERT INTO `sys_user_role` VALUES ('2', '2');
INSERT INTO `sys_user_role` VALUES ('16', '2');
INSERT INTO `sys_user_role` VALUES ('20', '2');
INSERT INTO `sys_user_role` VALUES ('16', '3');
INSERT INTO `sys_user_role` VALUES ('17', '3');
INSERT INTO `sys_user_role` VALUES ('18', '3');
INSERT INTO `sys_user_role` VALUES ('17', '7');
INSERT INTO `sys_user_role` VALUES ('18', '7');
INSERT INTO `sys_user_role` VALUES ('17', '8');
INSERT INTO `sys_user_role` VALUES ('18', '8');
INSERT INTO `sys_user_role` VALUES ('19', '8');
