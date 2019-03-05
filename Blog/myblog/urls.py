
from django.urls import path
from . import views

app_name='myblog'
urlpatterns = [
    path('home/',views.首页,name='首页'),
    path('more/<文章_id>',views.更多,name='更多'),
    path('about/', views.关于, name='关于'),
    path('flag/<i_id>', views.flag, name='分类'),
]