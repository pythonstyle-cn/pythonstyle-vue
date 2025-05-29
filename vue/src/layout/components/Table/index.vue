<template>
    <el-scrollbar>
      <div class="table-content">
        <el-card class="handle-card">
          <div class="search"><el-button :icon="Search" circle /></div>
          <div class="handle">
            <el-button type="primary" :icon="Plus">新增</el-button>
            <el-button :icon="Refresh" @click="initUserList"></el-button>
          </div>
        </el-card>
        <el-table  class="tree-table"
          v-loading="loading"
          :data="tableData" 
          style="width: 100%; margin-bottom: 0px; font-size: 15px;"
          row-key="menu_id"
          min-height="500"
          :default-expand-all="expand"
          :border="true"
        >
          <el-table-column :prop="item.prop" :label="item.label" :width="item.width" v-for="(item, index) in columnData" :key="index">
            <template v-if="item.prop ==='action'">
              <el-button type="warning" size="small" :icon="Edit"></el-button>
              <el-button type="danger" size="small" :icon="DeleteFilled"></el-button>
            </template>
          </el-table-column>
        </el-table>
        <Pagination
            v-show="total > 0"
            :total="total"
            v-model:page="queryParams.pageNum"
            v-model:limit="queryParams.pageSize"
            @pagination="getList"
        />
        <div class="page-contaner">
            
        </div>
      </div>
    </el-scrollbar>
  </template>
  <script setup>
    import { ref } from 'vue';
    import { getUserList } from '@/api/sysetm/user'
    import  {columnData}  from './userColumn'
    import {Edit,DeleteFilled,Plus,Search,Refresh} from '@element-plus/icons-vue'
    import Pagination from '@/layout/components/Pagination'
  
    
    const expand = ref(false)
    const tableData = ref([])
    const loading = ref(false)

    const total = ref(0)
    const queryParams = ref({
        pageNum:1,
        pageSize:1,
        username: '',
        phone: '',
        status: 0 
    })

    const getList = async() =>{
      loading.value = true
      const res = await getUserList(queryParams.value);
      if(res.code === 200){
        tableData.value = res.data.list
        total.value = res.data.total
      }
      loading.value = false
    }
    getList()
  </script>
  <style>
  
  </style>