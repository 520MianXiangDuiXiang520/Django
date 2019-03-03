from django.contrib import admin
from .models import 文章分类,文章标签,文章内容

# Register your models here.
admin.site.register(文章分类)
admin.site.register(文章标签)
admin.site.register(文章内容)