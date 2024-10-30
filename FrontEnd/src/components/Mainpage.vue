<template>
    <div class="Mainpage" >
      <el-row>
        <el-col :span="2">
          <el-button type="text" class="title-style el-icon-view"> 我的关注</el-button>
        </el-col>
        <el-col :span="1">
          <el-button type="text" class="el-icon-plus"> 添加关注</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="4">
          <el-menu mode="vertical" default-active="1" class="el-menu-vertical-demo" >
            <el-menu-item-group title="" class="overflow-style1">
              <el-menu-item index="1">
                <i class="el-icon-document"></i>简友圈
              </el-menu-item>
              <el-menu-item index="2">
                <i class="el-icon-star-on"></i>程序员
              </el-menu-item>
              <el-menu-item index="3">
                <i class="el-icon-date"></i>前端基础类学习
              </el-menu-item>
              <el-menu-item index="4">
                <i class="el-icon-message"></i>拯救地球一号
              </el-menu-item>
              <el-menu-item index="4">
                <i class="el-icon-message"></i>手绘
              </el-menu-item>
              <el-menu-item index="5">
                <i class="el-icon-message"></i>人物
              </el-menu-item>
              <el-menu-item index="6">
                <i class="el-icon-message"></i>城市故事
              </el-menu-item>
              <el-menu-item index="7">
                <i class="el-icon-message"></i>简书电影
              </el-menu-item>
              <el-menu-item index="8">
                <i class="el-icon-message"></i>旅行
              </el-menu-item>
              <el-menu-item index="9">
                <i class="el-icon-message"></i>历史
              </el-menu-item>
              <el-menu-item index="10">
                <i class="el-icon-message"></i>故乡
              </el-menu-item>
            </el-menu-item-group>
          </el-menu>
        </el-col>
        <el-col :span="14">
          <div class ="block2">
            <el-tabs v-model="activeName2" type="border-card" text-color="black">
              <el-tab-pane label="今日推荐" name="first" class="overflow-style">
                <div>
                  <el-card body-style="padding-top:15px;">
                    <div class ="person1">
                      <el-row :span ="1">
                        <el-col :span="4">
                          <p class="topic-style">
                            来自话题:xxxxx
                          </p>
                        </el-col>
                      </el-row>
                      <el-row>
                        <el-row>
                          <el-col :span="8">
                            <router-link to="/p/1" class="ref-style">
                            <p style="margin-top:10px;margin-bottom:5px;" >如何评价电影敦刻尔克</p>
                            </router-link>
                          </el-col>
                        </el-row>
                        <el-row :span="4">
                          <el-col :span="3">
                            <p class="name-style"> 作者:杨万里</p>
                          </el-col>
                        </el-row>
                        <div>
                              《敦刻尔克》，本身是个历史名词，且有珠玉在前；好比中国人听《四渡赤水》，结果已经知道，并无悬念。
                              照着史实硬拍，就成科教纪录片了。诺兰自然也明白。所以他想了个法子保留悬念，那就是：本片与其说是战争片，不如说是悬疑片。
                              我们知道历史上40万英法联军最后成功撤出了33万人，知道这次大撤退某种程度上挽救了欧洲，保留了二战西线的火种，某种程度上拯救了英国与法国。
                              宏伟的结果没有悬念。
                        </div>
                      </el-row>
                      <el-row>
                        <el-col :span="1">
                          <el-button  type="text" icon="edit">
                          </el-button>
                        </el-col>
                        <el-col :span ="2" >
                        </el-col>
                        <el-col :span="1">
                          <el-button type="text" icon="share"></el-button>
                        </el-col>
                        <el-col :span="2">
                        </el-col>
                        <el-col :span="1">
                          <el-button type="text" icon="star-off"></el-button>
                        </el-col>
                      </el-row>
                    </div>
                  </el-card>
                </div>

                <div>
                  <p></p>
                </div>
                <div class="card2">
                  <el-card class="card2" body-style="padding-top:15px;">
                    <el-row>
                      <el-col :span="4">
                        <p class="topic-style">
                            来自话题:xxxxx
                        </p>
                      </el-col>
                    </el-row>
                    <el-row>
                      <el-col :span="6">
                        <router-link to="/p/2"  class="ref-style">
                        <p style="margin-top:10px;margin-bottom:5px;">敦刻尔克是否是诺兰导演迄今最烂的作品</p>
                        </router-link>
                      </el-col>
                    </el-row>
                    <el-row>
                       <el-col :span="3">
                        <p class="name-style">作者:郑川</p>
                      </el-col>
                    </el-row>
                    <el-row>
                      <el-col :span="1">
                        <el-button  type="text" icon="edit">
                        </el-button>
                      </el-col>
                      <el-col :span ="2" >
                      </el-col>
                      <el-col :span="1">
                        <el-button type="text" icon="share"></el-button>
                      </el-col>
                      <el-col :span="2">
                      </el-col>
                      <el-col :span="1">
                        <el-button type="text" icon="star-off"></el-button>
                      </el-col>
                    </el-row>
                  </el-card>
                </div>
                <div>
                  <p></p>
                </div>
                <div class="card3">
                  <el-card class="card3" body-style="padding-top:15px;">
                    <el-row :span="4">
                     <p class="topic-style">来自话题:xxxxxxx</p>
                    </el-row>
                    <el-row>
                      <el-col :span="6" >
                       <router-link to="/p/3" class="ref-style">
                        <p style="margin-top:10px;margin-bottom:5px;">敦刻尔克是否是诺兰导演迄今最烂的作品</p>
                       </router-link>
                      </el-col>
                    </el-row>
                      <el-row>
                      <el-col :span="3">
                        <p class="name-style">作者:陈冠斌</p>
                      </el-col>
                      </el-row>
                    <el-row>
                      <el-col :span="1">
                        <el-button  type="text" icon="edit">
                        </el-button>
                      </el-col>
                      <el-col :span ="2" >
                      </el-col>
                      <el-col :span="1">
                        <el-button type="text" icon="share"></el-button>
                      </el-col>
                      <el-col :span="2">
                      </el-col>
                      <el-col :span="1">
                        <el-button type="text" icon="star-off"></el-button>
                      </el-col>
                    </el-row>
                  </el-card>
                </div>
              </el-tab-pane>
              <el-tab-pane label="相关推荐" name="second" class="overflow-style">
                <div class="card4">
                  <el-card class="card4">
                    <el-row>
                      <el-col :span="6">
                      </el-col>
                    </el-row>
                  </el-card>
                </div>
              </el-tab-pane>

            </el-tabs>
          </div>
        </el-col>
      </el-row>
      </div>
</template>
<script>
export default {
  name: 'Mainpage',
  components: {
  },
  data () {
    console.log(this.$parent.get('username'));
    console.log(this.$parent.get('sessionKey'));
    return {
      activeIndex: '1',
      activeName2: 'first',
      input: '',
      input2: ''
    }
  },
  methods: {
    startHacking () {
      this.$notify({
        title: 'It Works',
        message: 'We have laid the groundwork for you. Now it is your time to build something epic!',
        duration: 6000
      })
    },
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    handleIconClick() {

    },
    open () {
      this.$alert('这是一段内容', '标题名称', {
        confirmButtonText: '确定',
        callback: action => {
          this.$message({
            type: 'info',
            message: `action: ${action}`
          })
        }
      })
    }
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
  /*
  .ul::-webkit-scrollbar{
    width:5px;
    height:initial;
  }
  .ul::-webkit-scrollbar-track-piece{
    background-color:#f2f2f2;
  }
  .ul::-webkit-scrollbar-thumb{
    background-color:#c3ccd5;
    border-radius:20px;
  }*/

</style>

