<template>
    <div class="black-box">
	  <el-table :data="tableData" border stripe style="width: 100%" v-loading="loading">
		<el-table-column prop="pk" label="编号" width="150" align="center"></el-table-column>
		<el-table-column prop="fields.enterprise_name" label="公司名称" width="280" align="center"></el-table-column>
		<el-table-column prop="fields.legal_rep" label="法定人" width="100" align="center"></el-table-column>
		<el-table-column prop="fields.punishment" label="惩罚" width="400" align="center"></el-table-column>
		<el-table-column prop="fields.criminal_behavior" label="犯罪行为" width="400" align="center"></el-table-column>
	  </el-table>
	  <div style="text-align:center;margin: 10px 0;">
	  	<el-pagination background layout="prev, pager, next" :total="10"></el-pagination>
	  </div>
	</div>
</template>

<script>
  export default {
    data() {
      return {
        loading: false,
        tableData: [],
      }
    },
	
	created() {
		this.loading = true,
		this.$axios.get("/api/blacklist/")
			.then(res =>{
				this.tableData = JSON.parse(res.data.data)

		}),
		this.loading = false
	} 
}
</script>

<style>
	.black-box{
		margin-top: 20px;;
	}
</style>
