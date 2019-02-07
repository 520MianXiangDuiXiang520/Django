from django.urls import path,include
from . import views

app_name='music'
urlpatterns = [
    path('home/',views.home,name='主页' ),
    path('about/',views.about,name='关于' ),
    path('chboy/',views.chboy,name='华语男'),
    path('usboy/',views.usboy,name='欧美男'),
    path('jpboy/',views.jpboy,name='日本男'),
    path('smdboy/',views.smdboy,name='韩国男'),
    path('qtboy/',views.qtboy,name='其他男'),
    path('update/',views.update,name='更新数据库'),
    path('download/<info_歌手ID>',views.download,name='下载'),

]