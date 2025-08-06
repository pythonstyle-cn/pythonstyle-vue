import router from './router'
import { getToken,removeToken } from '@/utils/Token'
import useUserStore from "@/stores/user-store";
import useMenuStore from "@/stores/menu-permission";
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
          userStore.getUserInfo().then( () => {
            const role_ids = userStore.roles
            menuStore.generateRoutes(role_ids).then( routerLists =>{
              const home = {
                path: '/index',
                name: '工作台', // 这里为首页设置一个唯一的名称
                component: () => import('@/views/index.vue'),
              };
          
              // 将首页路由添加到路由列表中
              routerLists.push(home);
              // 添加父路由
              router.addRoute({
                path: '',
                component: Layout,
                name: '首页', // 修改父路由的名称，确保和子路由不重复
                redirect: '/index',
                children: routerLists, // 将生成的子路由传入
              });
              next({ ...to, replace: true }) // hack方法 确保addRoutes已完成
            })
          }).catch(err => {
            removeToken()
            // useUserStore().logOut().then(() => {
            //   ElMessage.error(err)
            //   next({ path: '/' })
            // })
          })
        } else  {
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
