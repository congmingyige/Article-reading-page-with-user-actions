<template>
<div id="people">
    <div class="projHeadline">
        <!--
            <projHeadline></projHeadline>
        -->
    </div>
    <p></p>
    <div class="people">
        <el-row>
            <el-col :span="4">
                <div class="grid-content bg-white"></div>
            </el-col>
            <el-col :span="16">
                <el-card>
                    <el-container>
                        <el-container>
                            <el-aside>
                                <img src="../assets/logo.png" class="img-style">
                            </el-aside>
                            <el-main class="edit-name-style">
                                <el-row style="height:80px;border-bottom-color:#cac9c9;border-bottom-width:1px;border-bottom-style:solid;">
                                    <el-col :span="14">
                                        <p style="font-weight: bold;font-size: x-large;text-align:left;">
                                            {{username}}
                                        </p>
                                    </el-col>
                                    <el-col :span="2">
                                        <el-button type="text" icon="el-icon-arrow-right" style="margin-top:15px;">
                                            返回
                                        </el-button>
                                    </el-col>
                                </el-row>
                                <div v-if="!edit.sex">
                                    <el-row style="height:80px;border-bottom-color:#cac9c9 ;border-bottom-width: 1px;border-bottom-style: solid;">
                                        <el-col :span="6">
                                            <p style="margin-top:18px;font-weight: bold;font-size: large;text-align:left;">
                                                性别
                                            </p>
                                        </el-col>
                                        <el-col :span="8">
                                            <p style="margin-top:18px;font-weight: bold;font-size: normal;text-align:left;">
                                                {{localInfo.sex}}
                                            </p>
                                        </el-col>
                                        <el-col :span="2">
                                            <el-button type="text" icon="el-icon-edit" style="margin-top:10px" v-on:click="edit.sex=!edit.sex">
                                                修改
                                            </el-button>
                                        </el-col>
                                    </el-row>
                                </div>
                                <div class="changemodel" v-if="edit.sex">
                                    <el-row>
                                        <el-col :span="6">
                                            <p style="margin-top:18px;font-weight: bold;font-size: large;text-align:left;">
                                                性别
                                            </p>
                                        </el-col>
                                        <el-col :span="10">
                                            <el-input v-model="localInfo.sex" style="margin-top:10px;"></el-input>
                                        </el-col>
                                    </el-row>
                                    <el-row style="height:60px;border-bottom-color:#cac9c9 ;border-bottom-width:1px;border-bottom-style:solid;">
                                        <el-col :span="6" style="height:20px">
                                            <div class="grid-content bg-white"></div>
                                        </el-col>
                                        <el-col :span="4">
                                            <div class="button1">
                                                <el-button type="round" size="small" class="button1" v-on:click="updateInfo('sex')">
                                                    确定
                                                </el-button>
                                            </div>
                                        </el-col>
                                        <el-col :span="1">
                                            <div class="bg-white"></div>
                                        </el-col>
                                        <el-col :span="4">
                                            <div class="button2">
                                                <el-button type="round" size="small" class="button2" v-on:click="edit.sex=!edit.sex">
                                                    取消
                                                </el-button>
                                            </div>
                                        </el-col>
                                    </el-row>
                                </div>
                                <div v-if="!edit.introduction">
                                    <el-row style="height:80px;border-bottom-color:#cac9c9;border-bottom-width: 1px;border-bottom-style: solid;">
                                        <el-col :span="6">
                                            <p text-align="left" style="margin-top:18px;font-weight: bold;font-size: normal;text-align:left;">
                                                个人简介
                                            </p>
                                        </el-col>
                                        <el-col :span="8">
                                            <p style="margin-top:18px;font-weight: bold;font-size: normal;text-align:left;">
                                                {{localInfo.introduction}}
                                            </p>
                                        </el-col>
                                        <el-col :span="2">
                                            <el-button type="text" icon="el-icon-edit" text-align="left" style="margin-top:10px" v-on:click="edit.introduction=!edit.introduction">
                                                修改
                                            </el-button>
                                        </el-col>
                                    </el-row>
                                </div>
                                <div class="changemodel1" v-if="edit.introduction">
                                    <el-row>
                                        <el-col :span="6">
                                            <p style="margin-top:18px;font-weight: bold;text-align:left;">
                                                个人简介
                                            </p>
                                        </el-col>
                                        <el-col :span="10">
                                            <el-input v-model="localInfo.introduction" style="margin-top:10px;"></el-input>
                                        </el-col>
                                    </el-row>
                                    <el-row style="height:60px;border-bottom-color:#cac9c9 ;border-bottom-width:1px;border-bottom-style:solid;">
                                        <el-col :span="6" style="height:20px">
                                            <div class="grid-content bg-white"></div>
                                        </el-col>
                                        <el-col :span="4">
                                            <div class="button1">
                                                <el-button type="round" size="small" class="button1" v-on:click="updateInfo('introduction')">
                                                    确定
                                                </el-button>
                                            </div>
                                        </el-col>
                                        <el-col :span="1">
                                            <div class="bg-white"></div>
                                        </el-col>
                                        <el-col :span="4">
                                            <div class="button2">
                                                <el-button type="round" size="small" class="button2" v-on:click="edit.introduction=!edit.introduction">
                                                    取消
                                                </el-button>
                                            </div>
                                        </el-col>
                                    </el-row>
                                </div>
                                <div v-if="!edit.resident">
                                    <el-row style="height:80px;border-bottom-color:#cac9c9;border-bottom-width: 1px;border-bottom-style: solid;">
                                        <el-col :span="6">
                                            <p text-align="left" style="margin-top:18px;font-weight: bold;font-size: normal;text-align:left;">
                                                居住地
                                            </p>
                                        </el-col>
                                        <el-col :span="8">
                                            <p style="margin-top:18px;font-weight: bold;font-size: normal;text-align:left;">
                                                {{localInfo.resident}}
                                            </p>
                                        </el-col>
                                        <el-col :span="2">
                                            <el-button type="text" icon="el-icon-edit" text-align="left" style="margin-top:10px" v-on:click="edit.resident=!edit.resident">
                                                修改
                                            </el-button>
                                        </el-col>
                                    </el-row>
                                </div>
                                <div class="changemodel1" v-if="edit.resident">
                                    <el-row>
                                        <el-col :span="6">
                                            <p style="margin-top:18px;font-weight: bold;text-align:left;">
                                                居住地
                                            </p>
                                        </el-col>
                                        <el-col :span="10">
                                            <el-input v-model="localInfo.resident" style="margin-top:10px;"></el-input>
                                        </el-col>
                                    </el-row>
                                    <el-row style="height:60px;border-bottom-color:#cac9c9 ;border-bottom-width:1px;border-bottom-style:solid;">
                                        <el-col :span="6" style="height:20px">
                                            <div class="grid-content bg-white"></div>
                                        </el-col>
                                        <el-col :span="4">
                                            <div class="button1">
                                                <el-button type="round" size="small" class="button1" v-on:click="updateInfo('resident')">
                                                    确定
                                                </el-button>
                                            </div>
                                        </el-col>
                                        <el-col :span="1">
                                            <div class="bg-white"></div>
                                        </el-col>
                                        <el-col :span="4">
                                            <div class="button2">
                                                <el-button type="round" size="small" class="button2" v-on:click="edit.resident=!edit.resident">
                                                    取消
                                                </el-button>
                                            </div>
                                        </el-col>
                                    </el-row>
                                </div>
                            </el-main>
                        </el-container>
                    </el-container>
                </el-card>
            </el-col>
            <el-col :span="4">
                <div class="grid-content bg-white"></div>
            </el-col>
        </el-row>
    </div>
</div>

</template>
<script>
//import projHeadline from "../components/projHeadline.vue" 
export default {
  name: 'people',
  components: {
    //projHeadline,
  },
  data () {
    return {
      username:'Ben',        
      localInfo: {
          sex: 'Male',
          resident: 'Laznzhou',
          introduction: 'Introduce your self~'
      },
      edit: {
          sex: false,
          introduction: false,
          resident: false
      },
      sessionKey: ''
    }
  },
  methods:{
      updateInfo(item) {
          let url = 'http://127.0.0.1:8000/editProfile';
          let info = {
              'sessionKey': this.sessionKey,
              'name': item,
              'value': this.localInfo[item]
          }
          this.$http.post(url, JSON.stringify(info))
                    .then((response) => {
                            if(response.body == "OJ8K") {
                                console.log("Cant not update profile");
                            }
                            else {
                                this.edit[item] = !this.edit[item]; 
                            }
                        },
                        (response) => {
                            console.log("Not OK in update profile");
                            console.log(response);
                        });
      }
  },
  created: function() {
      let url = 'http://127.0.0.1:8000/getProfile';
      this.sessionKey = "xthjdy2n4xaubaa870ga6hyifsw325o9";
      this.$http.post(url, this.sessionKey)
                .then((response) => {
                        if(response.body == "OJ8K") {
                            console.log("Cant not get updated profile through django");
                        }
                        else {
                            this.localInfo.sex = response.body.sex;
                            this.localInfo.resident = response.body.resident;
                            this.localInfo.introduction = response.body.introduction;
                        }
                    },
                    (response) => {
                          console.log("Not OK in people getting profile");
                          console.log(response);
                    });
    }
}
</script>
<style>
.row-edit-style
{
    width:300%;
}
.img-style
{
    border:4px;
    width:160px;
    height:40px;
}
.el-main
{
    line-height:50px;
    text-align:left;
    background-color: white;
}
.edit-name-style
{
    text-align:left;
    height:30px;
    background-color: white;
}
.el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color:white;
    text-align: center;
    line-height: 200px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  .edit-p-style
  {
      font-weight:bold;
  }
  .edit-row-style
  {
      border-bottom-color: rgb(21, 22, 20);
      border-bottom-width: 1px;
      border-bottom-style: solid;
  }
  .edit-p-style
  {
      font-weight: bold;
      font-size: x-large;
      text-align:left;
  }
  .bg-white
  {
      background-color:white;
  }
</style
