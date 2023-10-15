<script lang="ts">
import { toggleDark } from "~/composables";

export default{
  data(){
    return {
      isLogin: false,
    }
  }
}
</script>

<template>
  <el-menu class="el-menu-demo" mode="horizontal" :router="true">
    <el-menu-item index="/">Home</el-menu-item>
    <el-sub-menu index="2">
      <template #title>Workspace</template>
      <el-menu-item index="2-1">Workspace - 1</el-menu-item>
      <el-menu-item index="2-2">Workspace - 2</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      <el-sub-menu index="2-5">
        <template #title>New Workspace</template>
        <el-menu-item index="2-5-1-1">new item one</el-menu-item>
      </el-sub-menu>
      </el-sub-menu>
    </el-sub-menu>
    <el-menu-item index="3" disabled>Info</el-menu-item>
    <el-menu-item index="/feedback">Feedback</el-menu-item>
    <el-menu-item h="full" @click="toggleDark()">
      <button
        class="border-none w-full bg-transparent cursor-pointer"
        style="height: var(--ep-menu-item-height)"
      >
        <i inline-flex i="dark:ep-moon ep-sunny" />
      </button>
    </el-menu-item>
    <el-menu-item v-if="isLogin">
      logout
    </el-menu-item>
    
  </el-menu>
</template>
