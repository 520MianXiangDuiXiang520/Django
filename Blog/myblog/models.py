from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class 文章分类(models.Model):
    类名=models.CharField(max_length=70)

    def __str__(self):
        return self.类名

class 文章标签(models.Model):
    标签名=models.CharField(max_length=70)

    def __str__(self):
        return self.标签名

class 文章内容(models.Model):
    标题=models.CharField(max_length=30)
    正文=models.TextField()
    创建时间=models.DateField()
    摘要=models.CharField(max_length=100,blank=True)
    分类=models.ForeignKey(文章分类,on_delete=models.CASCADE)
    标签=models.ManyToManyField(文章标签,blank=True)
    作者=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.标题


class 评论(models.Model):
    评论者=models.CharField(max_length=20)
    评论日期=models.DateField(auto_now_add=True)
    评论时间=models.TimeField(auto_now_add=True)
    评论内容=models.TextField()
    对应文章=models.ForeignKey('myblog.文章内容',on_delete=models.CASCADE)

    def __str__(self):
        return self.评论者

