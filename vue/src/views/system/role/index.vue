<template>
    <el-scrollbar>
      <div class="table-content">
        <el-card class="handle-card">
          <div class="search">
            <el-popover placement="bottom-start" :width="400" trigger="hover">
            <template #reference>
              <el-button :icon="Search" circle />
            </template>
            <div class="search-content">
              <el-form :inline="true" :model="queryParams" ref="searchForm">
                <el-form-item label="名 称" prop="role_name">
                  <el-input class="search-input" v-model="queryParams.role_name" size="small" placeholder="请输入角色名称"/>
                </el-form-item>
                <el-form-item label="状 态" prop="status">
                <el-select
                    v-model="queryParams.status"
                    placeholder="选择状态"
                    size="small"
                    class="search-input"
                    :teleported="false"
                >
                  <el-option
                    v-for="item in statusOptions"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
                </el-form-item>
                <div class="search-popover-btn">
                  <el-button type="primary" size="small" :icon="Search" @click="handSearch">搜索</el-button>
                  <el-button size="small" @click="resetForm(searchForm)">重置</el-button>
                </div>
                
              </el-form>
            </div>
          </el-popover>
          </div>
          <div class="handle">
            <el-button type="primary" :icon="Plus" v-permission="['system:role:role_add']" @click="handleAdd">新增</el-button>
            <el-button type="danger" :icon="Delete" v-permission="['system:role:role_mult_delete']" @click="multipleDelete">删除</el-button>
            <el-button :icon="Refresh" @click="getDataList"></el-button>
          </div>
        </el-card>
        <el-table  class="tree-table"
          v-loading="loading"
          :data="tableData" 
          style="width: 100%; margin-bottom: 0px; font-size: 15px;"
          row-key="role_id"
          min-height="500"
          :default-expand-all="expand"
          :border="true"
          @selection-change="handleSelectionChange"
        >
          <el-table-column type="selection" width="55" />
          <el-table-column :prop="item.prop" :label="item.label" :align="item.align" :width="item.width" v-for="(item, index) in columnData" :key="index">
            <template #default="data" v-if="item.prop === 'status'">
                <el-switch v-model="data.row.status" 
                active-value="0" 
                inactive-value="1" 
                inline-prompt 
                active-text="启用" 
                inactive-text="禁用"  
                style="--el-switch-on-color: #409eff; --el-switch-off-color: #ff4949"
                v-permission="['system:role:update_status']"
                @change="handleChangeStatus(data.row)" />
            </template>
            <template #default="scope" v-if="item.prop ==='action'">
              <template v-if="scope.row.role_id > 1">
                <!-- <el-button type="primary" size="small" :icon="Lock" title="角色权限">权限</el-button> -->
                <el-button type="warning" size="small" :icon="Edit" v-permission="['system:role:role_update']" @click="handleUpdate(scope.row)">修改</el-button>
                <el-popconfirm 
                  title="确认删除记录吗?"
                  @confirm="handDelete(scope.row)">
                  <template #reference>
                    <el-button type="danger" size="small" :icon="DeleteFilled" v-permission="['system:role:role_delete']" title="删除">删除</el-button>
                  </template>
                </el-popconfirm>
              </template>
            </template>
            <template #default="data" v-if="item.prop === 'listorder'">
                <el-input class="listorder-input" type="number" v-permission="['system:role:update_listorder']" v-model="data.row.listorder" @change="handleChangeListOrder(data.row)" />
            </template>
              
          </el-table-column>
        </el-table>
        <pagination
            v-show="total > 0"
            :total="total"
            v-model:page="queryParams.pageNum"
            v-model:limit="queryParams.pageSize"
            @pagination="getDataList"/>
      </div>
      <!--添加修改弹框-->
      <el-dialog v-model="dialogFormVisible" :title="title" :before-close="getDataList" width="500">
        <el-form  :model="form" ref="postFormRef" :rules="rules" label-width="90px">
          <el-form-item label="角色名称" prop="role_name">
            <el-input v-model="form.role_name" autocomplete="off" />
          </el-form-item>
          <el-form-item label="岗位排序">
            <el-input-number v-model="form.listorder" controls-position="right"/>
          </el-form-item>
          <el-form-item label="岗位状态">
            <el-radio-group v-model="form.status">
                <el-radio value="0">开启</el-radio>
                <el-radio value="1">禁用</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="备注">
            <el-input v-model="form.remark" type="textarea" />
          </el-form-item>
          <el-form-item label="角色权限">
            <el-tree
              ref="treeMenuRef"
              :data="dataOptions"
              accordion
              node-key="menu_id"
              :props="defaultProps"
              :default-checked-keys="menu_ids"
              show-checkbox
              @check="getCheckedKeys"
              style="border: 1px solid #409eff; width: 100%;"
            />
          </el-form-item>
        </el-form>
        <template #footer>
          <div class="dialog-footer">
            <el-button @click="closeDialogFormVisible">取消</el-button>
            <el-button type="primary" v-permission="['system:role:role_add']" @click="submitDialogForm">
              提交
            </el-button>
          </div>
        </template>
    </el-dialog>
    </el-scrollbar>
  </template>
  <script setup>
    import { ref } from 'vue';
    import { getRoleList, updateData, updateStatusData, updateListorderData, deleteData, deleteByIds,addData,getInfoData } from '@/api/sysetm/role'
    import { getMenuList } from '@/api/sysetm/menu'
    import  {columnData}  from './columnData'
    import { ElMessage } from 'element-plus'
    import {Edit,DeleteFilled,Plus,Search,Refresh,Delete,Lock} from '@element-plus/icons-vue'
    import Pagination from '@/components/Pagination'

    const statusOptions = [
      { label: '启用', value: '0'},
      { label: '禁用', value: '1'}
    ]
    const defaultProps = {
      children: 'children',
      label: 'menu_name',
    }
    const dialogFormVisible = ref(false)
    const title = ref('')
    const form = ref({})
    const postFormRef = ref()
    const rules = {
      role_name: [{ required: true, message: "角色名称不能为空", trigger: "blur" }],
    }

    const searchForm = ref()
    const multipleSelection = ref([])
    const expand = ref(false)
    const tableData = ref([])
    const dataOptions = ref([])
    const menu_ids = ref([])
    const half_checked_ids = ref([])
    const loading = ref(false)
    const total = ref(0)
    const treeMenuRef = ref()
    const queryParams =ref({
        pageNum: 1,
        pageSize: 20,
        role_name: '',
        status: ''
    })
    const handleSelectionChange = (val) => {
      multipleSelection.value = val
    }
    const handDelete = async(params) => {
      let param = { 'role_id' : params.role_id }
      const res = await deleteData(param);
      if(res.code === 200){
        getDataList()
      }
    } 
    /** 修改状态 **/
    const handleChangeStatus = async(val) =>{
        const res = await updateStatusData(val);
        if(res.code === 200){
            getDataList()
        }
    }
    //获取选中的权限值
    const getCheckedKeys = (leafOnly,includeHalfChecked) =>{
      console.log('leafOnly',includeHalfChecked)
      menu_ids.value = includeHalfChecked.checkedKeys
      half_checked_ids.value = includeHalfChecked.halfCheckedKeys
    }
  
    /**操作搜索* */
    const handSearch = () => {
      getDataList()
    }
    /**操作排序 */
    const handleChangeListOrder = async(val) =>{
        const res = await updateListorderData(val);
        if(res.code === 200){
            getDataList()
        }
    }

    /**重置表单 */
    const resetForm = (FormEL) => {
      FormEL.resetFields();
      getDataList()
    }

    /**批量删除 */
    const multipleDelete = () => {
      let role_ids  = multipleSelection.value.map(item => item.role_id);
      const params = {'role_ids': role_ids}
      const res = deleteByIds(params)
      if(res.code === 200){
            getDataList()
      }
    }
    /**获取列表数据 */
    const getDataList = async() => {
      loading.value = true
      if(dialogFormVisible.value) dialogFormVisible.value = false
      const res = await getRoleList(queryParams.value);
      if(res.code === 200){
        tableData.value = res.data.list
        total.value = res.data.total  
      }
      loading.value = false 
    }

     /** 取消按钮 */
     const closeDialogFormVisible = () => {
      dialogFormVisible.value = false;
      reset();
    }
    /** 表单重置 */
    const reset = () => {
      form.value = {
        role_id: undefined,
        role_name: undefined,
        listorder: 1,
        status: '0',
        remark: undefined
      }
    }

    /** 新增按钮操作 */
    const handleAdd = () => {
      reset();
      menu_ids.value = []
      getMenuList().then(response => {
        dataOptions.value = response.data
        dialogFormVisible.value = true;
        title.value = "添加角色"
      });
      
    }
    /** 修改按钮操作 */
    const handleUpdate = (row) => {
      reset();
      const role_id = row.role_id
      getInfoData({role_id:role_id}).then(response => {
        form.value = response.data.role_info
        menu_ids.value = response.data.menu_ids
      })
      getMenuList().then(response => {
        dataOptions.value = response.data
        const ids = getIdsByPid(response.data, 0)
        dialogFormVisible.value = true
        title.value = "修改角色"
        menu_ids.value = filterOutExistingValues(menu_ids.value,ids)
      })
      
    }
    /*拿到顶级id*/
    const getIdsByPid = (data) =>{
      var ids = [];
      data.forEach(node => {
        if (node.children && node.children.length > 0) {
          ids.push(node.menu_id); // 如果当前节点有 children，则将其 id 加入结果数组
          // 递归处理子节点
          ids = ids.concat(getIdsByPid(node.children));
        }
      })
      return ids
    }
   
    /**过滤掉顶级 */
    const filterOutExistingValues = (arr1, arr2) => {
      return arr1.filter(value => !arr2.includes(value));
    }

    /** 提交对话框表单 **/
    const submitDialogForm = ()=>{
      if (!postFormRef.value) return
        postFormRef.value.validate((valid) => {  
            if(form.value.menu_ids == undefined &&  menu_ids.value.length == 0){
              valid = false
              ElMessage({ message: '角色权限不能为空！', type: 'error', duration: 3 * 1000 })
            }
            if (valid) {   
              form.value.menu_ids = [...menu_ids.value,...half_checked_ids.value]
              if(form.value.role_id != undefined || form.value.role_id > 0){
                console.log('form.value.menu_ids',form.value.menu_ids)
                updateData(form.value).then(res => {
                  ElMessage({ message: res.msg, type: 'success', duration: 3 * 1000 })
                  getDataList()
                })
              }else{
                addData(form.value).then(res => {
                  ElMessage({ message: res.msg, type: 'success', duration: 3 * 1000 })
                  getDataList()
                })
              }
            } 
        })
    }

    getDataList()
  </script>
  <style>
  
  </style>