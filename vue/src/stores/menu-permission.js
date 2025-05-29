import { defineStore } from 'pinia'
import {getToken,setToken,removeToken} from '@/utils/Token'
import { getRoleRouter } from '@/api/sysetm/menu'

// 匹配views里面所有的.vue文件
const modules = import.meta.glob('./../views/**/*.vue')

const useMenuStore = defineStore(
  'permission', {
  //state 是 store 的数据 (data)
  state: () => ({
    roles: [],
    menuRouter: [],
    menuList: [],
    permissions: [],
    roleIds: [],
    asideType: false
  }),
  //actions 则是方法 (methods)
  actions: {
    changeAsideType(){
      this.asideType = !this.asideType
    },
    setMenuList(data) {
      this.menuList = data
    },
    setRoles(data) {
      this.roles = data
    },
    setPermissions(data) {
      this.permissions = data
    },
    //设置路由：data-->后端传入的路由信息
    setMenuRouter(routerInfo) {
          this.menuRouter.push(routerInfo)
    },
    generateRoutes(role_ids) {
      //获取路由信息
      return new Promise((resolve, reject) => {
          getRoleRouter(role_ids).then(res => {
              if (res.code == 200) {
                const menuList = res.data.routers
                const permissions = res.data.permissions
                const roles_info = res.data.roles_info
                this.setRoles(roles_info)
                this.setMenuList(menuList)
                this.setPermissions(permissions)
                const routerLists = buildRouterData(menuList)
                this.setMenuRouter(routerLists)
                resolve(routerLists)
              } else {
                  reject()
              }
          })
      })
    },
  
  },
  //getters 是 store 的计算属性 (computed)
  getters: { 
    getAsideType(state){
      return state.asideType
    },
   
    getAsideTitleShow(state){
      return !state.asideType ? true : false
    }
  },
  
})

//递归生成路由
function buildRouterData(menu) {
  const routes = [];
  for (const item of menu) {
    if (item.menu_type !== 'F'){
      const route = {
        path:  `/${item.path}`,
        name: item.menu_name,
        component:  loadView(item.component),
        meta: {
          'title':item.menu_name,
          'icon':item.icon,
          'link':item.link
        },
        query:item.query,
      };

      if (item.children && item.children.length > 0 ) {
        route.children = buildRouterData(item.children);
      }else{
        delete route['children']
      }
      routes.push(route);
    }
  }
  return routes;
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

export default useMenuStore