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
                <el-form-item label="上级部门" prop="parent_id">
                  <el-tree-select
                      v-model="form.parent_id"
                      :data="dataDeptOptions"
                      :props="{ value: 'dept_id', label: 'dept_name', children: 'children' }"
                      value-key="dept_id"
                      placeholder="顶级部门"
                      check-strictly
                    />
                </el-form-item>
                <el-form-item label="账 号" prop="username">
                  <el-input class="search-input" v-model="queryParams.username" size="small" placeholder="请输入账号"/>
                </el-form-item>
                <el-form-item label="电 话" prop="phone">
                  <el-input class="search-input" v-model="queryParams.phone" size="small" placeholder="请输入用户电话"/>
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
                    v-for="item in userStatusOptions"
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
            <el-button type="primary" :icon="Plus" v-permission="['system:user:add']" @click="handleAdd">新增</el-button>
            <el-button type="danger" :icon="Delete" v-permission="['system:user:user_delete']" @click="multipleDelete">删除</el-button>
            <el-button :icon="Refresh" @click="getDataList"></el-button>
          </div>
        </el-card>
        <el-table  class="tree-table"
          v-loading="loading"
          :data="tableData" 
          style="width: 100%; margin-bottom: 0px; font-size: 15px;"
          row-key="user_id"
          min-height="500"
          :border="true"
        >
          <el-table-column :prop="item.prop" :label="item.label" :align="item.align" :width="item.width" v-for="(item, index) in columnData" :key="index">
            <template #default="data" v-if="item.prop ==='sex'">
              <span v-if="data.row.sex =='0'">男</span>
              <span v-if="data.row.sex =='1'">女</span>
              <span v-if="data.row.sex =='2'">未知</span>
            </template>
            <template #default="data" v-if="item.prop === 'status'">
              <el-switch v-model="data.row.status" 
                active-value="0" 
                inactive-value="1" 
                inline-prompt 
                active-text="启用" 
                inactive-text="禁用"  
                style="--el-switch-on-color: #409eff; --el-switch-off-color: #ff4949"
                v-permission="['system:user:updateStatus']"
                @change="handleChangeStatus(data.row)" />
            </template>
            <template #default="scope" v-if="item.prop ==='action'">
              <el-button type="warning" size="small" :icon="Edit" @click="handleUpdate(scope.row)"  v-permission="['system:user:update']"></el-button>
              <el-popconfirm 
                title="确认删除记录吗?"
                @confirm="handDelete(scope.row)">
                <template #reference>
                  <el-button type="danger" size="small" :icon="DeleteFilled"></el-button>
                </template>
              </el-popconfirm>
            </template>
          </el-table-column>
        </el-table>
        <pagination
            v-show="total > 0"
            :total="total"
            v-model:page="queryParams.pageNum"
            v-model:limit="queryParams.pageSize"
            @pagination="getDataList"
        />
      </div>
      <!--添加/修改 弹框-->
      <el-dialog v-model="dialogFormVisible" :title="title" :before-close="getDataList" width="700">
          <el-form inline="true" :model="form" ref="postFormRef" :rules="rules" label-width="90px">
            <el-form-item label="用户名称" prop="username">
              <el-input v-model="form.username" autocomplete="off" placeholder="请输入用户名" />
            </el-form-item>
            <el-form-item label="用户昵称" prop="nick_name">
              <el-input v-model="form.nick_name" autocomplete="off" placeholder="请输入用户昵称" />
            </el-form-item>
            <el-form-item label="用户密码" prop="password" >
              <el-input type="password" :disabled="isUpdateHandle" v-model="form.password" autocomplete="off" placeholder="请输入用户密码" />
            </el-form-item>
            <el-form-item label="所属角色" prop="role_ids">
              <el-select
                  multiple
                  collapse-tags="2"
                  v-model="form.role_ids">
                <el-option
                  v-for="item in dataRoleOptions"
                  :key="item.role_id"
                  :label="item.role_name"
                  :value="item.role_id"
                />
            </el-select>
            </el-form-item>
            <el-form-item label="手机号码" prop="phone">
              <el-input v-model="form.phone" autocomplete="off" placeholder="请输入手机号码" />
            </el-form-item>
            <el-form-item label="所属部门" prop="dept_id">
              <el-tree-select
                  v-model="form.dept_id"
                  :data="dataDeptOptions"
                  :props="{ value: 'dept_id', label: 'dept_name', children: 'children' }"
                  value-key="dept_id"
                  placeholder="请选择所属部门"
                  collapse-tags
                  check-strictly
                />
            </el-form-item>
            <el-form-item label="联系邮箱" prop="email">
              <el-input v-model="form.email" autocomplete="off" placeholder="请输入手机号码" />
            </el-form-item>
            <el-form-item label="所属岗位" prop="post_ids">
              <el-select
                  multiple
                  collapse-tags
                  v-model="form.post_ids">
                <el-option
                  v-for="item in dataPostOptions"
                  :key="item.post_id"
                  :label="item.post_name"
                  :value="item.post_id"
                />
            </el-select>
            </el-form-item>
            <el-form-item label="性别">
              <el-radio-group v-model="form.sex">
                <el-radio value="0">男</el-radio>
                <el-radio value="1">女</el-radio>
                <el-radio value="2">未知</el-radio>

              </el-radio-group>
            </el-form-item>
            <el-form-item label="状态">
              <el-radio-group v-model="form.status">
                <el-radio value="0">开启</el-radio>
                <el-radio value="1">禁用</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="备注">
              <el-input v-model="form.remark" type="textarea" style="width: 500px;" />
            </el-form-item>
          </el-form>
          <template #footer>
            <div class="dialog-footer">
              <el-button @click="closeDialogFormVisible">取消</el-button>
              <el-button type="primary" @click="submitDialogForm">
                提交
              </el-button>
            </div>
          </template>
      </el-dialog>
    </el-scrollbar>
  </template>
  <script setup>
    import { ref } from 'vue';
    import { getUserList, addData, deleteData, getInfoData, updateData, updateStatusData, getUserRolesData, getUserPostsData } from '@/api/sysetm/user'
    import { getList } from '@/api/sysetm/dept'
    import { getRoleSelectList } from '@/api/sysetm/role'
    import { getPostSelectList } from '@/api/sysetm/post'
    import  {columnData}  from './columnData'
    import { ElMessage } from 'element-plus'
    import {Edit, DeleteFilled, Plus, Search, Refresh, Delete} from '@element-plus/icons-vue'
    import Pagination from '@/components/Pagination'

    const userStatusOptions = [
      {
        label: '启用',
        value: '0'
      },
      {
        label: '禁用',
        value: '1'
      },
    ]
    const searchForm = ref()
    const tableData = ref([])
    const loading = ref(false)
    const total = ref(0)
    const queryParams =ref({
        pageNum: 1,
        pageSize: 20,
        dept_id: '',
        username: '',
        phone: '',
        status: ''
    })

    const dialogFormVisible = ref(false)
    const title = ref('')
    const form = ref({})
    const postFormRef = ref()
    const dataDeptOptions = ref([])
    const dataRoleOptions = ref([])
    const dataPostOptions = ref([])
    const isUpdateHandle = ref(false)
    const rules = {
      username: [{ required: true, message: "用户名称不能为空", trigger: "blur" }],
      role_ids: [{ required: true, message: "用户角色不能为空", trigger: "blur" }],
      password: [{ required: true, message: "用户密码不能为空", trigger: "blur" }],
      nick_name: [{ required: true, message: "用户昵称不能为空", trigger: "blur" }],
    }
    /**删除操作 */
    const handDelete = async(params) => {
      let param = {'user_id':params.user_id}
      const res = await deleteData(param);
      if(res.code === 200){
        getDataList()
      }
    } 
    /**状态操作 */
    const handleChangeStatus = async(val) =>{
        const res = await updateStatusData(val);
        if(res.code === 200){
            getDataList()
        }
    }
    /**搜索操作 */
    const handSearch = () => {
      getDataList()
    }

    /** 重置表单 */
    const resetForm = (FormEL) => {
      FormEL.resetFields();
      getDataList()
    }

    /** 取消按钮 */
    const closeDialogFormVisible = () => {
      dialogFormVisible.value = false;
      reset();
    }
    /** 表单重置 */
    const reset = () => {
      form.value = {
        dept_id: undefined,
        username: undefined,
        nick_name: undefined,
        sex: '0',
        phone: undefined,
        password: undefined,
        status: '0',
        remark: ''
      }
    }

    /** 新增按钮操作 */
    const handleAdd = () => {
      reset();
      isUpdateHandle.value = false
      getList().then(response => {
        dataDeptOptions.value = response.data
      });
      //获取角色列表
      getRoleSelectList().then(response => {
        dataRoleOptions.value = response.data
      })
      //获取岗位列表
      getPostSelectList().then(response => {
        dataPostOptions.value = response.data
        dialogFormVisible.value = true;
        title.value = "添加用户"
      })
    }

    /** 修改按钮操作 */
    const handleUpdate = (row) => {
      reset();
      isUpdateHandle.value = true
      const user_id = row.user_id
      getInfoData({user_id:user_id}).then(response => {
        form.value = response.data
        form.value.password = '*******'
      });
      getList().then(response => {
        dataDeptOptions.value = response.data
      });
      //获取角色列表
      getRoleSelectList().then(response => {
        dataRoleOptions.value = response.data
      })
      //获取岗位列表
      getPostSelectList().then(response => {
        dataPostOptions.value = response.data
      })
      //获取用户所属角色列表
      getUserRolesData({user_id:user_id}).then(response => {
        form.value.role_ids = response.data
      })
      //获取用户所属角色列表
      getUserPostsData({user_id:user_id}).then(response => {
        form.value.post_ids = response.data
        dialogFormVisible.value = true;
        title.value = "修改用户"
      })
    }

    /** 提交对话框表单 **/
    const submitDialogForm = ()=>{
      if (!postFormRef.value) return
        postFormRef.value.validate((valid) => {  
            if (valid) {   
              if(form.value.user_id != undefined || form.value.user_id > 0){
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

    /**获取列表 */
    const getDataList = async() => {
      loading.value = true
      if(dialogFormVisible.value) dialogFormVisible.value = false
      const res = await getUserList(queryParams.value);
      if(res.code === 200){
        tableData.value = res.data.list
        total.value = res.data.total  
      }
      loading.value = false 
    }
    getDataList()
  </script>
  <style>
  .el-select{
    min-width: 195px;
  }
  </style>