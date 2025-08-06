<template>
  <el-scrollbar>
    <div class="table-content">
      <el-card class="handle-card">
        <div class="search">
          <el-button type="info" :icon="Sort" plain @click="handleExpand">展开/折叠</el-button>
        </div>
        <div class="handle">
          <el-button type="primary" :icon="Plus" v-permission="['system:menu:menu_add']" @click="handleAdd">新增</el-button>
          <el-button :icon="Refresh" @click="getDataList"></el-button>
        </div>
      </el-card>
      <el-table class="tree-table" v-if="refTable" v-loading="loading" :data="tableData"
        style="width: 100%; margin-bottom: 20px; font-size: 15px;" row-key="menu_id" min-height="500"
        :default-expand-all="expands" :tree-props="{ children: 'children', hasChildren: 'hasChildren' }" :border="true">
        <el-table-column :prop="item.prop" :label="item.label" :align="item.align" :width="item.width"
          v-for="(item, index) in columnData" :key="index">
          <template #default="data" v-if="item.prop === 'icon'">
            <el-icon v-if="data.row.icon != '#'">
              <component :is="data.row.icon"></component>
            </el-icon>
          </template>
          <template #default="data" v-if="item.prop === 'status'">
            <el-switch v-model="data.row.status" active-value="0" inactive-value="1" inline-prompt active-text="启用"
              inactive-text="禁用" style="--el-switch-on-color: #409eff; --el-switch-off-color: #ff4949"
              v-permission="['system:menu:updateStatus']" @change="handleChangeStatus(data.row)" />
          </template>
          <template #default="data" v-if="item.prop === 'action'">
            <el-button type="primary" size="small" :icon="Plus" v-permission="['system:menu:menu_add']"
              @click="handleItemAdd(data.row)"></el-button>
            <el-button type="warning" size="small" :icon="Edit" v-permission="['system:menu:update']"
              @click="handleUpdate(data.row)"></el-button>
            <el-popconfirm title="确认删除记录吗?" @confirm="handDelete(data.row)">
              <template #reference>
                <el-button type="danger" size="small" v-permission="['system:menu:delete']"
                  :icon="DeleteFilled"></el-button>
              </template>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <!--添加修改弹框-->
    <el-dialog v-model="dialogFormVisible" :title="title" :before-close="getDataList" width="700">
      <el-form :inline="true" :model="form" ref="postFormRef" :rules="rules" label-width="120px">
        <el-form-item class="width100" label="上级菜单" prop="parent_id">
          <el-tree-select v-model="form.parent_id" :data="dataOptions"
            :props="{ value: 'menu_id', label: 'menu_name', children: 'children' }" value-key="menu_id" placeholder="顶级类目"
            check-strictly />
        </el-form-item>
        <el-form-item label="菜单类型" class="width100" prop="menu_type">
          <el-radio-group v-model="form.menu_type">
            <el-radio value="M">目录</el-radio>
            <el-radio value="C">菜单</el-radio>
            <el-radio value="F">按钮</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="菜单名称" prop="menu_name">
          <el-input v-model="form.menu_name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="菜单图标" prop="icon" v-if="form.menu_type != 'F'">
          <icon-picker v-model="form.icon" autocomplete="off" />
        </el-form-item>
        <el-form-item label="路由地址" prop="path" v-if="form.menu_type != 'F'">
          <template #label>
            <span>
              <el-tooltip content="路由地址是访问路由的地址：如`user` 路由会自动加上`/user`,如果是外链则是一个http(s)地址" placement="top">
                <el-icon><question-filled /></el-icon>
              </el-tooltip>
              路由地址
            </span>
          </template>
          <el-input v-model="form.path" autocomplete="off" placeholder="如：user,不要加`/`" />
        </el-form-item>
        <el-form-item label="组件地址" prop="component" v-if="form.menu_type == 'C'">
          <template #label>
            <span>
              <el-tooltip content="组件地址是访问路由的视图地址：如`system/user/add`" placement="top">
                <el-icon><question-filled /></el-icon>
              </el-tooltip>
              路由地址
            </span>
          </template>
          <el-input v-model="form.component" autocomplete="off" placeholder="如：system/user/add" />
        </el-form-item>
        <el-form-item label="路由参数" prop="query" v-if="form.menu_type == 'C'">
          <el-input v-model="form.query" autocomplete="off" placeholder="如：{'page':'1'}" />
        </el-form-item>
        <el-form-item label="权限标识" prop="perms" v-if="form.menu_type != 'M'">
          <el-input v-model="form.perms" autocomplete="off" placeholder="如：system:user:add" />
          <template #label>
            <span>
              <el-tooltip content="权限标识是访问路由的权限标识：如`system:user:add`,后端由`模块名称:控制器:方法组成`" placement="top">
                <el-icon><question-filled /></el-icon>
              </el-tooltip>
              权限标识
            </span>
          </template>
        </el-form-item>
        <el-form-item label="菜单序号" prop="listorder">
          <el-input-number v-model="form.listorder" controls-position="right" />
        </el-form-item>
        <el-form-item label="是否外链" prop="is_link" v-if="form.menu_type != 'F'">
          <el-radio-group v-model="form.is_link">
            <el-radio :value="0">否</el-radio>
            <el-radio :value="1">是</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="显示状态" v-if="form.menu_type != 'F'">
          <el-radio-group v-model="form.visible">
            <el-radio value="0">显示</el-radio>
            <el-radio value="1">隐藏</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="菜单状态" v-if="form.menu_type != 'F'">
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
import { ref, nextTick, watch } from 'vue';
import { getList, updateStatusData, deleteData, updateData, addData, getInfoData } from '@/api/sysetm/menu'
import { columnData } from './columnData'
import { ElMessage } from 'element-plus'
import { Edit, DeleteFilled, Plus, Sort, Refresh } from '@element-plus/icons-vue'
import IconPicker from '@/components/icons/IconPicker.vue'

var expands = ref(false)
const refTable = ref(true)
const tableData = ref([])
const loading = ref(false)

const getDataList = async () => {
  loading.value = true
  if (dialogFormVisible.value) dialogFormVisible.value = false
  const res = await getList();
  if (res.code === 200) {
    tableData.value = res.data
  }
  loading.value = false
}

/** 删除操作 */
const handDelete = async (params) => {
  let param = { 'menu_id': params.menu_id }
  const res = await deleteData(param);
  if (res.code === 200) {
    getDataList()
  }
}

const dialogFormVisible = ref(false)
const title = ref('')
const form = ref({})
const postFormRef = ref()
const dataOptions = ref([])
const rules = {
  menu_name: [{ required: true, message: "菜单名称不能为空", trigger: "blur" }],
  path: [{ required: true, message: "菜单路由不能为空", trigger: "blur" }],
}

/** 修改状态 **/
const handleChangeStatus = async (val) => {
  const res = await updateStatusData(val);
  if (res.code === 200) {
    getDataList()
  }
}

/**展开/收起操作**/
const handleExpand = async () => {
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
    menu_id: undefined,
    parent_id: undefined || 0,
    menu_name: undefined,
    listorder: 1,
    component: undefined,
    query: undefined,
    is_link: 0,
    is_cache: '0',
    menu_type: 'M',
    visible: '0',
    perms: undefined,
    icon: undefined,
    remark: undefined,
    status: '0'
  }
}

/** 新增按钮操作 */
const handleAdd = () => {
  reset();
  getList().then(response => {
    dataOptions.value = response.data
    dialogFormVisible.value = true;
    title.value = "添加菜单"
    form.value.parent_id = '顶级类目'
  });
}

/** 新增按钮操作 */
const handleItemAdd = (row) => {
  reset();
  getList().then(response => {
    dataOptions.value = response.data
    dialogFormVisible.value = true;
    title.value = "添加菜单"
    if (row.menu_id == 0) {
      form.value.parent_id = '顶级类目'
    } else {
      form.value.parent_id = row.menu_id
    }
  });
}

/** 修改按钮操作 */
const handleUpdate = (row) => {
  reset();
  const menu_id = row.menu_id
  getInfoData({ menu_id: menu_id }).then(response => {
    form.value = response.data
    if (form.value.parent_id == 0) form.value.parent_id = '顶级类目'
  });
  getList().then(response => {
    dataOptions.value = response.data
    dialogFormVisible.value = true;
    title.value = "修改菜单"
  });
}

/** 提交对话框表单 **/
const submitDialogForm = () => {
  if (!postFormRef.value) return
  postFormRef.value.validate((valid) => {
    if (valid) {
      if (form.value.parent_id == undefined || form.value.parent_id == '顶级类目') form.value.parent_id = 0
      if (form.value.menu_id != undefined || form.value.menu_id > 0) {
        updateData(form.value).then(res => {
          ElMessage({ message: res.msg, type: 'success', duration: 3 * 1000 })
          getDataList()
        })
      } else {
        addData(form.value).then(res => {
          ElMessage({ message: res.msg, type: 'success', duration: 3 * 1000 })
          getDataList()
        })
      }
    }
  })
}

//监听path 把权限值自动改为标准权限值
watch(() => form.value.component, (newComponent) => {
  if (newComponent && typeof newComponent === 'string') { // 确保 newPath 是非空字符串
    newComponent = newComponent.replace(/^\/|\/$/g, '');
    form.value.perms = newComponent.replace(/\//g, ':');
  }
})

getDataList()
</script>
<style>
.el-form--inline .el-form-item {
  width: 40%;
}

.el-form--inline .el-form-item.width100 {
  width: 100%;
}
</style>