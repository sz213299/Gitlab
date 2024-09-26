<template>
    <div class="app-wrapper">
      <el-container>
        <el-aside width="200px" class="sidebar-container"> <Menu/> </el-aside>
        <el-container>
          <el-header> <Header/> </el-header>
          <el-main> <Tabs/> </el-main>
          <el-footer> <Footer/> </el-footer>
        </el-container>
      </el-container>
    </div>
  </template>

<script setup>
import Menu from '@/layout/menu' //最左侧导航栏
import Footer from '@/layout/footer' //底部
import Tabs from '@/layout/tabs'  // 中间
import Header from '@/layout/head'  // 顶部

</script>
<!-- <style scoped> 是 Vue 单文件组件（SFC）中用来限制 CSS 样式作用范围的一种方式。
    它的作用是使当前组件的样式只作用于组件自身，而不会影响到其他组件，避免了全局样式冲突的问题。 -->
<style scoped>
.app-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
}

.sidebar-container {
  background-color: #2d3a4b;
  height: 100%;
}

.el-container {
  height: 100%
}

.el-header {
  padding-left: 0px;
  padding-right: 0px;
}

:deep(ul.el-menu) {
  border-right-width: 0px
}
</style>