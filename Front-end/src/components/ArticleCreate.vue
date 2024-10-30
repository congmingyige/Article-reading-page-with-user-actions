<template>
  <div id="ArticleCreate">
    <ArticleDecorate ref="article_decorate"></ArticleDecorate>
    <el-button @click="articleCreate">确定</el-button>
  </div>
</template>

<script>
    import ArticleDecorate from '../components/ArticleDecorate'
    export default {
        components: {
            ArticleDecorate,
        },
        name: 'ArticleCreate',
        data() {
            return {
            }
        },
        methods: {
            articleCreate: function () {
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
                    url: "http://127.0.0.1:8005/p/create",
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
                    if (response.body.code == '105') {
                        alert('文章重复');
                        return;
                    }
                    alert('创建文章成功');
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
