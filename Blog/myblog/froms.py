from django import forms
from .models import 评论

class 评论表单(forms.ModelForm):
    class Meta:
        model=评论
        fields=['评论者','评论内容']
