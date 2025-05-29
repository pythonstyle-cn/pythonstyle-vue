<template>
    <div class="avatar-content">
        <span class="user-role">[{{ username }}
            <span v-for="(roleinfo,index) in rolename" :key="index"> -{{ roleinfo.role_name }} </span>]</span>
        <el-dropdown>
        <el-avatar class="useravatar" :size="40" :src="avatarUrl" />
        <template #dropdown>
        <el-dropdown-menu>
            <el-dropdown-item @click="gotoUrl"><el-icon><Pointer /></el-icon> 帮助文档</el-dropdown-item>
            <el-dropdown-item><el-icon><Edit /></el-icon> 修改密码</el-dropdown-item>
            <el-dropdown-item @click="loginOut"><el-icon><SwitchButton /></el-icon> 退出登录</el-dropdown-item>
        </el-dropdown-menu>
        </template>
    </el-dropdown>
    </div>
    
</template>
<script setup>
    import { ref } from 'vue';
    import useUserStore from "@/stores/user-store";
    import useMenuStore from "@/stores/menu-permission";
    import { ElMessage } from 'element-plus'
    import noavator from '@/assets/images/noavator.jpg';
    
    const useStore =  useUserStore()
    const useMenu = useMenuStore()
    console.log('useStore.avatar', useStore.avatar)
    const avatarUrl = useStore.avatar || noavator
    const username = ref('')
    const rolename = ref([])
    username.value = useStore.name
    rolename.value = useMenu.roles

    const loginOut = async ()=>{
        var res = await useStore.loginOut()
        if(res.code ==200){
            ElMessage({ message: res.msg, type: 'success', duration: 5 * 1000 })
        }
    }
    const gotoUrl = ()=>{
        window.open('https://doc.pythonstyle.cn', '_blank');
    }
</script>
<style>
    .avatar-content{
        height: auto;
    }
    .avatar-content .user-role{
        line-height:35px;
        padding-right: 10px;
    }
    .useravatar{
        position: relative;
        top:15px
    }
    .useravatar:hover{
        cursor: pointer;
    }
    .useravatar:focus {
        outline: none;
    }
    .el-popper.is-light{
        background: none !important;
    }
</style>