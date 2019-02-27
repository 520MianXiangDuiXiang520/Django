
from django.urls import path,include
from . import views

app_name='myauth'

urlpatterns = [
    path('home/',views.home,name='主页' ),
    path('login/',views.logins,name='登录' ),
    path('logouts/',views.logouts,name='登出' ),
    path('zhuce/',views.zhuce ,name='注册' ),
    path('个人中心/', views.个人中心, name='个人中心'),
    path('个人中心/修改密码', views.修改密码, name='修改密码'),
    path('个人中心/修改个人信息', views.修改个人信息, name='修改个人信息'),
]