<template>
  <div style="background-color:#333;display:flex;align-items:center;justify-content:space-between;">
      <div style="color:#fff;">LOGO</div>
      <el-menu
        class="el-menu-demo"
        mode="horizontal"
        background-color="#333" 
        text-color="#fff"
        active-text-color="#ffd04b">
		   <el-menu-item index="1" style="padding: 0;">
				 <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
				   <el-select v-model="select" slot="prepend" placeholder="请选择">
					 <el-option label="餐厅名" value="1"></el-option>
					 <el-option label="订单号" value="2"></el-option>
					 <el-option label="用户电话" value="3"></el-option>
				   </el-select>
				   <el-button slot="append" icon="el-icon-search"></el-button>
				 </el-input>
		   </el-menu-item>
	   </el-menu>
    </div>
</template>

<script>

export default {
	components:{
		
	},
	data() {
	    return {
	      input3: '',
	      select: ''
	    }
	  }
}
</script>


