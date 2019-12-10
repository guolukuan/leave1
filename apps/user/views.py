from django.shortcuts import render,reverse,redirect,HttpResponse
from django import views
from django.contrib.auth import authenticate,login,logout
from .models import User,Message

import re
from utils.mixin import LoginRequiredMixin
# Create your views here.

#注册
class Register(views.View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        pwds = request.POST.get('mail')
        if not all([username,pwd,pwds]):
            return render(request,'register.html',{'reemsg':'数据不完整'})
        if User.objects.filter(username=username):
            return render(request,'register.html',{'reemsg':'用户已存在'})
        if pwd != pwds:
            return render(request,'register.html',{'reemsg':'两次输入密码不一致'})
        user = User.objects.create_user(username=username,password=pwd)
        user.save()
        return redirect(reverse('user:login'))


#登录
class Login(views.View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST.get('username')
        pwd = request.POST.get('password')

        if not all([username,pwd]):
            return render(request,'login.html',{'reemsg':'数据不完整'})

        """验证用户是否存在"""
        user = authenticate(request,username=username,password=pwd)
        """记录用户登录状态"""
        login(request,user=user)
        response = redirect(reverse('user:usercentre'))
        response.delete_cookie('username')
        return response



#用户退出
class Exit(views.View):
    def get(self,request):
        logout(request)
        return redirect(reverse('user:login'))


#用户个人信息
class User_centre(LoginRequiredMixin,views.View,):
    def get(self,request):
        try:
            user = request.user
            message = Message.objects.get(user=user.id)
            users = User.objects.get(id=user.id)

            return render(request, 'userc entre.html', {'message': message,'users':users})
        except Exception:
            return render(request,'userc entre.html',{'errmsg':'请添加个人信息'})
    def post(self,request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        serial = request.POST.get('serial')
        phone = request.POST.get('phone')
        section = request.POST.get('section')
        """验证手机号和个人信息的完整性"""
        if not all([name,age,sex,serial,phone,section]):
            return render(request,'userc entre.html',{'errmsg':'请输入完整信息'})
        print('错误1')
        if not re.match('[\u4e00-\u9fa5]',name):
            return render(request, 'userc entre.html', {'errmsg': '姓名只可为汉字'})
        if sex != '男' or sex !='女':
            return render(request, 'userc entre.html', {'errmsg': '请输入正确的性别'})
        if not re.match('^((13[0-9])|(14[5,7,9])|(15[^4])|(18[0-9])|(17[0,1,3,5,6,7,8]))\\d{8}$', phone):
            return render(request,'userc entre.html',{'errmsg':'手机号错误'})
        user = request.user
        message = Message.objects.create(name=name,
                                         age=age,
                                         sex=sex,
                                         serial=serial,
                                         phone=phone,
                                         section=section,
                                         user=user)
        message.save()
        return redirect(reverse('user:usercentre'))



#修改个人信息

class Update(LoginRequiredMixin,views.View,):

    def get(self,request):
        user = request.user
        message = Message.objects.get(user=user.id)
        users = User.objects.get(id=user.id)
        return render(request,'userc entre.html',{'message':message,'users':users,'ratify':ratify})

    def post(self,request):
        user = request.user
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        serial = request.POST.get('serial')
        phone = request.POST.get('phone')
        section = request.POST.get('section')
        if not re.match('[\u4e00-\u9fa5]',name):
            return render(request, 'userc entre.html', {'errmsg': '姓名只可为汉字'})
        if sex != '男' or sex !='女':
            return render(request, 'userc entre.html', {'errmsg': '请输入正确的性别'})
        if not re.match('^((13[0-9])|(14[5,7,9])|(15[^4])|(18[0-9])|(17[0,1,3,5,6,7,8]))\\d{8}$', phone):
            return render(request,'userc entre.html',{'errmsg':'手机号错误'})
        message = Message.objects.get(user=user.id)
        message.name=name
        message.age=age
        message.aex=sex
        message.serial=serial
        message.phone=phone
        message.section=section
        message.save()
        return redirect(reverse('user:update'))