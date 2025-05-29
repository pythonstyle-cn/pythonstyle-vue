<template>
    <div class="page-contaner">
        <el-pagination
            v-model:current-page="currentPage"
            v-model:page-size="pageSize"
            :page-sizes="pageSizes"
            :pager-count="pagerCount"
            :disabled="disabled"
            :background="background"
            :layout="layout"
            :total="total"
            small
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
        />   
    </div>

</template>   
<script setup>
    import { computed } from 'vue'
    const emit = defineEmits(['pagination','update:page','update:limit'])
    
    const props = defineProps({
        total: {
            required: true,
            type: Number
        },
        page: {
            type: Number,
            default: 1
        },
        limit: {
            type: Number,
            default: 20
        },
        pageSizes: {
            type: Array,
            default() {
            return [10, 15, 20, 30, 40, 50, 100]
            }
        },
        // 移动端页码按钮的数量端默认值5
        pagerCount: {
            type: Number,
            default: document.body.clientWidth < 992 ? 5 : 7
        },
        layout: {
            type: String,
            default: 'total, sizes, prev, pager, next, jumper'
        },
        background: {
            type: Boolean,
            default: true
        }
    })

    const currentPage = computed({
        get() {
            return props.page
        },
        set(val) {
            console.log('update:page',val)
            emit('update:page', val)
        }
    })
    const pageSize = computed({
        get() {
            return props.limit
        },
        set(val){
            console.log('update:limit',val)
            emit('update:limit', val)
        }
    })
    const handleSizeChange = (val) =>{
        if (currentPage.value * val > props.total) {
            currentPage.value = 1
        }
        emit('pagination', { page: currentPage.value, limit: val })
    }
    const handleCurrentChange = (val) => {
        emit('pagination', { page: val, limit: pageSize.value })
    }

</script>      
<style>
    .page-contaner{
        background: #ffffff;
        padding: 10px 0;
        border: 1px solid #ecedee;
        padding-left: 10px;
    }
</style>