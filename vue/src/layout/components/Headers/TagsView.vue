<template>
  <el-scrollbar>
    <div class="tagsview-contanter">
      <!-- 右键菜单 -->
      <div v-show="visibleMenu" class="contextmenu" :style="{left: left + 'px', top: top + 'px'}">
        <div class="menu-item" @click="refreshPage"><i class="el-icon-refresh"></i> 刷新页面</div>
        <div class="menu-divider"></div>
        <div class="menu-item" @click="closeCurrent">关闭当前</div>
        <div class="menu-item" @click="closeOthers">关闭其他</div>
        <div class="menu-item" @click="closeAll">全部关闭</div>
      </div>
      
      <template v-for="(tag, index) in visitedViews">
        <el-tag type="primary"  v-if="tag.path !=='/index'"
          :key="index"
          :class="isActive(tag) ? 'active' : ''"
          :to="{ path: tag.path, query: tag.query, fullPath: tag.fullPath}"
          @click="toTags(tag)"
          :style="activeStyle(tag)"
          effect="plain"
          @close="handleClose(tag,index)"
          closable
          @contextmenu.prevent="openMenu($event, tag)"
        >{{ tag.name }}
        </el-tag>
        <el-tag :key="index+1" type="primary" v-else
          :class="isActive(tag) ? 'active' : ''"
          :to="{ path: tag.path, query: tag.query, fullPath: tag.fullPath}"
          @click="toTags(tag)"
          :style="activeStyle(tag)"
          effect="plain"
          @contextmenu.prevent="openMenu($event, tag)"
        >
          {{ tag.name }}
        </el-tag>
      </template>
    </div>
  </el-scrollbar>
</template>

<script setup>
import { useRoute,useRouter } from 'vue-router';
import { ref, watch, onMounted,computed } from 'vue';
import useTagsViewStore from '@/stores/tags-view-store'

const scrollPaneRef = ref(null)
const router = useRouter()
const route = useRoute()
const tagsViewStore = useTagsViewStore() // 修改这里：调用store函数

// 右键菜单相关变量
const visibleMenu = ref(false)
const left = ref(0)
const top = ref(0)
const selectedTag = ref(null)

// 修改这里：使用store的状态
const visitedViews = computed(() => tagsViewStore.visitedViews);

function isActive(r) {
  return r.path === route.path
}

function activeStyle(tag) {
  if (!isActive(tag)) return {};
  return {
    "background-color": "#409EFF",
    "border-color": "#337ecc"
  };
}

const initTagsView = ()=>{
    const routes = {
      path:route.path,
      name:route.name,
      meta:route.meta,
      query:route.query,
      params:route.params,
      fullPath:route.fullPath
    }
    
    tagsViewStore.addVisitedView(routes) // 修改这里：使用store的方法
}

watch(route, 
    ()=>{
        initTagsView()
    },
    {deep:true, immediate:true}
)

const toTags = (tag)=>{
  router.push(tag.path)
}
const handleClose = (tag, index) => {
  tagsViewStore.removeVisitedView(tag);
  
  // 如果关闭的是当前激活的标签
  if (isActive(tag)) {
    // 如果还有其他标签
    if (visitedViews.value.length > 0) {
      // 尝试跳转到前一个标签（如果关闭的是最后一个标签）
      const newIndex = index >= visitedViews.value.length ? visitedViews.value.length - 1 : index;
      const lastView = visitedViews.value[newIndex];
      router.push(lastView.fullPath || lastView.path);
    } else {
      // 如果没有其他标签了，跳转到首页
      router.push('/index');
    }
  }
}


// 打开右键菜单
const openMenu = (e, tag) => {
  // 首页不能操作
  if (tag.path === '/index') return;
  // 设置菜单位置
  left.value = e.clientX;
  top.value = e.clientY;
  // 存储选中的标签
  selectedTag.value = tag;
  // 显示菜单
  visibleMenu.value = true;
}
// 点击其他地方关闭菜单
const closeMenu = () => {
  visibleMenu.value = false;
}

// 刷新页面 - 使用重定向方法
const refreshPage = () => {
  if (!selectedTag.value) return;
  
  // 重新加载当前页面
  if (isActive(selectedTag.value)) {
    // 使用重定向技术强制刷新页面
    const { fullPath } = selectedTag.value;
    router.replace({
      path: '/redirect' + fullPath,
      query: selectedTag.value.query
    }).then(() => {

    });
  }
  
  closeMenu();
}

// 关闭当前标签
const closeCurrent = () => {
  if (!selectedTag.value) return;
  // 查找当前标签在数组中的位置
  const index = visitedViews.value.findIndex(v => v.path === selectedTag.value.path);
  if (index !== -1) {
    handleClose(selectedTag.value, index);
  }
  
  closeMenu();
}

// 关闭其他标签
const closeOthers = () => {
  if (!selectedTag.value) return;
  
  // 调用 store 中的方法，只保留首页和当前选中的标签
  tagsViewStore.removeOthersViews(selectedTag.value); // 修改这里：使用store的方法
  
  // 如果当前激活的标签已经被关闭，则跳转到选中的标签
  if (!visitedViews.some(v => isActive(v))) {
    router.push(selectedTag.value.fullPath);
  }
  
  closeMenu();
}

// 关闭所有标签
const closeAll = () => {
  // 调用 store 中的方法，只保留首页
  tagsViewStore.removeAllViews(); // 修改这里：使用store的方法
  
  // 跳转到首页
  if (route.path !== '/index') {
    router.push('/index');
  }
  
  closeMenu();
}

// 点击页面其他地方关闭菜单
onMounted(() => {
  document.addEventListener('click', closeMenu);
});
</script>

<style>
.tagsview-contanter{
  display: flex;
  height: 38px;
  align-items:center;
  position: relative;
}
.tagsview-contanter .el-tag{
  margin-right: 5px;
  color: black;
  cursor: pointer;
}
.tagsview-contanter .el-tag .el-tag__close{
  color: black;
}
.tagsview-contanter .el-tag.active{
  color: #fff;
}
.tagsview-contanter .el-tag.active .el-tag__close{
  color: #fff;
}

/* 右键菜单样式 */
.contextmenu {
  position: fixed;
  z-index: 3000;
  background: white;
  border-radius: 4px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  padding: 5px 0;
  min-width: 130px;
  font-size: 13px;
}
.menu-item {
  padding: 8px 15px;
  cursor: pointer;
}
.menu-item:hover {
  background-color: #f0f7ff;
  color: #409eff;
}
.menu-divider {
  height: 1px;
  margin: 5px 0;
  background-color: #eaeefb;
}
</style>