<template>

            <el-row>
                <el-menu :default-active="activeIndex" class="el-menu-demo;"  mode="horizontal">
                <el-row>
                    <el-col :span="8"  type="flex" justify="space-around">
                      <el-menu-item index="1" class="font-size-large">
                        <a src="www.baidu.com"><img src="../assets/logo.png" style="height:50px;" class="nav-logo"></a>
                      </el-menu-item>
                      <el-menu-item index="1" class="font-size-large">发现</el-menu-item>
                      <el-menu-item index="1" class="font-size-large">关注</el-menu-item>
                      <el-menu-item index="1" class="font-size-large">消息</el-menu-item>
                    </el-col>
                    <el-col :span="14">
                      <el-menu-item index="1">
                          <el-input>
                                placeholder="请输入想查找的内容"
                                icon="search"
                                v-model="input2"
                                :on-icon-click="handleIconClick">
                          </el-input>
                          <el-button type="primary">搜索</el-button>
                      </el-menu-item>
                    </el-col>
                    <el-col :span="2">
                      <div style="display:flex; display:-webkit-flex; align-items:center;">
                          <el-submenu index="2">
                              <template slot="title"><img src="../assets/logo.png" style="height:40px;"></template>
                              <el-menu-item index="2-1">我的主页</el-menu-item>
                              <el-menu-item index="2-2">设置</el-menu-item>
                              <el-menu-item index="2-3">退出</el-menu-item>
                          </el-submenu>
                      </div>
                    </el-col>
                </el-row>
                </el-menu>
            </el-row>
</template>

<script>
export default{
  name:'rootNav',
  data(){
    return{

    }
  },
}
</script>
<style>
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
  .bg-purple-dark {
  background: #99a9bf;
  }
  .bg-purple {
  background: #d3dce6;
  }
  .bg-purple-light {
  background: #e5e9f2;
  }
  .grid-content {
  border-radius: 4px;
  min-height: 36px;
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
  .title-style
  {
    margin-left:10px;
    margin-bottom:0px;
    margin-top:0px;
    font-size:15px;
    padding-bottom:5px;
    color:#20a0ff;

  }
  .name-style
  {
    margin-bottom:0px;
    margin-top:3px;
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

.footer{
  height:200px;
  background-color:#4d79ff;
  color: #ffffff;
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
