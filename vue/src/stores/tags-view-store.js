import { defineStore } from 'pinia'

const useTagsViewStore = defineStore(
  'tagsview', {
  //state 是 store 的数据 (data)
  state: () => ({
    visitedViews: [{
      path: '/index',
      name: '工作台'
    }],
    iframeViews: [],
    currentTags: {}
  }),
  actions: {
    addVisitedView(view) {
        if (this.visitedViews.some(v => v.name === view.name)){
          return
        }
        if (view.name == '工作台') {
          this.currentTags = {}
        } else {
          this.currentTags = view;
          this.visitedViews.push(view);
        }
    },
    removeVisitedView(view){
      let res = this.visitedViews.findIndex(item => item.name === view.name)
      this.visitedViews.splice(res, 1)
    },
    removeOthersViews(selectedTag) {
      const newViews = this.visitedViews.slice().filter(view => 
        view.path === '/index' || view.path === selectedTag.path
      );
      this.visitedViews = newViews;
    },
    removeAllViews() {
      this.visitedViews = this.visitedViews.filter(view => view.path === '/index');
      this.currentTags = {};
    },
  },
  //getters 是 store 的计算属性 (computed)
  getters: { 
    
  },
  
})


export default useTagsViewStore