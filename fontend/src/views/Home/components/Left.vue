<template>
	<el-menu
        :default-active="activeIndex"
        class="el-menu-vertical-demo"
        background-color="#333"
        text-color="#fff"
        active-text-color="#ffd04b"
        :collapse="iscollapse"
        router  
        >
        <el-menu-item index="1" route="/">
          <i class="el-icon-setting"></i>
          <span slot="title">首&nbsp;&nbsp;&nbsp;页</span>
        </el-menu-item>        
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>食品安全管理</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="news" route="/news">热门新闻</el-menu-item>
            <el-menu-item index="blacklist" route="/blacklist">企业黑名单</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-menu-item index="cases" route="/cases">
          <i class="el-icon-menu"></i>
          <span slot="title">食品安全案例</span>
        </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data () {
    return {
      iscollapse: false,
      activeIndex:"1"
    }
  }
}
</script>
