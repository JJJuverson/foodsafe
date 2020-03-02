<!-- <template>
	<el-breadcrumb separator-class="el-icon-arrow-right">
	  <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
	  <el-breadcrumb-item :to="{ path: '/news' }">热门新闻</el-breadcrumb-item>
	  <el-breadcrumb-item :to="{ path: '/blacklist' }">企业黑名单</el-breadcrumb-item>
	  <el-breadcrumb-item :to="{ path: '/cases' }">食品安全案例</el-breadcrumb-item>
	</el-breadcrumb>
</template>

<script>
	
</script> -->

<template>
	<el-tabs type="border-card">
	    <el-row>
		    <a href="/"><el-button type="success" plain>首页</el-button></a>
		    <a href="/news"><el-button type="success" plain>热门新闻</el-button></a>
		    <a href="/blacklist"><el-button type="success" plain>企业黑名单</el-button></a>
		    <a href="/cases"><el-button type="success" plain>食品安全案例</el-button></a>
	    </el-row>
	</el-tabs>
</template>
