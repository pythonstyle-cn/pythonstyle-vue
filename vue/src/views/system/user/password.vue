<template>
    <div>
        <el-row>
            <el-col :span="12">
                <el-card>
                    <template #header>
                        <div class="card-header">
                            <span class="h-title">修改密码</span>
                        </div>
                    </template>
                    <div class="card-body">
                        <el-form :model="form" ref="postFormRef" :rules="rules" label-width="90px">
                            <el-form-item label="旧密码" prop="old_password">
                                <el-input type="password" v-model="form.old_password" placeholder="输入账号的原登录密码" />
                            </el-form-item>
                            <el-form-item label="新密码" prop="password">
                                <el-input type="password" v-model="form.password" placeholder="输入新的密码" />
                            </el-form-item>
                            <el-form-item label="确认密码" prop="new_password" for="new-password">
                                <el-input type="password" v-model="form.new_password" placeholder="再次输入确认新密码" />
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
import { ref } from 'vue';
import { editPassword } from '@/api/sysetm/user'
import { ElMessage } from 'element-plus'

const form = ref({
    old_password: undefined,
    password: undefined,
    new_password: undefined
})
const postFormRef = ref()
const rules = {
    old_password: [{ required: true, message: "旧密码不能为空", trigger: "blur" }],
    password: [{ required: true, message: "新密码不能为空", trigger: "blur" }],
    new_password: [{ required: true, message: "确认密码不能为空", trigger: "blur" }],
}

/** 提交表单 **/
const submitForm = () => {
    if (!postFormRef.value) return
    postFormRef.value.validate((valid) => {
        if (valid) {
            editPassword(form.value).then(res => {
                ElMessage({ message: res.msg, type: 'success', duration: 3 * 1000 })
            })
        }
    })
}
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