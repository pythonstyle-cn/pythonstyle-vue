<template>
    <div></div>
</template>
  
  <script>
  import { useRoute, useRouter } from 'vue-router'
  
  export default {
    name: 'RedirectView',
    setup() {
      const route = useRoute()
      const router = useRouter()
      
      // 解析重定向路径
      const path = route.params.path
      const redirectPath = `${Array.isArray(path) ? path.join('/') : path}`
      
      // 立即重定向
      router.replace(redirectPath)
      
      return {}
    }
  }
  </script>