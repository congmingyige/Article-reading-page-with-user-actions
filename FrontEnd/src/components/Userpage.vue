<template>
  <div class="Userpage">

      <el-container>
        <el-card class="usrCard">
          <el-row :gutter="20">
            <el-col :span="4">
              <div class="userImg"><img src="../assets/logo.png"></div>
            </el-col>
            <el-col :span="20">
              <el-row type="flex" align="center">
                <el-col :span="6"><p class="font-size-exlarge" style="color:#000000; font-weight:bold;">User Name</p></el-col>
                <el-col :span="10"><p class="font-size-exlarge"> {{ author_name }} </p></el-col>
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
          <el-tabs v-model="activeName">
            <el-tab-pane label="My Stars" name="first">
              <div v-for="article in starredArticles">
                <articleCard :article="article" :type='starred'></articleCard>
              </div>
            </el-tab-pane>
            <el-tab-pane label="My Thumb Up" name="second">
              <div v-for="article in thumbedArticles">
                <articleCard :article="article" :type='thumbed'></articleCard>
              </div>
            </el-tab-pane>
          </el-tabs>
        </el-main>
        <el-aside width="400px">广告</el-aside>
      </el-container>
  </div>
</template>

<script>

    import ArticleCard from '../components/ArticleCard'
    export default {
    name: 'Userpage',
    components: {
        ArticleCard,
    },
    data () {
        return {
            activeName: 'first',
            starred: 'starred',
            thumbed: 'thumbed',
            starredArticles: [],
            thumbedArticles: [],
            article: '',
            author_name: ''
        }
    },
    mounted: function() {
        //分两次获得数据：让用户尽快看到必要的数据；暂时不必要的数据也传送过来，避免后面用户的干等，影响用户体验
        //starredArticles
        this.$http({
            method: 'POST',
            url: "http://127.0.0.1:8005/a/" + this.$route.params.id_author + "/collection",
            headers: {
                'sessionKey': this.$parent.get('sessionKey')
            }
          }).then((response) => {
            console.log(this.$route.params.id_author);
            if (response.body.code == "103") {
                alert('文章不存在');
                return;
            }
            this.starredArticles = response.body.article;
            this.author_name = response.body.author_name;
          },
          (response) => {
            alert('数据传输失败');
          });
          //thumbedArticles
          this.$http({
              method: 'POST',
              url: "http://127.0.0.1:8005/a/" + this.$route.params.id_author + "/liked",
              headers: {
                  'sessionKey': this.$parent.get('sessionKey')
              }
            }).then((response) => {
              if (response.body.code == "103") {
                  alert('文章不存在');
                  return;
              }
              this.thumbedArticles = response.body.article;
            },
            (response) => {
              alert('数据传输失败');
            });
    },
    methods: {

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
