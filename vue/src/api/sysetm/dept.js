import request from '@/utils/request'
// 获取列表信息
export const getList = (params) => {
    return request({
        url: '/system/dept/get_list',
        method: 'GET',
        params 
    })
}

// 获取数据信息
export const getInfoData = (params) => {
    return request({
        url: '/system/dept/public_get_info',
        method: 'GET',
        params 
    })
}

// 删除
export const deleteData = (params) => {
    return request({
        url: '/system/dept/delete',
        method: 'GET',
        params 
    })
}

// 批量删除用户
export const deleteByIds = (params) => {
    return request({
        url: '/system/dept/mult_delete',
        method: 'GET',
        params 
    })
}

// 修改用户
export const updateData = (params) => {
    return request({
        url: '/system/dept/update',
        method: 'POST',
        data: params 
    })
}

// 修改状态数据
export const updateStatusData = (params) => {
    return request({
        url: '/system/dept/updateStatus',
        method: 'POST',
        data: params 
    })
}

// 添加信息
export const addData = (params) => {
    return request({
        url: '/system/dept/add',
        method: 'POST',
        data: params 
    })
}


