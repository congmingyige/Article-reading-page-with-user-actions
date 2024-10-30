<template>
  <div class="Headline">
        <!--<el-header style="padding:0;">-->
            <el-row>
                <el-menu :default-active="activeIndex" class="el-menu-demo"  mode="horizontal">
                <el-row>
                    <el-col :span="8"  type="flex" justify="space-around">
                      <el-menu-item index="1" class="font-size-large">
                        <a src="www.baidu.com"><img src="../assets/logo.png" style="height:60px;" class="nav-logo"></a>
                      </el-menu-item>
                      <el-menu-item index="1" class="font-size-large">发现</el-menu-item>
                      <el-menu-item index="1" class="font-size-large">关注</el-menu-item>
                      <el-menu-item index="1" class="font-size-large">消息</el-menu-item>
                    </el-col>
                    <el-col :span="14">
                      <el-menu-item index="1">
                          <el-input
                                placeholder="请输入想查找的内容"
                                icon="search"
                                v-model="searchText"
                                :on-icon-click="search">
                          </el-input>
                          <el-button type="primary">搜索</el-button>
                      </el-menu-item>
                    </el-col>
                    <el-col :span="2">
                      <div style="display:flex; display:-webkit-flex; align-items:center;">
                          <el-submenu index="2">
                              <template slot="title"><img src="../assets/logo.png" style="height:40px;"></template>
                              <el-menu-item index="2-1" @click="toUserpage">我的主页</el-menu-item>
                              <el-menu-item index="2-2" @click="toUserinfo">设置</el-menu-item>
                              <el-menu-item index="2-3" @click="logout">退出</el-menu-item>
                          </el-submenu>
                      </div>
                    </el-col>
                </el-row>
                </el-menu>
            </el-row>
        <!--</el-header>-->
  </div>
</template>

<script>
  export default {
      name: 'Headline',
      prop: ['username'],
      data() {
          return {
              activeIndex: '1',
              searchText: '',
              username: ''
          }
      },
      methods: {
        logout: function() {
            this.$http({
                method: 'POST',
                url: "http://127.0.0.1:8005/logout",
                headers: {
                    'sessionKey': this.$parent.get('sessionKey')
                },
                body: {

                }
              }).then((response) => {
                this.username = '';
                this.$parent.delete('sessionKey');
                this.$parent.delete('username');
                this.$parent.delete('id_user');
                this.$router.push('/');
              },
              (response) => {
                alert('数据传输失败');
              });
        },
        toUserpage: function() {
            this.$router.push('/a/'+this.$parent.get('id_user'));
        },
        toUserinfo: function() {
            this.$router.push('/a/'+this.$parent.get('id_user')+'/getProfile');
        },
        search: function() {

        }
      }
  }
</script>

<style>

</style>
