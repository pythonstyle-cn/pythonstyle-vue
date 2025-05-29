<template>
    <div class="login">
      <el-form ref="ruleFormRef" :model="loginForm" :rules="loginRules" class="login-form">
          <h3 class="login-header">后台管理系统</h3>
          <el-form-item prop="username">
              <el-input
                      v-model="loginForm.username"
                      type="text"
                      size="large"
                      autocomplete="off"
                      placeholder="账号"
              >
                  <template #prefix><el-icon><UserFilled /></el-icon></template>
              </el-input>
          </el-form-item>
          <el-form-item prop="password">
              <el-input
                      v-model="loginForm.password"
                      type="password"
                      size="large"
                      autocomplete="off"
                      placeholder="密码"
                      @keyup.enter="submitLoginForm"
              >
                  <template #prefix><el-icon><Lock /></el-icon></template>
              </el-input>
          </el-form-item>
          <el-form-item prop="code" v-if="captchaEnabled">
              <el-input
                      v-model.number="loginForm.code"
                      size="large"
                      auto-complete="off"
                      placeholder="验证码"
                      style="width: 63%"
                      @keyup.enter="submitLoginForm"
              >
                  <template #prefix><el-icon><Stamp /></el-icon></template>
              </el-input>
              <div class="login-imagecode">
                  <div class="code-image">
                      <img :src="codeUrl" @click="getCode" class="login-image-code"/>
                  </div>

              </div>
          </el-form-item>

          <el-form-item style="width:100%; padding-top: 20px;">
              <el-button
                      :loading="loading"
                      size="large"
                      type="primary"
                      style="width:100%;"
                      @click="submitLoginForm()"
              >
                  <span v-if="!loading">登 录</span>
                  <span v-else>登 录 中...</span>
              </el-button>
              <div style="text-align: right; width: 100%;" v-if="register">
                  <router-link class="link-type" :to="'/register'">立即注册</router-link>
              </div>
              <el-row class="copyright">
                <el-col>Copyright © 2022-2024 All.</el-col>
              </el-row>
          </el-form-item>
        </el-form>
        
    </div>
</template>

<script setup>
    import { getImgCode } from "@/api/login"
    import { ref} from 'vue'
    import useUserStore  from "@/stores/user-store";
    import { ElMessage } from 'element-plus'
    import { useRouter } from 'vue-router';
    
    const router = useRouter();
    const userStore = useUserStore()
    
    const captchaEnabled = ref(true)
    const codeUrl = ref("")
    const loading = ref(false)
    const register = ref(false)
    const ruleFormRef = ref(null)
    const redirect = ref(undefined);

    const loginRules = {
        username: [{ required: true, message: '请输入您的账号名称', trigger: 'blur' }],
        password: [
            { required: true, message: '请输入您的密码', trigger: 'blur'},
            { min: 8, max: 20, message: '密码长度不得小于8位数，且需要大小写数字组合', trigger: 'blur' }
        ],
        code: [{ required: true, message: '请输入验证码', trigger: 'blur' }]
    }

    const loginForm = ref({
        username: "admin",
        password: "admin123",
        code: "",
        uuid: ""
    });

    const submitLoginForm = () => {
        loading.value = true
        if (!ruleFormRef.value) return
        ruleFormRef.value.validate((valid) => {  
            if (valid) {   
                // 调用action的登录方法
                userStore.login(loginForm.value).then(res => {
                    if(res.code ===200){
                        ElMessage({ message: res.msg, type: 'success', duration: 5 * 1000 })
                        router.push({ path: redirect.value || "/" });
                    }else{
                        loading.value = false;
                        // 重新获取验证码
                        ElMessage({ message: res.msg, type: 'error', duration: 5 * 1000 })
                        if (captchaEnabled.value) {
                            getCode();

                        }
                    }
                    //
                }).catch(() => {
                    loading.value = false;
                    // 重新获取验证码
                    if (captchaEnabled.value) {
                    getCode();
                    }
                });
            
            } else {
                loading.value = false;
                console.log('error submit!')
                return false
            }
        })
    }

    function getCode() {
        getImgCode().then(res => {
            captchaEnabled.value = res.data.captchaEnabled === undefined ? true : res.data.captchaEnabled;
            if (captchaEnabled.value) {
                codeUrl.value = "data:image/gif;base64," + res.data.img;
                loginForm.value.uuid = res.data.uuid;
            }
        });
    }
    getCode()
</script>
<style lang='scss' scoped>
    .login{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background: url('@/assets/images/login-bg-blur.jpg');
        background-size: cover;
    }
    h3.login-header {
        margin: 0px auto 30px auto;
        text-align: center;
        color: #707070;
    }
    .login .login-form{
        width: 360px;
        height: auto;
        border: 1px solid #dddddd;
        border-radius: 8px;
        padding: 15px;
        background: rgba(255,255,255,0.8);
    }
    .login .login-form .el-input {
        height: 37px;
        margin-top: 5px;
    }
    .login .login-form .el-input input {
        height: 37px;
    }
    .login .login-form .code-image{
        padding-top: 2px;
        margin-left: 15px;
        height: 35px;
    }
    .login .login-form .login-image-code{
        border: 1px solid #2579f8;
        height: 35px !important;
    }
    .copyright{
        width: 100%;
        margin-top: 10px;
        text-align: center;
    }
</style>
