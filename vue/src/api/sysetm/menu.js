import request from '@/utils/request'

// 获取菜单
export const getList = () => {
    return request({
        url: '/system/menu/menu_list',
        method: 'GET'
    })
}

// 获取菜单
export const getMenuList = () => {
    return request({
        url: '/system/menu/public_menu_list',
        method: 'GET'
    })
}

export const getRoleRouter = (role_ids) =>{
    const data = {
        role_ids
    }
    return request({
        url: '/system/menu/public_get_role_menu',
        method: 'POST',
        data: data
      })
}

// 获取数据信息
export const getInfoData = (params) => {
    return request({
        url: '/system/menu/get_info',
        method: 'GET',
        params 
    })
}

// 删除
export const deleteData = (params) => {
    return request({
        url: '/system/menu/delete',
        method: 'GET',
        params 
    })
}

// 修改用户
export const updateData = (params) => {
    return request({
        url: '/system/menu/update',
        method: 'POST',
        data: params 
    })
}

// 修改状态数据
export const updateStatusData = (params) => {
    return request({
        url: '/system/menu/updateStatus',
        method: 'POST',
        data: params 
    })
}

// 添加信息
export const addData = (params) => {
    return request({
        url: '/system/menu/menu_add',
        method: 'POST',
        data: params 
    })
}