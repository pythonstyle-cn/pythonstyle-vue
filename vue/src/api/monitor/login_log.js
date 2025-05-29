import request from '@/utils/request'
// 获取列表信息
export const getList = (params) => {
    return request({
        url: '/system/login_log/get_list',
        method: 'GET',
        params 
    })
}


// 获取数据信息
export const getInfoData = (params) => {
    return request({
        url: '/system/login_log/get_info',
        method: 'GET',
        params 
    })
}



