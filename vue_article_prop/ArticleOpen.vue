<template>
  <div id="ArticleOpen" v-show="condition">
    <ArticleSingle :title="title" :author="author" :time="time" :text="text" :views="views" :liked="liked"></ArticleSingle>
    <CommentCreate></CommentCreate>

    <span v-for="comment in comments">
      <Comment :comment_id="comment[0]" :comment_author="comment[1]+comment[2]" :comment_time="comment[3]" :comment_content="comment[4]"></Comment>
    </span>
  </div>
</template>

<script>
  import ArticleSingle from '../components/Article'
  import Comment from '../components/Comment'
  import CommentCreate from '../components/CommentCreate'

  export default {
    components: {
      ArticleSingle,
      Comment,
      CommentCreate
    },
    name: 'ArticleOpen',
    data() {
      this.ArticleOpen();
      return {
        condition: false,
        title: '',
        author: '',
        time: '',
        text: '',
        views: '',
        liked: '',
        comments: '',
        comment_id: '',
        comment_time: '',
        comment_content: ''
      }
    },
    methods: {
      ArticleOpen: function() {
        document.cookie="username"+"="+"chen"+";";
        this.$http.post("http://127.0.0.1:8005/p/"+this.$route.params.id_article.toString())
                  .then((response) => {
                      if (response.body == "106") {
                        alert('文章不存在');
                        return;
                      }
                      this.condition = true;
                      var article=response.body.article[0];
                      this.title = article[1];
                      if (article[3] == null)
                        this.author = article[2];
                      else
                        this.author = article[3];
                      this.time = article[4];
                      this.text = article[5];
                      this.views = article[6];
                      this.liked = article[7];
                      var comments = response.body.article_comments;
                      //this.comments = comments;
                      //console.log(this.comments);
                      //console.log(response['headers']);
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
</style>
