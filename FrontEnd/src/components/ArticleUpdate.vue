<template>
  <div id="ArticleUpdate">
    <ArticleDecorate ref="article_decorate"></ArticleDecorate>
    <el-button @click="articleUpdate">确定</el-button>
  </div>
</template>

<script>
    import ArticleDecorate from '../components/ArticleDecorate'
    export default {
        components: {
            ArticleDecorate,
        },
        name: 'ArticleUpdate',
        data() {
            this.articleGet();
            return {
        }
    },
    methods: {
        articleGet: function() {
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/"+this.$route.params.id_article+"/article_title_text",
                headers: {
                    'sessionKey': this.$parent.get('sessionKey')
                },
              }).then((response) => {
                if (response.body.code == '103') {
                    this.$router.push("/");
                    return;
                }
                if (response.body.code == '105') {
                    alert('修改后文章重复');
                }
                if (response.body.code == '106') {
                    alert('文章不存在');
                    return;
                }
                if (response.body.code == '109') {
                  alert('无权限修改文章');
                  return;
                }
                this.$refs.article_decorate.title = response.body.title;
                this.$refs.article_decorate.text = response.body.text;
              },
              (response) => {
                alert('数据传输失败');
            });
        },
        articleUpdate: function () {
            let title = this.$refs.article_decorate.title;
            if (title.length == 0) {
                alert("标题不能为空");
                return;
            }
            let text = this.$refs.article_decorate.text;
            if (text.length == 0) {
                alert("内容不能为空");
                return;
            }
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/p/"+this.$route.params.id_article+"/update",
                headers: {
                    'sessionKey': this.$parent.get('sessionKey')
                },
                body: {
                    title: title,
                    text: text,
                }
              }).then((response) => {
                if (response.body.code == '103') {
                  alert('用户不存在');
                  this.$router.push("/");
                  return;
                }
                if (response.body == '106') {
                    alert('文章不存在');
                    return;
                }
                if (response.body == '105') {
                    alert('同名文章存在');
                    return;
                }
                if (response.body.code == '109') {
                    alert('无权限请求');
                    return;
                }
                alert('更新文章成功');
                this.$router.push("/p/" + this.$route.params.id_article);
              },
              (response) => {
                  alert('数据传输失败');
            });
        }
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
