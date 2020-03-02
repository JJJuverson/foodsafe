<template>
    <div class="cases-box">
	  <el-table :data="tableData" border stripe style="width: 100%" v-loading="loading">
		<el-table-column prop="pk" label="编号" width="150" align="center"></el-table-column>
		<el-table-column prop="fields.case_name" label="案件名称" width="280" align="center"></el-table-column>
		<el-table-column prop="fields.offender" label="犯罪人" width="100" align="center"></el-table-column>
		<el-table-column prop="fields.gender" label="性别" width="180" align="center"></el-table-column>
		<el-table-column prop="fields.age" label="年龄" width="150" align="center"></el-table-column>
		<el-table-column prop="fields.domicile" label="籍贯" width="150" align="center"></el-table-column>
		<el-table-column prop="fields.criminal_behavior" label="犯罪行为" width="300" align="center"></el-table-column>
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
		this.$axios.get("/api/cases/")
			.then(res =>{
				this.tableData = JSON.parse(res.data.data)

		}),
		this.loading = false
	} 
}
</script>

<style>
	.cases-box{
		margin-top: 20px;
	}
</style>
