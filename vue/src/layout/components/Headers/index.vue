<template>
    <div class="header-contaner">
        <div class="header-navbar">
            <Collapse />
            <Breadcrumb/>
            <div class="avatar">
                <span><el-icon title="帮助文档"><Promotion /></el-icon></span>
                <span><el-icon title="通知消息"><Bell /></el-icon></span>
                <Avatar/>
            </div>
        </div>
        <div class="header-tags">
            <TagsView/>
        </div>
    </div>
</template>
<script setup>
    import Collapse from './Collapse';
    import Breadcrumb from './Breadcrumb.vue';
    import  Avatar  from './Avatar.vue';
    import  TagsView  from './TagsView.vue';
</script>
<style scoped>
    .header-contaner{
        height: 100px;
        display: flex;
        width: 100%;
        flex-direction:column;
    }
    .header-navbar{
        width: 100%;
        display: flex;
        height: 60px;
        line-height: 60px;
        align-items: center; /* 垂直居中 */
        overflow: hidden;
        position: relative;
    }
    .avatar{
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: right;
    }
    .avatar span{
        margin-right: 30px;
        font-size: 1.3rem;
    }
    .avatar span:hover{
        cursor: pointer;
    }
    .header-tags{
        height: 40px;
        border-top: 1px solid #d3d1d1;
    }
    
</style>