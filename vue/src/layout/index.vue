<template>
    <div class="common-layout">
      <el-container>
        <transition name="slide">
          <el-aside :width="asideWideth" class="aside" >
              <Menu :menu_list="menu_list" :logo="logo"/>
          </el-aside>
       </transition>
        <el-container>
          <el-header class="header"><Headers /></el-header>
          <el-main>
            <RouterView />
          </el-main>
        </el-container>
      </el-container>
    </div>
  </template>
  <script setup>

    import { ref, computed } from 'vue'
    import Menu from '@/layout/components/Menu'
    import Headers from '@/layout/components/Headers'
    import useMenuStore from '@/stores/menu-permission'
    import logo from '@/assets/images/logo-white.svg'

    const menuStore = useMenuStore()
    const menu_list = menuStore.menuList
    const asideWideth = computed(()=>{
      return !menuStore.getAsideType? '200px':'64px'
    })
  </script>