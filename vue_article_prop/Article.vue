<template>

  <div id="Article">

    <el-row :gutter="50">
      <el-tag> {{ title }} </el-tag>
    </el-row>

    <el-row :gutter="50">
      <el-tag :span="20"> {{ author }} </el-tag>
      <el-tag :span="20"> {{ time }} </el-tag>
    </el-row>

    <el-input type="textarea"> {{ text }} </el-input>

     <el-button-group>
      <el-button type="primary" icon="el-icon-edit"></el-button>
      <el-button type="primary" icon="el-icon-delete"></el-button>
      <el-button type="primary" v-bind:icon='star' @click="star_mode"></el-button>
     </el-button-group>

    <el-row :gutter="50">
      <el-tag :span="10"> views </el-tag>
      <el-tag :span="10"> {{ views }} </el-tag>
      <el-tag :span="10"> liked </el-tag>
      <el-tag :span="10"> {{ liked }} </el-tag>
      <el-button type="primary" icon="el-icon-arrow-down" @click="not_liked_change"></el-button>
      <el-button type="primary" icon="el-icon-arrow-up" @click="liked_change"></el-button>

    </el-row>
  </div>

</template>

<script>
export default {
  name: 'Article',
  props: ['title', 'author', 'time', 'text', 'views', 'liked'],
  data() {
    return {
        star: 'el-icon-star-off'
    }
  },
  methods: {
    star_mode: function() {
      if (this.star == "el-icon-star-off")
        this.star = "el-icon-star-on";
      else
        this.star = "el-icon-star-off";
    },
    not_liked_change: function() {
          let temp = {
          };
          let data = JSON.stringify(temp);
          this.$http.post("http://127.0.0.1:8005/p/"+this.$route.params.id_article.toString()+'/not_liked', data)
                    .then((response) => {
                        this.liked = this.liked - 1;
                        console.log("OK -- not_like");
                    },
                      (response) => {
                        console.log("Not OK -- not_like");
                      })

    },
    liked_change: function() {
          let temp = {
          };
          let data = JSON.stringify(temp);
          this.$http.post("http://127.0.0.1:8005/p/"+this.$route.params.id_article.toString()+'/liked', data)
                    .then((response) => {
                        this.liked = this.liked + 1;
                        console.log("OK -- like");
                    },
                      (response) => {
                        console.log("Not OK -- not_like");
                      })

    },

  }
}
</script>

<style>
  #Article {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
  }
}

  .el-col {
    border-radius: 4px;
  }

  textarea.article {
    resize:none;
    width:500px;
    height:300px;
  }

</style>

