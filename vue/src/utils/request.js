import axios from 'axios'
import { getToken,removeToken } from './Token';
import { ElNotification , ElMessageBox, ElMessage, ElLoading } from 'element-plus'

axios.defaults.headers['Content-Type'] = 'application/json;charset=utf-8'

// 是否显示重新登录
export let isRelogin = { show: false };

const service = axios.create({
    // axios中请求配置有baseURL选项，表示请求URL公共部分
    baseURL: import.meta.env.VITE_APP_BASE_API,
    // 超时
    timeout: 30000
})

// 添加请求拦截器
service.interceptors.request.use(function (config) {
    // 是否需要发送token
    const isToken = (config.headers || {}).isToken === false
    if (getToken() && !isToken) {
      config.headers['Authorization'] = 'Bearer ' + getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
    }
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });

// 添加响应拦截器
service.interceptors.response.use(function (response) {
      // 未设置状态码则默认成功状态
      const code = response.data.code || 200
      const msg =  response.data.msg || '未知错误，请联系系统管理员'
      
      if(response.request.responseType ===  'blob' || response.request.responseType ===  'arraybuffer'){
        return response.data
      }

      if (code === 401) {
        if (!isRelogin.show) {
            isRelogin.show = true;
            ElMessageBox.confirm('登录状态已过期，请重新登录', '系统提示', { confirmButtonText: '重新登录', cancelButtonText: '取消', type: 'warning' }).then(() => {
              isRelogin.show = false;
              useUserStore().logOut().then(() => {
                location.href = '/login';
              })
          }).catch(() => {
            isRelogin.show = false;
          });
        }
        return Promise.reject('无效的会话，或者会话已过期，请重新登录。')
      } else if (code === 500) {
        ElMessage({message: msg, type: 'error'})
        return Promise.reject(new Error(msg))
    } else if (code !== 200) {
        ElNotification.error({title: msg})
        return Promise.reject('error')
    } else {
        return Promise.resolve(response.data)
    }
    },
    function (error) {
      let {message, response} = error;
      if (message == "Network Error") {
          message = "后端接口连接异常";
      } else if (message.includes("timeout")) {
          message = "系统接口请求超时";
      } else {
          return Promise.resolve(response.data)
      }
      ElMessage({message: message, type: 'error', duration: 5 * 1000})
      return Promise.reject(error)
  });

export default service
