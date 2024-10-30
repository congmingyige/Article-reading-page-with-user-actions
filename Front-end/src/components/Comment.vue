<template>
  <div id="Comment">
    <el-row>
      <el-col :span="12" :offset="6">
        <div class="author">
          <img src="../assets/logo.png" class="nav-usr" style="height:40px;">
          <div style="position:relative; left:40px;">
            <a style="font-size:14px;line-height:1.5"> {{ comment_author }} </a>
            <div>
              <span class="font-size-exsmall font-color-light"> {{ comment_time }} </span>
            </div>
          </div>
        </div>
        <div class="font-size-small font-color-medium">
          <p> {{ comment_content }} </p>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    export default {
        props: ['comment_id', 'comment_author', 'comment_time', 'comment_content'],
        name: 'Comment',
        data(){
            return {
            }
        },
        methods: {

        }
    }
</script>

<style>
.font-size-small{
  font-size:12px;
}
  .font-size-exsmall{
  font-size:10px;
}
  .font-color-medium{
  color:#404040;
}
  .font-color-light{
  color:##595959;
}
</style>
