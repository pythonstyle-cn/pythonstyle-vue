<template>
    <div class="avatar-content">
        <span class="user-role">[{{ username }}
            <span v-for="(roleinfo, index) in rolename" :key="index"> -{{ roleinfo.role_name }} </span>]</span>
        <el-dropdown>
            <el-avatar class="useravatar" :size="30" :src="avatarUrl" />
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item @click="gotoUrl"><el-icon>
                            <Pointer />
                        </el-icon> 帮助文档</el-dropdown-item>
                    <el-dropdown-item @click="changeProfile" v-permission="['system:user:profile']"><el-icon>
                            <Edit />
                        </el-icon> 个人信息</el-dropdown-item>
                    <el-dropdown-item @click="changePassword" v-permission="['system:admin:change_password']"><el-icon>
                            <Edit />
                        </el-icon> 修改密码</el-dropdown-item>
                    <el-dropdown-item @click="loginOut"><el-icon>
                            <SwitchButton />
                        </el-icon> 退出登录</el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import router from '@/router/index'
import useUserStore from "@/stores/user-store";
import useTagsViewStore from '@/stores/tags-view-store'
import useMenuStore from "@/stores/menu-permission";
import { ElMessage } from 'element-plus'
import noavator from '@/assets/images/default_avatar.png';

const useStore = useUserStore()
const useMenu = useMenuStore()
const tagsViewStore = useTagsViewStore() 
const avatarUrl = ref(useStore.avatar || noavator)
const username = ref('')
const rolename = ref([])
username.value = useStore.name
rolename.value = useMenu.roles


const loginOut = async () => {
    var res = await useStore.loginOut()
    if (res.code == 200) {
        ElMessage({ message: res.msg, type: 'success', duration: 5 * 1000 })
        tagsViewStore.removeAllViews()
    }
}
const gotoUrl = () => {
    window.open('https://doc.pythonstyle.cn', '_blank');
}

const changeProfile = () => {
    router.push({
        path: '/change_profile', // 目标页面路径
        query: {}      // 传递当前行的 ID 作为参数
    });
}
const changePassword = () => {
    router.push({
        path: '/change_password', // 目标页面路径
        query: {}      // 传递当前行的 ID 作为参数
    });
}
</script>
<style>
.avatar-content {
    height: auto;
}

.avatar-content .user-role {
    line-height: 35px;
    padding-right: 10px;
}

.useravatar {
    position: relative;
    top: 15px
}

.useravatar:hover {
    cursor: pointer;
}

.useravatar:focus {
    outline: none;
}

.el-popper.is-light {
    background: none !important;
}
</style>