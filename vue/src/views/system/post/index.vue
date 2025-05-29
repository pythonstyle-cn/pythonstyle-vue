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
                <el-form-item label="名 称" prop="dept_name">
                  <el-input class="search-input" v-model="queryParams.dept_name" size="small" placeholder="请输入部门名称"/>
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
            <el-button type="primary" :icon="Plus" v-permission="['system:post:add']" @click="handleAdd">新增</el-button>
            <el-button type="danger" :icon="Delete" v-permission="['system:post:mult_delete']" @click="multipleDelete">删除</el-button>
            <el-button :icon="Refresh" @click="getDataList"></el-button>
          </div>
        </el-card>
        <el-table  class="tree-table"
          v-loading="loading"
          :data="tableData" 
          style="width: 100%; margin-bottom: 0px; font-size: 15px;"
          min-height="500"
          :border="true"
          @selection-change="handleSelectionChange"
        >
          <el-table-column type="selection" width="55" />
          <el-table-column :prop="item.prop" :label="item.label" :align="item.align" :width="item.width" v-for="(item, index) in columnData" :key="index">
            <template #default="scope" v-if="item.prop ==='action'">
              <el-button type="warning" size="small" :icon="Edit" v-permission="['system:post:update']" @click="handleUpdate(scope.row)"></el-button>
              <el-popconfirm 
                title="确认删除记录吗?"
                @confirm="handDelete(scope.row)">
                <template #reference>
                  <el-button type="danger" size="small" v-permission="['system:post:delete']" :icon="DeleteFilled"></el-button>
                </template>
              </el-popconfirm>
            </template>
            <template #default="data" v-if="item.prop === 'status'">
              <el-switch v-model="data.row.status" 
                active-value="0" 
                inactive-value="1" 
                inline-prompt 
                active-text="启用" 
                inactive-text="禁用"  
                style="--el-switch-on-color: #409eff; --el-switch-off-color: #ff4949"
                v-permission="['system:post:updateStatus']"
                @change="handleChangeStatus(data.row)" />
            </template>
            <template #default="data" v-if="item.prop === 'listorder'">
                <el-input class="listorder-input" type="number" v-permission="['system:post:update']" v-model="data.row.listorder" @change="handleChange(data.row)" />
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
      <!--添加修改弹框-->
      <el-dialog v-model="dialogFormVisible" :title="title" :before-close="getDataList" width="500">
        <el-form  :model="form" ref="postFormRef" :rules="rules" label-width="90px">
          <el-form-item label="岗位名称" :label-width="formLabelWidth" prop="post_name">
            <el-input v-model="form.post_name" autocomplete="off" />
          </el-form-item>
          <el-form-item label="岗位编码" :label-width="formLabelWidth" prop="post_code">
            <el-input v-model="form.post_code" autocomplete="off" />
          </el-form-item>
          <el-form-item label="岗位排序" :label-width="formLabelWidth">
            <el-input-number v-model="form.listorder" controls-position="right"/>
          </el-form-item>
          <el-form-item label="岗位状态" :label-width="formLabelWidth">
            <el-radio-group v-model="form.status">
                <el-radio value="0">开启</el-radio>
                <el-radio value="1">禁用</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="备注" :label-width="formLabelWidth">
            <el-input v-model="form.remark" type="textarea" />
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
    import { getList, updateData, updateStatusData, deleteData, deleteByIds,addData,getInfoData } from '@/api/sysetm/post'
    import  {columnData}  from './columnData'
    import {Edit,DeleteFilled,Plus,Search,Refresh,Delete} from '@element-plus/icons-vue'
    import { ElMessage } from 'element-plus'
    import Pagination from '@/components/Pagination'

    const statusOptions = [
      { label: '启用', value: '0'},
      { label: '禁用', value: '1'}
    ]
    const searchForm = ref()
    const multipleSelection = ref([])
    const expand = ref(true)
    const tableData = ref([])
    const loading = ref(false)
    const total = ref(0)
    const queryParams =ref({
        pageNum: 1,
        pageSize: 10,
        post_name: '',
        status: ''
    })

    const dialogFormVisible = ref(false)
    const title = ref('')
    const form = ref({})
    const postFormRef = ref()
    const rules = {
      post_name: [{ required: true, message: "岗位名称不能为空", trigger: "blur" }],
      post_code: [{ required: true, message: "岗位编码不能为空", trigger: "blur" }],
    }

    /** 取消按钮 */
    const closeDialogFormVisible = () => {
      dialogFormVisible.value = false;
      reset();
    }
    /** 表单重置 */
    const reset = () => {
      form.value = {
        post_id: undefined,
        post_code: undefined,
        post_name: undefined,
        listorder: 1,
        status: '0',
        remark: undefined
      }
    }

    /** 新增按钮操作 */
    const handleAdd = () => {
      reset();
      dialogFormVisible.value = true;
      title.value = "添加岗位"
    }
    /** 修改按钮操作 */
    const handleUpdate = (row) => {
      reset();
      const postId = row.post_id
      getInfoData({post_id:postId}).then(response => {
        form.value = response.data
        dialogFormVisible.value = true
        title.value = "修改岗位"
      });
    }

    /** 提交对话框表单 **/
    const submitDialogForm = ()=>{
      if (!postFormRef.value) return
      postFormRef.value.validate((valid) => {  
            if (valid) {   
              if(form.value.post_id != undefined || form.value.post_id > 0){
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

    /** 多选 */
    const handleSelectionChange = (val) => {
      multipleSelection.value = val
    }
    /** 删除操作 */
    const handDelete = async(params) => {
      let param = { 'post_id' : params.post_id }
      const res = await deleteData(param);
      if(res.code === 200){
        getDataList()
      }
    } 
    /** 搜索操作 */
    const handSearch = () => {
      getDataList()
    }
    /** 修改排序 */
    const handleChange = async(val) =>{
        const res = await updateData(val);
        if(res.code === 200){
            getDataList()
        }
    }
    /** 修改状态 */
    const handleChangeStatus = async(val) =>{
        const res = await updateStatusData(val);
        if(res.code === 200){
            getDataList()
        }
    }
    
    /** 搜索表单重置 */
    const resetForm = (FormEL) => {
      FormEL.resetFields();
      getDataList()
    }

    /** 批量删除 */
    const multipleDelete = () => {
      let post_ids  = multipleSelection.value.map(item => item.post_id);
      const params = {'post_ids': post_ids}
      if(multipleSelection.value.length == 0 ){
        ElMessage({message: '请选择你要删除的项！',type: 'error', plain: true})
        return
      }

      const res = deleteByIds(params)
  
      if(res.code === 200){
            getDataList()
      }
    }

    /** 获取列表数据 */
    const getDataList = async() => {
      loading.value = true
      if(dialogFormVisible.value) dialogFormVisible.value = false
      const res = await getList(queryParams.value);
      if(res.code === 200){
        tableData.value = res.data.list
        total.value = res.data.total  
      }
      loading.value = false 
    }
    getDataList()
  </script>
  <style>
  
  </style>