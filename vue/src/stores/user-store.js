import router from '@/router/index'
import { defineStore } from 'pinia'
import {getToken,setToken,removeToken} from '@/utils/Token'
import {login, getUserInfo, loginOut} from '@/api/login'
const base_url = import.meta.env.VITE_APP_BASE_API
const useUserStore = defineStore(
  'user', {
  //state 是 store 的数据 (data)
  state: () => ({
    token: getToken(),
    name: '',
    avatar: '',
    roles: []
  }),
  //actions 则是方法 (methods)
  actions: {
    login(userData) {
        const username = userData.username.trim()
        const password = userData.password
        const code = userData.code
        const uuid = userData.uuid
        return new Promise((resolve, reject) => {
          login(username, password, code, uuid).then(res => {
            setToken(res.data.token)
            this.token = res.data.token
            resolve(res)
          }).catch(error => {
            reject(error)
          })
        })
    },
    loginOut() {
      return new Promise((resolve, reject) => {
        loginOut().then((response) => {
          removeToken()
          this.token = ''
          this.roles = []
          this.permissions = []
          resolve(response)
          router.replace('/login')
        }).catch(error => {
          router.replace('/login')
          reject(error)
        })
      })
    },
   // 获取用户信息
   getUserInfo() {
      return new Promise((resolve, reject) => {
        getUserInfo().then(res => {
          const userData = res.data
          const avatar = userData.avatar.length > 0 ? base_url + userData.avatar : '';
          if (userData.role_id && userData.role_id.length > 0) { // 验证返回的roles是否是一个非空数组
            this.setRoles(userData.role_id)
          }
          this.name = userData.username
          this.avatar = avatar;
          resolve(res.data)
        }).catch(error => {
          reject(error)
        })
      })
    },
    setRoles(data) {
      this.roles = data
    },
  },
  //getters 是 store 的计算属性 (computed)
  getters: { 
    
  },
  
})

function filterAsyncRouter(asyncRouterMap, lastRouter = false, type = false) {
  return asyncRouterMap.filter(route => {
    if (type && route.children) {
      route.children = filterChildren(route.children)
    }
    
    if (route.component) {
      // Layout ParentView 组件特殊处理
      if (route.component === 'Layout') {
        route.component = Layout
      } else if (route.component === 'ParentView') {
        route.component = ParentView
      } else if (route.component === 'InnerLink') {
        route.component = InnerLink
      } else {
        route.component = loadView(route.component)
      }
    }
    if (route.children != null && route.children && route.children.length) {
      route.children = filterAsyncRouter(route.children, route, type)
    } else {
      delete route['children']
      delete route['redirect']
    }
    return true
  })
}
function filterChildren(childrenMap, lastRouter = false) {
  var children = []
  childrenMap.forEach((el, index) => {
    if (el.children && el.children.length) {
      if (el.component === 'ParentView' && !lastRouter) {
        el.children.forEach(c => {
          c.path = el.path + '/' + c.path
          if (c.children && c.children.length) {
            children = children.concat(filterChildren(c.children, c))
            return
          }
          children.push(c)
        })
        return
      }
    }
    if (lastRouter) {
      el.path = lastRouter.path + '/' + el.path
    }
    children = children.concat(el)
  })
  
  return children
}

export const loadView = (view) => {
  let res;
  for (const path in modules) {
    const dir = path.split('views/')[1].split('.vue')[0];
    if (dir === view) {
      res = () => modules[path]();
    }
  }
  return res;
}

export default useUserStore