import request from '@/utils/request'
// 获取验证码
export const getImgCode = () => {
    return request({
        url: '/system/captcha/captcha_image',
        headers:{
            'Browser':'EQVR4n',
            'isToken': false
        },
        method: 'GET',
        timeout: 20000
    })
}

//登录
export const login = (username, password, code, uuid)=>{
    const data = {
        username,
        password,
        code,
        uuid
      }
    return request({
        url: '/system/admin/login',
        headers: {
          isToken: false
        },
        method: 'POST',
        data: data
      })
}

//获取用户信息
export const getUserInfo = ()=>{
    return request({
      url: '/system/admin/public_get_userinfo',
      method: 'GET'
    })
}

//获取用户信息
export const loginOut = ()=>{
  return request({
    url: '/system/admin/login_out',
    method: 'GET'
  })
}
