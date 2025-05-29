  /**
   * 自定义权限指令 v-Permission
   * @param {*} permission 
   * @returns 
   */
  import useMenuStore from "@/stores/menu-permission";
  // 导出自定义指令对象
  export const permission = {
    // 指令钩子函数，当绑定的元素插入到 DOM 中时调用
    mounted(el, binding) {
      // 获取传递给指令的参数
      const permission_value = binding.value
      const all_permission = '*:*:*'
      const permissions = useMenuStore().permissions
      console.log('perms',permissions)
      if (permission_value && permission_value instanceof Array && permission_value.length > 0) {
        const permissionFlag = permission_value
        console.log('permissionFlag',permissionFlag)
        // 检查用户是否有指定权限
        const hasPermission = permissions.some(permission => {
          
            return all_permission === permission || permissionFlag.includes(permission)
        })
        console.log('hasPermission',hasPermission)
        // 如果用户没有权限，则从 DOM 中移除元素
        if (!hasPermission) {
            el.parentNode && el.parentNode.removeChild(el);
        }
      }else{
        throw new Error(`请设置操作权限标签值`)
      }
    }
  };