import request from '@/utils/request'
// 获取用户列表
export const getUserList = (params) => {
    return request({
        url: '/system/user/get_list',
        method: 'GET',
        params 
    })
}
// 获取数据信息
export const getInfoData = (params) => {
    return request({
        url: '/system/user/public_get_info',
        method: 'GET',
        params 
    })
}

// 删除用户
export const deleteData = (params) => {
    return request({
        url: '/system/user/user_delete',
        method: 'GET',
        params 
    })
}

// 修改用户
export const updateData = (params) => {
    return request({
        url: '/system/user/update',
        method: 'POST',
        data: params 
    })
}

// 修改状态数据
export const updateStatusData = (params) => {
    return request({
        url: '/system/user/updateStatus',
        method: 'POST',
        data: params 
    })
}

// 添加数据
export const addData = (params) => {
    return request({
        url: '/system/user/add',
        method: 'POST',
        data: params 
    })
}

// 获取用户角色数据
export const getUserRolesData = (params) => {
    return request({
        url: '/system/user/public_get_user_roleids',
        method: 'POST',
        data: params 
    })
}
// 获取用户岗位数据
export const getUserPostsData = (params) => {
    return request({
        url: '/system/user/public_get_user_postids',
        method: 'POST',
        data: params 
    })
}

export const getInitData = () => {
    return request({
        url: '/system/admin/public_get_userinfo',
        method: 'POST'
    })
}

export const editProfile = ( data ) => {
    return request({
        url: '/system/admin/profile',
        method: 'POST',
        data:data
    })
}

export const editPassword = ( data ) => {
    return request({
        url: '/system/admin/change_password',
        method: 'POST',
        data:data
    })
}


