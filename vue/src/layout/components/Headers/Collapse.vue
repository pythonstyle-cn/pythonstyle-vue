<template>
    <div class="fold-expand" @click="toogleFodeExpand">
        <el-icon v-if="!asideType"><Fold /></el-icon> 
        <el-icon v-else><Expand /></el-icon>
    </div>
</template>
<script setup>

    import useMenuStore from "@/stores/menu-permission"
    import { ref } from "vue"

    const menuStore = useMenuStore()
    
    const asideType = ref(false)
    const toogleFodeExpand = ()=>{
        menuStore.changeAsideType()
        asideType.value = menuStore.asideType
    }
    
</script>
<style>
    .fold-expand{
        font-size: 25px;
    }
    .fold-expand{
        cursor: pointer;
    }
</style>