<template>
    <div id="Comment">
      <el-row>
        <el-tag>作者</el-tag>
        <el-tag :span="20"> {{ comment_author }} </el-tag>
        <el-tag>时间</el-tag>
        <el-tag :span="20"> {{ comment_time }} </el-tag>
        <el-button type="primary" icon="el-icon-delete" v-show="comment_delete"></el-button>
      </el-row>
      <el-input type="textarea"> {{ comment_content }} </el-input>
    </div>
</template>

<script>
export default {
  name: 'Comment',
  props: ['comment_id', 'comment_author', 'comment_time', 'comment_content'],
  data() {
    return {
      comment_delete: true
    }
  }
}
</script>

<style>
  #Comment {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

</style>
