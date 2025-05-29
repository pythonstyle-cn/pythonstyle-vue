<template>
    <el-breadcrumb class="breadcrumb-content" separator="/">
        <template v-for="(item, index) in breadcrumbList">
            <el-breadcrumb-item :key="index" class="item" v-if="index==0" :to="{path:'/'}">
                {{item.name}}
            </el-breadcrumb-item>
            <el-breadcrumb-item v-else :key="index+1" >{{item.name}}</el-breadcrumb-item>
        </template>
    </el-breadcrumb>
  </template>
<script setup>
    import { useRoute } from 'vue-router';
    import { ref,watch } from 'vue';
    const route = useRoute()
    const breadcrumbList = ref([])
    const initBreadcrumb = ()=>{
        breadcrumbList.value = route.matched
    }
    watch(route, 
        ()=>{
            initBreadcrumb()
        },
        {deep:true, immediate:true}
    )
</script>
<style>
    .breadcrumb-content{
        margin-left: 15px;
        font-size: 0.9rem !important;
        font-weight: normal;
        margin-bottom: 6px;
    }
    .breadcrumb-content .el-breadcrumb__item .el-breadcrumb__inner a{
        font-weight: normal !important;
    }
    .breadcrumb-content .item span.is-link{
        font-weight: 200 !important;
    }
    .redirect{
        cursor: pointer;
    }
    .redirect:hover{
        color: #111;
    }
</style>