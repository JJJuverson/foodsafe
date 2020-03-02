<template>
	<div class="time-line">		
		  <el-timeline :reverse="reverse">
		    <el-timeline-item
		      v-for="(activity, index) in activities"
		      :key="index"
		      :timestamp="activity.timestamp">
			  <p>{{ activity.fields.news_time }}</p>
			  <el-card class="box-card">
			    <div slot="header" class="clearfix">
			      <span>{{ activity.fields.news_name }}</span>
			    </div>
				{{ activity.fields.content }}
				<div class="newsfooter">
				            <p>
				              来源:<span class="origin">{{ activity.fields.news_source }}</span>
				            </p>
				          </div>
			  </el-card>
		    </el-timeline-item>
		  </el-timeline>
		</div>
	</div>
</template>



<script>
  export default {
    data() {
      return {
        reverse: true,
        activities: []
      };
    },
	created(){
		this.loading = true,
		this.$axios.get("/api/news/")
			.then(res =>{
				this.activities = JSON.parse(res.data.data)
			})
    }
}
</script>

<style scoped>
	.time-line{
		margin-top: 20px;
	}
	.newsfooter{
	    display: flex;
	    justify-content: space-between;
	    font-size: 12px;
	}
	/* .area{
	    padding-left: 5px;
	} */
	.origin{
	    color: #6C63FF;
	    padding-left: 5px;
	}
</style>