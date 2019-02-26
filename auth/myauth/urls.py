
from django.urls import path,include
from . import views

app_name='myauth'

urlpatterns = [
    path('home/',views.home,name='主页' ),
    path('login/',views.logins,name='登录' ),
    path('logouts/',views.logouts,name='登出' ),
    path('zhuce/',views.zhuce ,name='注册' ),
]