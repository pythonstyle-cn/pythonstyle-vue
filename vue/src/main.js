import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import {zhCn} from 'element-plus/es/locale/index' // 中文语言
import { createPinia } from 'pinia'


import App from './App.vue'
import router from './router'
import './routeAuth'
import { permission } from './directive/permission'

import 'element-plus/dist/index.css'
import './assets/main.css'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)

app.directive('permission', permission);

app.use(ElementPlus,{locale: zhCn})
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.mount('#app')
