<template>
  <el-scrollbar>
    <div class="tagsview-contanter">
        <template v-for="(tag, index) in visitedViews" >
        <el-tag type="primary" v-if="tag.path !=='/index'"
          :key="index"
          :class="isActive(tag) ? 'active' : ''"
          :to="{ path: tag.path, query: tag.query, fullPath: tag.fullPath}"
          @click="toTags(tag)"
          :style="activeStyle(tag)"
          effect="plain"
          @close="handleClose(tag,index)"
          closable
        >{{ tag.name }}
        </el-tag>
        <el-tag :key="index+1" type="primary" v-else
          :class="isActive(tag) ? 'active' : ''"
          :to="{ path: tag.path, query: tag.query, fullPath: tag.fullPath}"
          @click="toTags(tag)"
          :style="activeStyle(tag)"
          effect="plain"
        >
          {{ tag.name }}
        </el-tag>
      </template>
    </div>
  </el-scrollbar>
</template>
<script setup>
import { useRoute,useRouter } from 'vue-router';
import { ref, watch } from 'vue';
import useTagsViewStore from '@/stores/tags-view-store'

const scrollPaneRef = ref(null)

const router = useRouter()
const route = useRoute()

const useTagsView = useTagsViewStore()

const visitedViews = useTagsView.visitedViews;

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
    
    useTagsView.addVisitedView(routes)
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
  
  let length = visitedViews.length - 1;
  
  useTagsView.removeVisitedView(tag)

  if (index === length) {
      router.push({
          name: visitedViews[index - 1].name,
      });
  } else {
      router.push({
          name: visitedViews[index].name,
      });
    }
}

</script>
<style>
.tagsview-contanter{
  display: flex;
  height: 38px;
  align-items:center;
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
</style>