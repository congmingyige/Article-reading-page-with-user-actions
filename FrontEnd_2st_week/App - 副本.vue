<template>
  <div id="app">
    <img src="./assets/logo.png"></img>
    <h1>{{ msg }}</h1>
    <el-button @click.native="startHacking">Let's do it</el-button>
    <div class="block1">
      <el-row :gutter="20">
        <el-col :span="6">
          <div class="grid-content bg-white"></div>
        </el-col>
        <el-col :span="4">
          <div class="character1">
            <span class="demonstration" v-model="character1">这里你将见到知识的海洋</span>
          </div>
        </el-col>
        <el-col :span="2">
          <div class="grid-content bg-white"></div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-white"></div>
        </el-col>
      </el-row>
     <el-row :gutter="20">
       <el-col :span="14">
         <div class="el-menu-demo"></div>
         <el-menu theme="dark" :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect">
           <el-menu-item index="1">处理中心</el-menu-item>
           <el-submenu index="2">
             <template slot="title">我的工作台</template>
             <el-menu-item index="2-1">选项1</el-menu-item>
             <el-menu-item index="2-2">选项2</el-menu-item>
             <el-menu-item index="2-3">选项3</el-menu-item>
           </el-submenu>
           <el-menu-item index="3">
             <a href="https://www.ele.me" target="_blank">订单管理</a>
           </el-menu-item>
         </el-menu>
       </el-col>
     </el-row>
   <el-row :gutter="20">
   <el-col :span="6"><div class="grid-content bg-white"></div></el-col>
   <el-col :span="4"><div class="input"><el-input v-model="username" placeholder="手机号或者邮箱"></el-input></div></el-col>
   <el-col :span="2"><div class="grid-content bg-white"></div></el-col>
   <el-col :span="4"><div class="grid-content bg-white"></div></el-col>
   </el-row>
   <el-row :gutter="20">
   <el-col :span="6"><div class="grid-content bg-white"></div></el-col>
   <el-col :span="4"><div class="input1"><el-input v-model="password" placeholder="密码"></el-input></div></el-col>
   <el-col :span="2"><div class="grid-content bg-white"></div></el-col>
   <el-col :span="4"><div class="grid-content bg-white"></div></el-col>
    </el-row>
    <el-row :gutter="20">
   <el-col :span="7"><div class="grid-content bg-white"></div></el-col>
   <el-col :span="6"><div class="button1"><el-button @click="loginSubmit(username,password)" type="primary">登陆</el-button></div></el-col>
   <el-col :span="4"><div class="grid-content bg-white"></div></el-col>
    </el-row>
     </div>
   </div>
</template>
<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    startHacking () {
      this.$notify({
        title: 'It Works',
        message: 'We have laid the groundwork for you. Now it\'s your time to build something epic!',
        duration: 6000
      })
    },
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    loginSubmit (username, password) {
        var account_code = {
            "100": "not_POST",
            "101": "username_invalid",
            "102": "password_invalid",
            "103": "username_existed",  //for register
            "105": "username_not_exist",  //for login
            "106": "password_error",
            "110": "register_success",
            "120": "login_success",
            "130": "reset_password_success",
            "140": "logout_success",
            "150": "options_request"
        };
        let temp = {
            "username": username,
            "password": password
        };
        let account = JSON.stringify(temp);
        this.$http.post("http://127.0.0.1:8000/login/",account)
                  .then((response) => {
                      console.log("OK");
                      console.log(response);
                      alert(account_code[response.body]);

                  },
                  (response) => {
                         console.log("Not OK");
                         console.log(response);
                  });
    }
  }
}
</script>
<style>
body {
  font-family: Helvetica, sans-serif;
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
</style>
