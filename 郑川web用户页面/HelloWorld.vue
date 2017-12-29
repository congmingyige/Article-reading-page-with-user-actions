<template>
  <div class="hello">

      <el-container>
        <el-card class="usrCard">
          <el-row :gutter="20">
            <el-col :span="4">
              <div class="userImg"><img src="../assets/logo.png"></div>
            </el-col>
            <el-col :span="20">
              <el-row type="flex" align="center">
                <el-col :span="6"><p class="font-size-exlarge" style="color:#000000; font-weight:bold;">User Name</p></el-col>
                <el-col :span="10"><p class="font-size-exlarge">User Name</p></el-col>
              </el-row>
              <el-row>
                <el-col :span="3"><p class="font-size-large" style="color:#000000; font-weight:bold;">居住地</p></el-col>
                <el-col :span="6"><p class="font-size-large" style="color:#000000; font-weight:bold;">现居西安</p></el-col>
              </el-row>
              <el-row>
                <el-col :span="3"><p style="color:#000000; font-weight:bold;">所在行业</p></el-col>
                <el-col :span="6"><p style="color:#000000; font-weight:bold;">互联网</p></el-col>
              </el-row>
              <el-row>
                <el-col :span="3"><p style="color:#000000; font-weight:bold;">教育经历</p></el-col>
                <el-col :span="6"><p style="color:#000000; font-weight:bold;">兰州大学 · 计算机科学</p></el-col>
              </el-row>
              <el-row>
                <el-col :span="3"><p style="color:#000000; font-weight:bold;">个人简介</p></el-col>
                <el-col :span="6"><p style="color:#000000; font-weight:bold;">越不会讲话就越去讲，然后就会了。</p></el-col>
              </el-row>
            </el-col>
          </el-row>
        </el-card>
      </el-container>






      <el-container>
        <el-main>
          <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="My Stars" name="first">
              <div v-for="starredArticle in starredArticles">
                <articleCard :article="starredArticle"></articleCard>
              </div>
            </el-tab-pane>
            <el-tab-pane label="My Thumb Up" name="second">
            </el-tab-pane>
          </el-tabs>
        </el-main>
        <el-aside width="400px">Aside</el-aside>
      </el-container>
  </div>
</template>

<script>
import articleCard from './articleCard'
export default {
  name: 'HelloWorld',
  components: {
    articleCard,
  },
  data () {
    return {

      activeName: 'first',
      starredArticle:[],
      thumbedArticle:[]
    }
  },
  created:function (){
    this.methods.loadResource()
  },
  methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },
      loadResource(){
        temp:{
          starredArticle,
          thumbedArticle
        }
        let request_body = JSON.stringify(temp);
        this.$http.post('/userPanel',request_body)
            .then((responce)=>{
              this.articles = responce.body.articles
              console.log(articles)
            },(responce)=>{
              console.log('responce failed!')
            })
            .catch((responce)=>{
              console.log('error ocurred during the process!')
            });
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.usrCard{
  width: 100%;
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
color:#000000 !important//be careful when using it cuse it atrract too much attention

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

</style>
