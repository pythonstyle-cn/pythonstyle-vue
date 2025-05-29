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
                <el-form-item label="操作用户" prop="username">
                  <el-input class="search-input" v-model="queryParams.username" size="small" placeholder="请输入操作用户"/>
                </el-form-item>
                <el-form-item label="登录状态" prop="status">
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
            <el-button :icon="Refresh" @click="getDataList"></el-button>
          </div>
        </el-card>
        <el-table  class="tree-table"
          v-loading="loading"
          :data="tableData" 
          style="width: 100%; margin-bottom: 0px; font-size: 15px;"
          min-height="500"
          :border="true"
        >
          <el-table-column :prop="item.prop" :label="item.label" :align="item.align" :width="item.width" v-for="(item, index) in columnData" :key="index">
            <template #default="scope" v-if="item.prop ==='action'">
              <el-button type="warning" size="small" :icon="View" v-hasPermission="['system:operation_log:get_info']" @click="handleDetail(scope.row)">详情</el-button>
            </template>
            <template #default="scope" v-if="item.prop === 'status'">
             <span v-if="scope.row.status =='0'">登录成功</span>
             <span v-if="scope.row.status =='1'">登录失败</span>
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
     
    </el-scrollbar>
  </template>
  <script setup>
    import { ref } from 'vue';
    import { getList, getInfoData } from '@/api/monitor/login_log'
    import  {columnData}  from './columnData'
    import {View,Search,Refresh} from '@element-plus/icons-vue'
    import Pagination from '@/components/Pagination'

    const statusOptions = [
      { label: '登录成功', value: '0'},
      { label: '登录失败', value: '1'}
    ]
    const searchForm = ref()
    const tableData = ref([])
    const loading = ref(false)
    const total = ref(0)
    const queryParams =ref({
        pageNum: 1,
        pageSize: 10,
        username: '',
        status: ''
    })

    /** 搜索操作 */
    const handSearch = () => {
      getDataList()
    }
    
    /** 搜索表单重置 */
    const resetForm = (FormEL) => {
      FormEL.resetFields();
      getDataList()
    }

    /** 获取列表数据 */
    const getDataList = async() => {
      loading.value = true
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