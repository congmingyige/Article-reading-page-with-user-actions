<template>
  <div class="card2">
    <el-card class="card2">
      <el-row type="flex">
        <p class="topic-style">Starred Articles</p>
      </el-row>
      <el-row type="flex">
        <router-link to="/p/1"  class="ref-style">
        <p @click="stepintoarticle()" style="margin-top:10px;margin-bottom:5px;">{{article.title}}</p>
        </router-link>
      </el-row>
      <el-row type="flex" align="middle" >
          <img style="width:40px;height:40px;" src="../assets/logo.png">
          <p class="name-style">{{article.author}}</p>
      </el-row>
      <el-row>
        <el-col :span="1">
          <el-button type="text" style="height:40px;" icon="el-icon-star-off"></el-button>
        </el-col>
        <el-col :span="2">
        </el-col>
        <el-col :span="1">
          <el-button type="text" icon="el-icon-star-off"></el-button>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
  export default{
    name: 'articleCard',
    props:['article',],
    data (){
      return{
      }
    },
    method:{
      stepintoarticle () {
        this.$router.push('/1'+this.$router.article.id)
      },

    },
  }
</script>

<style>
  body {
  font-family: Helvetica, sans-serif;
  }
  .el-row {
  margin-bottom: 0px;
  &:last-child {
  margin-bottom: 0;
  }
  }
  .el-col {
  border-radius:3px;
  margin-bottom:0px;
  }
  .img{
  margin-top: 10px;
  margin-bottom: 5px;
  }
  .row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
  }
  .ywl-style
  {
  height:100%;
  margin-top:10%;
  width:100%;
  }
  .a-style
  {
  text-decoration:none;
  }
  .h4-style
  {
  margin-top:10px;
  margin-bottom:10px;
  margin-left:0px;
  }
  .font-size
  {
  font-size:14px;
  }
  .overflow-style
  {
  overflow:auto;
  height:800px;
  }
  .ref-style
  {
  color:black;
  font-weight:bold;
  text-decoration:none;
  font-size:larger;
  }
  .ref-style:hover
  {
  color:blue;
  }
  .overflow-style1
  {
  overflow:auto;
  height:600px;
  background-color:white;
  padding-top:0px;
  padding-bottom:0px;
  }
  .title-style{
    margin-left:10px;
    margin-bottom:0px;
    margin-top:0px;
    font-size:15px;
    padding-bottom:5px;
    color:#20a0ff;
  }
  .name-style{
    color:gray;
    font-weight:bolder;
    font-family:serif;
  }
  .card-style
  {
    padding-top:15px;
  }
  .el-card_body
  {
    padding-top:15px;
  }
  .font-size-exlarge{
  font-size:40px;
  }
  .font-size-large{
    font-size: 20px;
  }

  .font-size-medium{
    font-size: 15px;
  }

  .font-size-small{
    font-size:12px;
  }

  .font-size-exsmall{
    font-size:10px;
  }

  .font-color-exheavy{
    color:##000000//be careful when using it cuse it atrract too much attention
  }

  .font-color-heavy{
    color:#1a1a1a;
  }

  .font-color-medium{
    color:#404040;
  }

  .font-color-light{
    color:##595959;
  }

  .font-color-exlight{
    color:#999999;
  }

  .blcok-bottom-line{
    border-bottom-color:rgb(240,240,240);
    border-bottom-style:solid;
    border-bottom-width:0.9px;
  }

  .img-height{
    display: inline;
    height:100%;
  }

  .img-center{
    text-align:center;
  }


  .text-certer-outer{
    height:40px;
    width: 100%;
    margin: 20px auto 10px;
  }

  .text-center-inner{
    margin:0 auto;

  }
  .topic-style
  {
    color:gray;
    margin-top:0px;
    margin-bottom:0px;
  }
</style>
