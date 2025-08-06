<script setup>
import {
  getCurrentInstance,computed
} from "vue";

const instance = getCurrentInstance();
const globalProperties = instance.appContext.config.globalProperties;

const props = defineProps({
  modelValue: {
    type: String,
    default: ""
  }
});

const emits = defineEmits(["update:modelValue"]);

/**清空选中的图标 */
function closeIcon() {
  emits("update:modelValue", "");
}
// 新增：检查是否是有效图标名
const isValidIcon = computed(() => {
  return props.modelValue && 
         props.modelValue !== "#" &&
         globalProperties.$icons.includes(props.modelValue);
});
</script>

<template>
  <el-popover trigger="click" :width="500">
    <template #reference>
      <el-button class="click-button" :icon="isValidIcon ? modelValue : null">
        {{ props.modelValue }}
        <p v-if="!isValidIcon" class="button-placeholder">点击选择图标</p>
        <el-icon @click.stop="closeIcon" v-if="modelValue && isValidIcon"  class="close-icon"
          ><CircleClose
        /></el-icon>
      </el-button>
    </template>
    <div class="el-icon-picker">
      <component
        v-for="icon in globalProperties.$icons"
        :key="icon"
        :class="[icon, 'icon', { 'icon-active': icon == props.modelValue }]"
        :is="icon"
        @click="emits('update:modelValue', icon)"
      >
      </component>
    </div>
  </el-popover>
</template>

<style scoped lang="scss">
.el-icon-picker {
  height: 256px;
  overflow-y: scroll;
  display: flex;
  flex-wrap: wrap;
}

.icon {
  display: inline-block;
  width: 24px;
  height: 24px;
  color: var(--el-text-color-regular);
  font-size: 20px;
  border-radius: 4px;
  cursor: pointer;
  text-align: center;
  line-height: 45px;
  margin: 5px;
}

.icon:hover {
  color: var(--el-color-primary);
}

.icon-active {
  color: var(--el-color-primary);
}
.click-button {
  width: 100%;
  position: relative;
}
::v-deep .el-button {
  justify-content: flex-start !important;
}
.button-placeholder {
  position: absolute;
  display: block;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: #a8abc3;
}
.close-icon {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
}
.el-button:focus,
.el-button:hover {
  background: #fff;
}
</style>