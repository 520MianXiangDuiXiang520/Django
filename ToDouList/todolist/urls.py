from django.urls import path,include
from . import views

app_name="todolist"
urlpatterns = [
    path('home/',views.home,name="主页"),
    path('about/',views.about,name="关于"),
    path('edit/<everything_id>',views.edit,name="编辑"),
    path('del/<everything_id>',views.delete,name="删除"),
    path('success/<everything_id>', views.success, name="划掉"),
    path('unsuccess/<everything_id>', views.unsuccess, name="撤销"),
]