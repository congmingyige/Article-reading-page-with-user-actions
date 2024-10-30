<template>
  <div id="ArticleOpen" v-show="condition">

    <ArticleSingle ref="article"></ArticleSingle>

    <!--
    <span v-for="comment in comments">
      <Comment :comment_id="comment[0]" :comment_author="comment[1]+comment[2]" :comment_time="comment[3]" :comment_content="comment[4]"></Comment>
    </span>
    -->

  </div>
</template>

<script>
  import ArticleSingle from '../components/Article'

  export default {
    components: {
      ArticleSingle,
    },
    name: 'ArticleOpen',
    data() {
      this.articleOpen();
      return {
        condition: false,

        /*
        comments: '',
        comment_id: '',
        comment_time: '',
        comment_content: ''
        */
      }
    },
    methods: {
      articleOpen: function() {
        this.$http.post("http://127.0.0.1:8005/p/"+this.$route.params.id_article)
                  .then((response) => {
                      if (response.body == "106") {
                        alert('文章不存在');
                        return;
                      }
                      this.condition = true;
                      var article=response.body.article[0];
                      this.$refs.article.title = article[0];
                      if (article[2] == null)
                        this.$refs.article.author = article[1];
                      else
                        this.$refs.article.author = article[2];
                      this.$refs.article.time = article[3];
                      this.$refs.article.text = article[4];
                      this.$refs.article.views = article[5];
                      this.$refs.article.liked = article[6];
                      this.$refs.article.text_length = this.$refs.article.text.length;
                      this.$refs.article.setText();

                      var comments = response.body.article_comments;
                      console.log(comments);
                      this.$refs.article.comment_count = comments.length;
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
