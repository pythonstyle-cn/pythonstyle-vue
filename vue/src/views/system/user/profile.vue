<template>
    <div>
        <el-row>
            <el-col :span="12">
                <el-card>
                    <template #header>
                        <div class="card-header">
                            <span class="h-title">个人信息</span>
                        </div>
                    </template>
                    <div class="card-body">
                        <div class="d-flex" style="margin-bottom: 10px;">
                            <span>头 像：</span>
                            <el-upload class="avatar-uploader" :action="base_url +'/system/admin/public_upload_avtor'" name="file"
                                :headers="uploadHeaders"
                                :show-file-list="false" 
                                :on-success="handleAvatarSuccess"
                                :before-upload="beforeAvatarUpload">
                                <img v-if="avatarUrl" :src="avatarUrl" class="avatar" width="100" />
                                <el-icon v-else class="avatar-uploader-icon">
                                    <Plus />
                                </el-icon>
                            </el-upload>
                        </div>
                        <hr>
                        <el-form :model="form" ref="postFormRef" :rules="rules" label-width="90px" style="margin-top: 10px;">
                            <el-form-item label="账 号" prop="username">
                                <el-input type="text" v-model="form.username" disabled="disabled" />
                            </el-form-item>
                            <el-form-item label="昵 称" prop="nick_name">
                                <el-input type="text" v-model="form.nick_name" placeholder="输入您的昵称" />
                            </el-form-item>
                            <el-form-item label="邮 箱" prop="email" for="email">
                                <el-input type="email" v-model="form.email" placeholder="请输入正确的邮箱地址" />
                            </el-form-item>
                            <el-form-item label="简 介" prop="remark" for="remark">
                                <el-input type="textarea" v-model="form.remark"></el-input>
                            </el-form-item>
                            
                        </el-form>

                    </div>
                    <template #footer><el-button type="primary" style="float: right; margin-bottom: 20px;" @click="submitForm">提交</el-button></template>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>
<script setup>
import { ref, computed } from 'vue';
import { getInitData, editProfile } from '@/api/sysetm/user'
import { Plus} from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { getToken } from '@/utils/Token'
import noavator from '@/assets/images/default_avatar.png';

const avatarUrl = ref(noavator)
const postFormRef = ref()
const base_url = import.meta.env.VITE_APP_BASE_API
const form = ref({
    username: undefined,
    avatar: undefined,
    nick_name: undefined,
    remark: undefined,
    email: undefined
})

const rules = {
    nick_name: [{ required: true, message: "昵称不能为空", trigger: "blur" }],
    email: [{ required: true, message: "邮箱不能为空", trigger: "blur" }]
}

const uploadHeaders = computed(() => {
  return {
    Authorization: 'Bearer ' + getToken(),
    Accept:'*/*',
    isUpload: 'true'
  }
})

const handleAvatarSuccess = (res) => {
    avatarUrl.value = res.data.filepath.length > 0 ? base_url + res.data.filepath : noavator
    form.value.avatar = base_url + res.data.filepath
}
const beforeAvatarUpload = (file) => {
    const isJPG = file.type === 'image/png' || file.type === 'image/jpeg'
    const isLt2M = file.size / 1024 / 1024 < 2

    if (!isJPG) {
        ElMessage({ message: '上传头像图片只能是 JPG或PNG格式!', type: 'error', duration: 3 * 1000 })
    }
    if (!isLt2M) {
        ElMessage({ message: '上传头像图片大小不能超过 2MB!', type: 'error', duration: 3 * 1000 })
    }
    return isJPG && isLt2M;
}

const getUserInfo = () => {
    getInitData().then(res => {
        form.value.username = res.data.username
        form.value.avatar = base_url + res.data.avatar
        form.value.nick_name = res.data.nick_name
        form.value.remark = res.data.remark
        form.value.email = res.data.email
        avatarUrl.value = res.data.avatar.length > 0 ? base_url + res.data.avatar : noavator
    })
}

/** 提交表单 **/
const submitForm = () => {
    if (!postFormRef.value) return
    postFormRef.value.validate((valid) => {
        if (valid) {
            editProfile(form.value).then(res => {
                ElMessage({ message: res.msg, type: 'success', duration: 3 * 1000 })
            })
        }
    })
}
getUserInfo()
</script>
<style>
    .avatar-uploader .el-upload {
        border: 1px dashed var(--el-border-color);
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: var(--el-transition-duration-fast);
    }

    .avatar-uploader .el-upload:hover {
        border-color: var(--el-color-primary);
    }

    .el-icon.avatar-uploader-icon {
        font-size: 18px;
        color: #8c939d;
        width: 90px;
        height: 90px;
        text-align: center;
    }
</style>