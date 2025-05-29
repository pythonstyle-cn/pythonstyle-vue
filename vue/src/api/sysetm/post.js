import request from '@/utils/request'
// 获取列表信息
export const getList = (params) => {
    return request({
        url: '/system/post/get_list',
        method: 'GET',
        params 
    })
}

// 获取选择列表信息
export const getPostSelectList = () => {
    return request({
        url: '/system/post/public_get_select_list',
        method: 'GET'
    })
}

// 获取数据信息
export const getInfoData = (params) => {
    return request({
        url: '/system/post/get_info',
        method: 'GET',
        params 
    })
}

// 删除
export const deleteData = (params) => {
    return request({
        url: '/system/post/delete',
        method: 'GET',
        params 
    })
}

// 批量删除数据
export const deleteByIds = (params) => {
    return request({
        url: '/system/post/mult_delete',
        method: 'GET',
        params 
    })
}

// 修改数据
export const updateData = (params) => {
    return request({
        url: '/system/post/update',
        method: 'POST',
        data: params 
    })
}
// 修改状态数据
export const updateStatusData = (params) => {
    return request({
        url: '/system/post/updateStatus',
        method: 'POST',
        data: params 
    })
}

// 修改用户
export const addData = (params) => {
    return request({
        url: '/system/post/add',
        method: 'POST',
        data: params 
    })
}


