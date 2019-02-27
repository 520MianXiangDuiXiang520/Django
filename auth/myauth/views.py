from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .froms import 自定义表单,自定义编辑表单
from .models import 普通会员表


# Create your views here.
def home(request):
    return render(request,"myauth/home.html")

def logins(request):
    if request.method=='POST':
        users=authenticate(request,username=request.POST['用户名'],password=request.POST['密码'])
        if users==None:
            return render(request, "myauth/login.html",{'错误':'用户名或密码错误'})
        else:
            login(request,users)
            return  redirect('myauth:主页')
    else:
        return render(request,"myauth/login.html")

def logouts(request):
    logout(request)
    return redirect('myauth:主页')

def zhuce(request):
    if request.method == 'POST':
        froms=自定义表单(request.POST)
        # 如果表单填写正确
        if froms.is_valid():
            froms.save()
            user=authenticate(username=froms.cleaned_data['username'],password=froms.cleaned_data['password1'])
            user.email=froms.cleaned_data['username']
            普通会员表(用户=user,昵称=froms.cleaned_data['昵称'],生日=froms.cleaned_data['生日']).save()
            login(request, user)
            return redirect('myauth:主页')
    else:
        froms = 自定义表单()
    表单={'表单':froms}
    return render(request, "myauth/zhuce.html",表单)

@login_required(login_url='myauth:登录')
def 个人中心(request):
    info={'info':request.user}
    return render(request,"myauth/myhome.html",info)

@login_required(login_url='myauth:登录')
def 修改个人信息(request):
    if request.method=='POST':
        change_froms = 自定义编辑表单(request.POST,instance=request.user)
        if change_froms.is_valid():
            change_froms.save()
            request.user.普通会员表.昵称=change_froms.cleaned_data['昵称']
            request.user.普通会员表.生日 = change_froms.cleaned_data['生日']
            request.user.普通会员表.save()
            return redirect('myauth:个人中心')
    else:
        change_froms = 自定义编辑表单(instance=request.user)
    表单 = {'表单': change_froms,'用户':request.user}
    return render(request, "myauth/change_info.html", 表单)

@login_required(login_url='myauth:登录')
def 修改密码(request):
    if request.method=='POST':
        change_froms = PasswordChangeForm(data=request.POST,user=request.user)
        if change_froms.is_valid():
            change_froms.save()
            return redirect('myauth:登录')
    else:
        change_froms = PasswordChangeForm(user=request.user)
    表单 = {'表单': change_froms,'用户':request.user}
    return render(request, "myauth/change_pw.html", 表单)