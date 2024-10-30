<template>
  <div id="User">

    <el-row class="body-style">
       <img src="../assets/logo.png" ></img>
    </el-row>

    <div class="block1">
      <el-row :gutter="20" class="body-style">
            <span class="demonstration">这里你将见到知识的海洋</span>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="10">
          <div class="grid-content bg-white"></div>
        </el-col>
        <el-col :span="8" class="col-style">
          <div class="tab1">
            <el-tabs v-model="activeName" class="tab-size">
              <el-tab-pane name="first"></el-tab-pane>

              <el-tab-pane label="登录" name="second">
                <el-form :model="loginForm" status-icon :rules="loginRules" ref="loginForm">
                  <el-form-item prop="loginUsername" class="input-style">
                    <el-input v-model="loginForm.loginUsername" placeholder="手机号/邮箱" ></el-input>
                  </el-form-item>
                  <el-form-item prop="loginPass" class="input-style">
                    <el-input type="password" placeholder="密码" v-model="loginForm.loginPass" auto-complete="off"></el-input>
                  </el-form-item>
                </el-form>
                <div>
                  <el-button class="el-button" @click="loginSubmit(loginForm.loginUsername,loginForm.loginPass)" type="primary">登录</el-button>
                </div>
                <el-row>
                  <el-col :span="8">
                    <div>
                      <el-button type="text" class="text-button-style1">手机二维码登录</el-button>
                    </div>
                  </el-col>
                  <el-col :span="1">
                    <div class="grid-content bg-white">
                    </div>
                  </el-col>
                  <el-col :span="1">
                    <div>
                      <el-button type="text" class="text-button-style2" >无法登录?</el-button>
                    </div>
                  </el-col>
                </el-row>
              </el-tab-pane>

              <el-tab-pane name="third"></el-tab-pane>

              <el-tab-pane name="fourth" label="注册">
                <!--这里就需要稍微布局一下了-->

                <el-form :model="regForm" status-icon :rules="regRules" ref="regForm">
                  <el-form-item prop="regUsername" class="input-style">
                    <el-input v-model="regForm.regUsername" placeholder="手机号/邮箱" ></el-input>
                  </el-form-item>
                  <el-form-item prop="regPass" class="input-style">
                    <el-input type="password" placeholder="密码" v-model="regForm.regPass" auto-complete="off"></el-input>
                  </el-form-item>
                  <el-form-item prop="checkPass" class="input-style">
                    <el-input type="password" placeholder="密码确认" v-model="regForm.checkPass" auto-complete="off"></el-input>
                  </el-form-item>

                  <el-form-item>
                    <el-button type="primary" @click="regSubmit('regForm')" class="reg-button">提交</el-button>
                    <div>
                      <el-button @click="resetForm('regForm')" class="reg-button">重置</el-button>
                    </div>
                  </el-form-item>
                </el-form>

              </el-tab-pane>
            </el-tabs>
          </div>
        </el-col>
      </el-row>
     </div>
   </div>
</template>

<script>
export default {
  data (){
    //  element-ui中可以自定义表单的验证方法
    //  检查用户名
    var checkUsername = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('账户不能为空'));
        }
        else {
          callback();
        }
      };
    //  检查注册密码是否为空 并调用重复密码的检测
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        if (this.regForm.checkPass !== '') {
          this.$refs.regForm.validateField('checkPass');
        }
        callback();
      }
    };
    //  检查注册的重复密码
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.regForm.regPass) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    //  检查登陆的密码是否为空
    var LoginValidatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        callback();
      }
    };
    //  我们约定俗成的账户状态码
    var account_code = {
          "100": "not_POST",
          "101": "username_invalid",
          "102": "password_invalid",
          "103": "username_existed",  //for register
          "105": "username_not_existed",  //for login
          "106": "password_error",
          "110": "register_success",
          "120": "login_success",
          "130": "reset_password_success",
          "140": "logout_success",
          "150": "options_request"
    };

    //  在子Vue实例中使用到的成员属性和方法等
    return {
      activeName: 'second',
      account_code,
      //  登录中使用的属性
			loginForm: {
          loginPass: '',
          loginUsername: ''
      },
      //  登陆表单的验证规则
      loginRules: {
        loginPass: [
          { validator: LoginValidatePass, trigger: 'blur' }
        ],
        loginUsername: [
          { validator: checkUsername, trigger: 'blur' }
        ]
      },
      //  注册中使用的属性
      regForm: {
          regPass: '',
          checkPass: '',
          regUsername: ''
      },
      //  注册表单的验证规则
      regRules: {
        regPass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
        regUsername: [
          { validator: checkUsername, trigger: 'blur' }
        ]
      }
      };
  },
  methods: {
    //  实现登陆按钮的交互功能 && 与后端的数据交换
    loginSubmit (username, password) {
      if(username.length>5 && username.length<64) {
          if(password.length>5 && password.length<64) {
            let temp = {
                "username": username,
                "password": password
          };
          let account = JSON.stringify(temp);
          this.$http.post("http://127.0.0.1:8005/login/",account)
                    .then((response) => {
                        console.log("OK in login");
                        console.log(response);
                        this.$parent.set('sessionKey', response.body.sessionKey, 1);
                        this.$parent.set('username', username, 1);
                        this.$parent.set('id_user', response.body.id_user, 1);
                        this.$parent.headline_condition = true;
                        if(response.body.code == "120") {
                          this.$router.push('/p');
                          location.reload();
                        }
                    },
                    (response) => {
                          console.log("Not OK in login");
                          console.log(response);
                    });
          }
          else {
            alert("Your password input is invalid !!");
          }
      }
      else {
        alert("Your username input is invalid !!");
      }
    },
    //  实现注册按钮的交互功能 && 与后端的数据交换
    regSubmit(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let username = this.regForm.regUsername,
                password = this.regForm.regPass;
            if(username.length>5 && username.length<64) {
                if(password.length>5 && password.length<64) {
                  let temp = {
                      "username": username,
                      "password": password
                };
                let account = JSON.stringify(temp);
                this.$http.post("http://127.0.0.1:8005/register/",account)
                          .then((response) => {
                              console.log("register OK");
                              console.log(response);
                              alert(this.account_code[response.body]);
                              this.$parent.headline_condition = true;
                              if(response.body == "110") {
                                this.$router.push('/'); //注册完后重新跳转到登录页面
                                location.reload();
                              }
                          },
                          (response) => {
                                console.log("Not OK in register");
                                console.log(response);
                          });
                }
                else {
                  alert("Your password input is invalid !!");
                }
            }
            else {
              alert("Your username input is invalid !!");
            }
            return true;
          }
          else {
            console.log('error register submit!!');
            return false;
          }
        });
      },
      //  重置按钮的功能实现
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
  },
  beforeCreate: function() {
    this.$parent.headline_condition = false;
  }
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif,MicrosoftYahei;
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

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
 .body-style {
    text-align: center;
  }
  .el-menu {
     background-color: transparent;
     width: 200px;
  }
  .el-button {
     width: 230px;
  }
  .col-style {
    margin-left: -10px;
  }
  .demonstration {
    font-size: 400;
  }
  .tab-size {
    width: 230px;
    padding-left: 15px;
  }
  .input-style {
    margin-bottom: 17px;
    width: 230px;
    height: 40px;
  }
  .text-button-style1 {
    text-align:left;
    width:120px;
  }
  .text-button-style2 {
    text-align:right;
    width:135px;
    color:grey;
  }
  .reg-button {
    margin-bottom: 5px;
  }
</style>
