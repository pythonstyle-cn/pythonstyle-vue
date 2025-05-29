<template>
        <el-scrollbar>
            <div class="sidebar-logo-container">
                <img class="logo" :src="props.logo" width="120" >
                <h3 v-show="isShowTitle">开发框架</h3>
            </div>
            <el-menu
                active-text-color="#ffd04b"
                background-color="none"
                class="el-menu-vertical"
                :default-active="$route.path"
                text-color="#fff"
                :unique-opened="true"
                :collapse="collapse"
                router
            >
                <MenuTree :menu_lists="props.menu_list"></MenuTree>
            </el-menu>
        </el-scrollbar>
</template>

<script setup>
    import { computed, reactive } from 'vue'
    import useMenuStore from "@/stores/menu-permission"
    import MenuTree from './MenuTree.vue'

    const menuStore = useMenuStore()
    const props = defineProps(['menu_list','logo'])

    const collapse = computed(()=>{
        return menuStore.getAsideType
    })
    const isShowTitle = computed(()=>{
        return menuStore.getAsideTitleShow
    })
</script>

<style>
    .el-menu-vertical .el-sub-menu__title,.el-menu-item{
        font-size: 15px !important;
    }
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        min-height: 400px;
    }
    .el-menu--popup-container{
        background: #040547 !important;
    }
</style>