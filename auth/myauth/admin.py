from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import User
from .models import 普通会员表

# Register your models here.
class 普通会员表Inline(admin.TabularInline):
    model = 普通会员表
    can_delete = False
    verbose_name_plural = '普通会员表'

class UserAdmin(BaseUserAdmin):
    inlines = (普通会员表Inline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
