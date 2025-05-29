<template>
<div>
    <template v-for="item in props.menu_lists">
      <el-sub-menu :index="item.menu_id" :key="item.menu_id" v-if="item.children && item.children.length > 0">
        <template #title>
            <el-icon v-if="item.icon !=='#'"><component :is="item.icon"></component></el-icon>
            <span>{{ item.menu_name }}</span>
        </template>
        <MenuTree :menu_lists="item.children"></MenuTree>
      </el-sub-menu>
      <el-menu-item :index="'/'+item.path" :key="item.menu_name" v-else>
        <el-icon v-if="item.icon !=='#'"><component :is="item.icon"></component></el-icon>
        <span>{{ item.menu_name }}</span>
      </el-menu-item>
    </template>
</div>
</template>
<script setup>
const props = defineProps(['menu_lists'])
</script>