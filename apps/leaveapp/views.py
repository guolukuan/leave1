from django.shortcuts import render,HttpResponse,redirect,reverse
from django import views
from .models import Ratify
from user import models
import re,calendar
from utils.mixin import LoginRequiredMixin


#提交请假详情
class Apply(LoginRequiredMixin,views.View):
    def get(self,request):
        user = request.user
        users = models.User.objects.get(id=user.id)
        return render(request,'ask_for_leave.html',{'users':users})
    def post(self,request):
        user = request.user
        y = request.POST.get('Y')
        m = request.POST.get('m')
        d = request.POST.get('d')
        yy = request.POST.get('YY')
        mm = request.POST.get('mm')
        dd = request.POST.get('dd')
        cause = request.POST.get('cause')
        if not all([m,mm,y,yy,d,dd]):
            return render(request, 'ask_for_leave.html', {'errasg': '您的输入不合法'})
        if not 0>int(m)<12 and 0>int(mm)<12:
            return render(request, 'ask_for_leave.html', {'errasg': '您的输入日期有误'})
        if not 0>int(d)<31 and 0>int(dd)<31:
            return render(request, 'ask_for_leave.html', {'errasg': '您的输入日期有误'})
        n = y+'-'+m+'-'+d
        nn = yy + '-' + mm + '-' + dd
        if not re.match(r"(\d{4}-\d{1,2}-\d{1,2})",n):
            return render(request,'ask_for_leave.html',{'errasg':'您的输入日期有误'})
        if not re.match(r"(\d{4}-\d{1,2}-\d{1,2})",nn):
            return render(request, 'ask_for_leave.html', {'errasg': '您的输入日期有误'})
        try:
            message = models.Message.objects.get(user=user.id)
            ratify = Ratify.objects.create(name=message.name,
                                       department=message.section,
                                       phone=message.phone,
                                       sex=message.sex,
                                        start_data=n,
                                       due_date=nn,
                                        cause=cause)
            ratify.save()
            return redirect(reverse('leaveapp:apply'))
        except Exception:
            return redirect(reverse('leaveapp:apply'))


#渲染品准页面
class index(views.View,LoginRequiredMixin):
    def get(self,request):
        ratify = Ratify.objects.filter(affirm='待批准')
        return render(request,'index.html',{"ratify":ratify})


def Decision(request,id):
    ratify = Ratify.objects.get(id=id)
    ratify.affirm = '批准'
    ratify.save()
    return redirect(reverse('leaveapp:index'))

def unapproved(request,id):
    ratify = Ratify.objects.get(id=id)
    ratify.affirm = '不批准'
    ratify.save()
    return redirect(reverse('leaveapp:index'))


def result(request):
    user = request.user
    message = models.Message.objects.get(user=user.id)
    print(message.name)
    ratify = Ratify.objects.filter(name=message.name)
    # print(ratify.name)
    return render(request,'result.html',{"ratify":ratify})



