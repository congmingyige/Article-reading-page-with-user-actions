<template>
    <div id="Comment_create">
      <el-row>
        <el-tag>文章评论</el-tag>
        <el-button type="primary" icon="el-icon-plus"></el-button>
      </el-row>
      <el-input type="textarea"></el-input>
    </div>
</template>

<script>
  export default {
    name: 'Comment_create',
    data() {
      return {
      }
    },
    method: {
    }
  }
</script>

<style>
  #Comment_create {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
