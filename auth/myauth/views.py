from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .froms import 自定义表单
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