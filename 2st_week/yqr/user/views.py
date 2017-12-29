from django.shortcuts import render
from django.http import HttpResponse

''' To do list
1.//注册账号
  账号重名检测[注意账号类别]
  数据有效性、规范检测
  异常捕获
  存入数据库中
  返回登录信息

2.//登陆
  账号存在检测[注意账号类别]
  密码匹配
  异常捕获
  返回登陆信息

 3.//忘记密码
   与注册账号类似

 4.//与前端vue.js 的表单功能结合
   探讨如何将网页表单数据传送到后端
   Django中的视图中，方法接收到的request对象有什么成员属性?如何利用?
   (使用vue.js的form 还是 Django的form 或者是其它解决方案?)
  '''


def function1(request):
    pass

def function2(request):
    pass
