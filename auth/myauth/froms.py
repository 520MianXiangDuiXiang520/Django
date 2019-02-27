from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField

class 自定义表单(UserCreationForm):
    昵称=forms.CharField(required=False,max_length=50)
    生日=forms.DateField(required=False)

    class Meta:
        model=User
        fields=('username','password1','password2','email','昵称','生日')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].error_messages={'unique':'用户名已存在！！！','invalid':'用户名不合法'}


class 自定义编辑表单(UserChangeForm):
    昵称=forms.CharField(required=False,max_length=50)
    生日=forms.DateField(required=True)
    验证码=CaptchaField()

    class Meta:
        model=User
        fields=('username','password','email','昵称','生日')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].error_messages={'unique':'用户名已存在！！！','invalid':'用户名不合法'}



