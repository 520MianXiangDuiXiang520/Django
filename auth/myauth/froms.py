from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class 自定义表单(UserCreationForm):
    昵称=forms.CharField(required=False,max_length=50)
    生日=forms.DateField(required=False)

    class Meta:
        model=User
        fields=('username','password1','password2','email','昵称','生日')