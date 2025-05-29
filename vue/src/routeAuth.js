import router from './router'
import { getToken,removeToken } from '@/utils/Token'
import useUserStore from "@/stores/user-store";
import useMenuStore from "@/stores/menu-permission";
import { isHttp } from '@/utils/comment'
import Layout from '@/layout'

//定义白名单
const routeWhiteList = ['/login', '/auth-redirect', '/bind', '/register'];

router.beforeEach((to, from, next) => {
    const userStore =  useUserStore()
    const menuStore =  useMenuStore()

    if (getToken()) {
      /* has token*/
      if (to.path === '/login') {
        next({ path: '/' })
      } else {
        if (userStore.roles.length === 0) {
          // 判断当前用户是否已拉取完user_info信息
          console.log('to',to)
          userStore.getUserInfo().then( () => {
            const role_ids = userStore.roles
            menuStore.generateRoutes(role_ids).then( routerLists =>{
              const home  = {path: '/index',name: '首页',component: () => import('@/views/index.vue'),}
              routerLists.push(home)
              router.addRoute(
                {
                  path: '',
                  component:  Layout,
                  name: '首页',
                  redirect:'/index',
                  children: routerLists
                },
              )
              next({ ...to, replace: true }) // hack方法 确保addRoutes已完成
            })
          }).catch(err => {
            removeToken()
            // useUserStore().logOut().then(() => {
            //   ElMessage.error(err)
            //   next({ path: '/' })
            // })
          })
        } else {
          next()
        }
      }
    } else {
      // 没有token
      if (routeWhiteList.indexOf(to.path) !== -1) {
        // 在登录白名单，直接进入
        next()
      } else {
        next(`/login?redirect=${to.fullPath}`) // 否则全部重定向到登录页
      }
    }
  });

  router.afterEach((to, from) => {
    // 在路由完成后执行的逻辑
  });
