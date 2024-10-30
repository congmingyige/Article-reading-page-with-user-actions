<template>
  <div id="ArticleDecorate">
    <el-input type="textarea" autorsize v-model="title" placeholder="title"> </el-input>
    <el-input type="textarea" autosize v-model="text" placeholder="text"> </el-input>
  </div>
</template>

<script>
    export default {
    name: 'ArticleDecorate',
    data() {
        return {
            title: '',
            text: '',
        }
    },
    methods: {
    }
}
</script>

<style>
    textarea.article {
    resize:none;
    width:500px;
    height:300px;
  }
</style>
