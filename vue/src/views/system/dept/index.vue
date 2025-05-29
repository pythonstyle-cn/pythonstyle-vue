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
                  <el-input class="search-input" v-model="queryParams.role_name" size="small" placeholder="请输入账号"/>
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
          <el-button type="info" :icon="Sort" plain @click="handleExpand">展开/折叠</el-button>
          </div>
          <div class="handle">
            <el-button type="primary" :icon="Plus" v-permission="['system:dept:add']" @click="handleAdd">新增</el-button>
            <el-button :icon="Refresh" @click="getDataList"></el-button>
          </div>
        </el-card>
        <el-table  class="tree-table"
          v-if="refTable"
          v-loading="loading"
          :data="tableData" 
          style="width: 100%; margin-bottom: 20px; font-size: 15px;"
          row-key="dept_id"
          min-height="500"
          :default-expand-all="expands"
          :border="true"
        >
          <el-table-column :prop="item.prop" :label="item.label" :width="item.width" v-for="(item, index) in columnData" :key="index">
            <template #default="data" v-if="item.prop === 'status'">
              <el-switch v-model="data.row.status" 
                active-value="0" 
                inactive-value="1" 
                inline-prompt 
                active-text="启用" 
                inactive-text="禁用"  
                style="--el-switch-on-color: #409eff; --el-switch-off-color: #ff4949"
                v-permission="['system:dept:updateStatus']"
                @change="handleChangeStatus(data.row)" />
            </template>
            <template #default="data" v-if="item.prop ==='action'">
              <el-button type="primary" size="small" :icon="Plus" v-permission="['system:dept:add']" @click="handleItemAdd(data.row)"></el-button>
              <el-button type="warning" size="small" :icon="Edit" v-permission="['system:dept:update']" @click="handleUpdate(data.row)"></el-button>
              <el-popconfirm 
                  title="确认删除记录吗?"
                  @confirm="handDelete(data.row)">
                  <template #reference>
                    <el-button type="danger" size="small" v-permission="['system:dept:delete']" :icon="DeleteFilled"></el-button>
                  </template>
                </el-popconfirm>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <!--添加修改弹框-->
      <el-dialog v-model="dialogFormVisible" :title="title" :before-close="getDataList" width="500">
        <el-form  :model="form" ref="postFormRef" :rules="rules" label-width="90px">
          <el-form-item label="上级部门" prop="parent_id">
            <el-tree-select
                v-model="form.parent_id"
                :data="dataOptions"
                :props="{ value: 'dept_id', label: 'dept_name', children: 'children' }"
                value-key="dept_id"
                placeholder="顶级部门"
                check-strictly
              />
          </el-form-item>
          <el-form-item label="部门名称" :label-width="formLabelWidth" prop="dept_name">
            <el-input v-model="form.dept_name" autocomplete="off" />
          </el-form-item>
          <el-form-item label="负责人" :label-width="formLabelWidth" prop="leader">
            <el-input v-model="form.leader" autocomplete="off" />
          </el-form-item>
          <el-form-item label="联系电话" :label-width="formLabelWidth" prop="phone">
            <el-input v-model="form.phone" autocomplete="off" />
          </el-form-item>
          <el-form-item label="邮箱" :label-width="formLabelWidth" prop="email">
            <el-input v-model="form.email" autocomplete="off" />
          </el-form-item>
          <el-form-item label="部门排序" :label-width="formLabelWidth">
            <el-input-number v-model="form.listorder" controls-position="right"/>
          </el-form-item>
          <el-form-item label="部门状态" :label-width="formLabelWidth">
            <el-radio-group v-model="form.status">
                <el-radio value="0">开启</el-radio>
                <el-radio value="1">禁用</el-radio>
            </el-radio-group>
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
    import { ref, nextTick } from 'vue';
    import { getList,updateStatusData,deleteData,updateData,addData,getInfoData } from '@/api/sysetm/dept'
    import  {columnData}  from './columnData'
    import { ElMessage } from 'element-plus'
    import {Edit,DeleteFilled,Plus,Search,Refresh,Sort} from '@element-plus/icons-vue'

    const statusOptions = [
      { label: '启用', value: '0'},
      { label: '禁用', value: '1'}
    ]
    const expands = ref(true)
    const refTable = ref(true)
    const tableData = ref([])
    const loading = ref(false)
    const queryParams =ref({
        dept_name: '',
        status: ''
    })
    const getDataList = async() =>{
      loading.value = true
      if(dialogFormVisible.value) dialogFormVisible.value = false
      const res = await getList();
      if(res.code === 200){
        tableData.value = res.data
      }
      loading.value = false
      
    }

    /** 修改状态 **/
    const handleChangeStatus = async(val) =>{
        const res = await updateStatusData(val);
        if(res.code === 200){
            getDataList()
        }
    }
  
    /** 删除操作 */
    const handDelete = async(params) => {
      let param = { 'dept_id' : params.dept_id }
      const res = await deleteData(param);
      if(res.code === 200){
        getDataList()
      }
    } 

    const dialogFormVisible = ref(false)
    const title = ref('')
    const form = ref({})
    const postFormRef = ref()
    const dataOptions = ref([])
    const rules = {
      dept_name: [{ required: true, message: "部门名称不能为空", trigger: "blur" }],
    }

    /**展开/收起操作**/
    const handleExpand = async() => {
      refTable.value = false
      expands.value = !expands.value
      await nextTick() //更新Dom
      refTable.value = true
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
        parent_id: undefined || 0,
        dept_name: undefined,
        listorder: 1,
        leader: undefined,
        phone: undefined,
        email: undefined,
        status: '0'
      }
    }

    /** 新增按钮操作 */
    const handleAdd = () => {
      reset();
      getList().then(response => {
        dataOptions.value = response.data
        dialogFormVisible.value = true;
        title.value = "添加部门"
        form.value.parent_id = '顶级部门'
      });
    }

    /** 新增按钮操作 */
    const handleItemAdd = (row) => {
      reset();
      getList().then(response => {
        dataOptions.value = response.data
        dialogFormVisible.value = true;
        title.value = "添加部门"
        if(row.dept_id == 0) {
          form.value.parent_id = '顶级部门'
        }else{
          form.value.parent_id = row.dept_id
        }
      });
    }

    /** 修改按钮操作 */
    const handleUpdate = (row) => {
      reset();
      const deptId = row.dept_id
      getInfoData({dept_id:deptId}).then(response => {
        form.value = response.data
        if(form.value.parent_id == 0) form.value.parent_id = '顶级部门'
      });
      getList().then(response => {
          dataOptions.value = response.data
          dialogFormVisible.value = true;
          title.value = "修改部门"
        });
    }

    /** 提交对话框表单 **/
    const submitDialogForm = ()=>{
      if (!postFormRef.value) return
      postFormRef.value.validate((valid) => {  
            if (valid) {   
              if(form.value.parent_id == undefined || form.value.parent_id =='顶级部门') form.value.parent_id = 0
              if(form.value.dept_id != undefined || form.value.dept_id > 0){
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