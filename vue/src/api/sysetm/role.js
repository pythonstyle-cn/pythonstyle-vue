import request from '@/utils/request'
// 获取用户列表
export const getRoleList = (params) => {
    return request({
        url: '/system/role/role_list',
        method: 'GET',
        params 
    })
}

// 获取用户列表
export const getRoleSelectList = () => {
    return request({
        url: '/system/role/public_role_select_list',
        method: 'GET'
    })
}

// 获取数据信息
export const getInfoData = (params) => {
    return request({
        url: '/system/role/public_get_info',
        method: 'GET',
        params 
    })
}

// 删除用户
export const deleteData = (params) => {
    return request({
        url: '/system/role/role_delete',
        method: 'GET',
        params 
    })
}

// 批量删除数据
export const deleteByIds = (params) => {
    return request({
        url: '/system/role/role_mult_delete',
        method: 'POST',
        data:params 
    })
}

// 修改数据
export const updateData = (params) => {
    return request({
        url: '/system/role/role_update',
        method: 'POST',
        data: params 
    })
}

// 添加数据
export const addData = (params) => {
    return request({
        url: '/system/role/role_add',
        method: 'POST',
        data: params 
    })
}

// 修改状态数据
export const updateStatusData = (params) => {
    return request({
        url: '/system/role/update_status',
        method: 'POST',
        data: params 
    })
}

// 修改排序数据
export const updateListorderData = (params) => {
    return request({
        url: '/system/role/update_listorder',
        method: 'POST',
        data: params 
    })
}


