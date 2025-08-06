import { createRouter, createWebHistory } from 'vue-router'
import RedirectView from '@/views/redirect/RedirectView.vue'
export const defaultRouter = [
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/register.vue')
  },
  // 添加重定向路由
  {
    path: '/redirect:path(.*)',
    name: 'Redirect',
    component: RedirectView
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: defaultRouter,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  },
})

export default router
