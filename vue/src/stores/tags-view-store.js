import { defineStore } from 'pinia'
import { ref } from 'vue';

const useTagsViewStore = defineStore(
  'tagsview', {
  //state 是 store 的数据 (data)
  state: () => ({
    visitedViews: ref([{
      path: '/index',
      name: '首页'
    },]),
    iframeViews: [],
    currentTags :ref({})
  }),
  //actions 则是方法 (methods)
  actions: {
    addVisitedView(view) {
        if (this.visitedViews.some(v => v.name === view.name)){
          return
        }
        if (view.name == '首页') {
          this.currentTags.value = ''
        } else {
          this.currentTags.value = view;
          let result = this.visitedViews.some(val => val.name === view.name)
          result == false ? this.visitedViews.push(view) : 'no-name'
        }
    },
    removeVisitedView(view){
      // 删除选中项
      let res = this.visitedViews.findIndex(item => item.name === view.name)
      this.visitedViews.splice(res, 1)
      
    },
  },
  //getters 是 store 的计算属性 (computed)
  getters: { 
    
  },
  
})


export default useTagsViewStore