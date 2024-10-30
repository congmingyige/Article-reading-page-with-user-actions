<template>
    <div id="Article" v-show="condition">
    <el-container>
        <el-main>
          <div>
            <el-row>
                <el-col :span="6" :offset="6">
                  <div class="headline-center-outer">
                    <h1 class="font-size-exlarge font-color-heavy headline-center-inner"> {{ title }} </h1>
                  </div>
                </el-col>
                <el-col :span="4" :offset="20">
                    这里放广告
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="12" :offset="6">
                  <div class="author">
                    <img src="../assets/logo.png" class="nav-usr" style="height:40px;">
                    <div style="position:relative; left:40px;">
                      <a class="font-size-small font-color-medium"> {{ author }} </a>
                      <div>
                        <span class="font-size-exsmall font-color-exlight">
                          {{ time }} 字数 {{ text_length }}  阅读 {{ views }} 评论 {{ comments_count }} 喜欢 {{ liked_count }} 收藏 {{ collection_count }}
                        </span>
                      </div>
                      <el-button-group>
                        <el-button type="text" v-bind:icon="like" @click="likedChange">点赞</el-button>
                        <el-button type="text" v-bind:icon="star" @click="starChange">收藏</el-button>

                        <el-button type="text" icon="el-icon-edit" v-show="modify" @click="articleUpdate">修改</el-button>
                        <el-button type="text" icon="el-icon-delete" v-show="modify" @click="articleDelete">删除</el-button>
                      </el-button-group>
                    </div>
                  </div>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="12" :offset="6">
                  <p id="article_text"></p>
                </el-col>
            </el-row>
          </div>

          <div>
            <el-row>
              <el-col :span="12" :offset="6" style="padding:0 0 0 3px;margin-bottom:10px;border-bottom-color:rgb(240,240,240); border-bottom-style:solid; border-bottom-width:0.9px; ">
                <div class="author">
                  <img src="../assets/logo.png" class="nav-usr" style="height:40px;">
                  <div style="text-align:center; margin-top:10px;">
                    <el-input
                      type="text"
                      :rows="2"
                      placeholder="请在此添加你的评论"
                      v-model="content"
                      style="position:relative; left:50px;">
                    </el-input>
                    <el-button type="primary" round style="display:inline; margin:10px 0 10px;" @click="commentCreate">提交</el-button>
                  </div>
                </div>
              </el-col>
            </el-row>

            <el-row>
              <el-col :span="24" style="text-align:center">
                <div class="rating">
                  <span class="font-size-small font-color-light text-align:center"> 请给这篇文章打个分吧 </span>
                  <el-rate
                    v-model="article_score"
                    :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                  </el-rate>
                </div>
              </el-col>
            </el-row>

            <span v-for="comment in author_comments">
              <Comment :comment_id="comment.id" :comment_author="comment.author" :comment_time="comment.time" :comment_content="comment.content"></Comment>
            </span>

            <span v-for="comment in comments">
              <Comment :comment_id="comment.id" :comment_author="comment.author" :comment_time="comment.time" :comment_content="comment.content"></Comment>
            </span>

            <el-row>
              <el-col :span="24" style="text-align:center">
                <el-button type="info" @click="commentLoad">加载更多</el-button>
                <el-button :span="24" type="info" @click="commentRefresh">加载刷新</el-button>
              </el-col>
            </el-row>

          </div>

        </el-main>

    </el-container>
  </div>
</template>

<script>
  import Comment from '../components/Comment'
  export default {
    components: {
        Comment,
    },
    name: 'Article',
    data() {
        return {
            condition: false,
            like: 'el-icon-circle-check-outline',
            star: 'el-icon-star-off',
            modify: false,
            title: '',
            author: '',
            time: '',
            text: '',
            views: '',
            comments_count: 0,
            liked_count: 0,
            collection_count: 0,
            text_length: 0,
            comments_number: 0,
            author_comments: [],

            comments: [],
            comment_id: '',
            comment_author: '',
            comment_time: '',
            comment_content: '',
            content: '',

            article_score: 0,

        }
    },
    mounted: function() {
        this.$nextTick(function() {
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + "/article",
                headers: {
                    'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                }
              }).then((response) => {
                if (response.body.code == "106") {
                    alert('文章不存在');
                    return;
                }
                this.condition = true;
                if (response.body.if_liked == 1)
                    this.like = 'el-icon-success';
                if (response.body.if_collection == 1)
                    this.star = 'el-icon-star-on';
                if (response.body.if_modify == 1)
                    this.modify = true;
                let article = response.body.article;
                this.title = article.title;
                this.author = article.author;
                this.time = article.time;
                this.text = article.text;
                this.views = article.views;
                this.comments_count = article.comments_count;
                this.liked_count = article.liked_count;
                this.collection_count = article.collection_count;
                this.text_length = this.text.length;
                document.getElementById('article_text').innerHTML = this.text;
              },
              (response) => {
                alert('数据传输失败');
                return;
            });
            this.commentLoad();
        })
    },
    methods: {
        commentLoad: function() {
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + "/comments",
                headers: {
                    'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                },
                body: {
                    'comments_number': this.comments_number
                }
              }).then((response) => {
                if (response.body.code == "106") {
                    alert('文章不存在');
                    return;
                }
                this.comments = this.comments.concat(response.body.article_comments);
                this.comments_number = response.body.comments_number;
              },
              (response) => {
                alert('数据传输失败');
            });
        },
        commentCreate: function () {
            if (this.content.length == 0) {
                alert('评论信息不能为空');
                return;
            }
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + "/c/create",
                headers: {
                    'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                },
                body: {
                    'content': this.content
                }
              }).then((response) => {
                if (response.body.code == '103') {
                    alert('用户不存在');
                    this.$router.push("/");
                    return;
                }
                if (response.body.code == '106') {
                    alert('文章不存在');
                    return;
                }
                let comment_new = {};
                let author_comments = [];
                comment_new['id'] = response.body.id;
                comment_new['author'] = this.$parent.get('username');
                comment_new['time'] = response.body.time;
                comment_new['content'] = this.content;
                author_comments = author_comments.concat(comment_new);
                this.author_comments = author_comments.concat(this.author_comments);
                this.comments_count = this.comments_count + 1;
                this.content = '';
              },
              (response) => {
                alert('数据传输失败');
              });
        },
        commentRefresh: function() {
            this.comments = [];
            this.author_comments = [];
            this.comments_number = 0;
            this.commentLoad();
        },
        articleLoad1: function () {
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article,
                headers: {
                    'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                }
              }).then((response) => {
                this.$parent.set('sessionKey', response.body.sessionKey, 1);
                if (response.body.code == "106") {
                    alert('文章不存在');
                    return;
                }
                this.condition = true;
                if (response.body.if_liked == 1)
                    this.like = 'el-icon-star-on';
                if (response.body.if_collection == 1)
                    this.star = 'el-icon-star-on';
                let article = response.body.article;
                this.title = article.title;
                this.author = article.author;
                this.time = article.time;
                this.text = article.text;
                this.views = article.views;
                this.comments_count = article.comments_count;
                this.liked_count = article.liked_count;
                this.collection_count = article.collection_count;
                this.text_length = this.text.length;
                document.getElementById('article_text').innerHTML = this.text;
                this.comments = response.body.article_comments;
              },
              (response) => {
                alert('数据传输失败');
            });
        },
        likedChange: function () {
            console.log(this.$parent.get('sessionKey'));
            if (this.like == "el-icon-circle-check-outline") {
                this.$http({
                    method: 'POST',
                    url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + '/liked',
                    headers: {
                        'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                    },
                  }).then((response) => {
                    if (response.body.code == '103') {
                        alert('用户不存在');
                        this.$router.push("/");
                        return;
                    }
                    if (response.body.code == '106') {
                        alert('文章不存在');
                        return;
                    }
                    if (response.body.code == '110') {
                        alert('错误请求');
                        return;
                    }
                    this.like = "el-icon-success";
                    this.liked_count = this.liked_count + 1;
                  },
                  (response) => {
                    alert('数据传输失败');
                  });
            }
            else {
                this.$http({
                    method: 'POST',
                    url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + '/not_liked',
                    headers: {
                        'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                    },
                  }).then((response) => {
                    if (response.body.code == '103') {
                        alert('用户不存在');
                        this.$router.push("/");
                        return;
                    }
                    if (response.body.code == '106') {
                        alert('文章不存在');
                        return;
                    }
                    if (response.body.code == '110') {
                        alert('错误请求');
                        return;
                    }
                    this.like = "el-icon-circle-check-outline";
                    this.liked_count = this.liked_count - 1;
                },
                (response) => {
                  alert('数据传输失败');
                });
            }
        },
        starChange: function () {
            if (this.star == "el-icon-star-off") {
                this.$http({
                    method: 'POST',
                    url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + '/collection',
                    headers: {
                        'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                    },
                  }).then((response) => {
                    if (response.body.code == '103') {
                        alert('用户不存在');
                        this.$router.push("/");
                        return;
                    }
                    if (response.body.code == '106') {
                        alert('文章不存在');
                        return;
                    }
                    if (response.body.code == '110') {
                        alert('错误请求');
                        return;
                    }
                    this.$parent.set('sessionKey', response.body.sessionKey, 1);
                    this.star = "el-icon-star-on";
                    this.collection_count = this.collection_count + 1;
                  },
                  (response) => {
                    alert('数据传输失败');
                });
            }
            else {
                this.$http({
                    method: 'POST',
                    url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + '/not_collection',
                    headers: {
                        'sessionKey': 'weep477idbab9ig004kbazppr77v2f0p'
                    },
                  }).then((response) => {
                    if (response.body.code == '103') {
                        alert('用户不存在');
                        this.$router.push("/");
                        return;
                    }
                    if (response.body.code == '106') {
                        alert('文章不存在');
                        return;
                    }
                    if (response.body.code == '110') {
                        alert('错误请求');
                        return;
                    }
                    this.star = "el-icon-star-off";
                    this.collection_count = this.collection_count - 1;
                  },
                  (response) => {
                    alert('数据传输失败');
                });
            }
        },
        articleUpdate: function () {
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + '/update',
                headers: {
                    'sessionKey': this.$parent.get('sessionKey')
                },
              }).then((response) => {
                if (response.body.code == '103') {
                    alert('用户不存在');
                    this.$router.push("/");
                    return;
                }
                if (response.body.code == '106') {
                    alert('文章不存在');
                    return;
                }
                if (response.body.code == '109') {
                    alert('无权限请求');
                    return;
                }
                alert('删除文章成功');
                this.condition = false;
              },
              (response) => {
                alert('数据传输失败');
            });
        },
        articleDelete: function () {
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/" + this.$route.params.id_article + '/delete',
                headers: {
                    'sessionKey': this.$parent.get('sessionKey')
                },
              }).then((response) => {
                if (response.body.code == '103') {
                    alert('用户不存在');
                    this.$router.push("/");
                    return;
                }
                if (response.body.code == '106') {
                    alert('文章不存在');
                    return;
                }
                if (response.body.code == '109') {
                    alert('无权限请求');
                    return;
                }
                alert('删除文章成功');
                this.condition = false;
              },
              (response) => {
                alert('数据传输失败');
            });
        }
    }
  }
</script>

<style>
   .el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
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
</style>
