from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import 文章分类,文章标签,文章内容,评论
import markdown
from .froms import 评论表单
import time
# Create your views here.

def 首页(request):
    分类=文章分类.objects.all()
    标签=文章标签.objects.all()
    内容=文章内容.objects.all()
    title=get_html()
    wz=get_wz()
    shijian=time.strftime("%Y-%m-%d", time.localtime())
    info={'分类':分类,'标签':标签,'内容':内容,'everyday':title,'wz':wz,'time':shijian}
    return render(request,'myblog/home.html',info)

def 更多(request,文章_id):
    内容 = 文章内容.objects.get(id=文章_id)
    内容.正文 = markdown.markdown(内容.正文,
                              extensions=[
                                  'markdown.extensions.extra',
                                  'markdown.extensions.codehilite',
                                  'markdown.extensions.toc',
                              ])
    评论列表 = 评论.objects.filter(对应文章_id=文章_id)
    for i in 评论列表:
        i.评论内容= markdown.markdown(i.评论内容,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    info = {'内容': 内容, '正文': 内容.正文, '评论列表': 评论列表, '评论': 评论表单}

    if request.method=='POST':
        form=评论表单(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.对应文章_id=文章_id
            a.save()
            #return render(request, 'myblog/more.html', info)
            return HttpResponseRedirect(reverse('更多', args=(文章_id)))
    else:
        return render(request, 'myblog/more.html', info)



def 关于(request):
    return render(request,'myblog/about.html')

def flag(request,i_id):
    文章=文章内容.objects.filter(分类_id=i_id)
    分类列表=文章分类.objects.all()
    title = get_html()
    wz = get_wz()
    shijian = time.strftime("%Y-%m-%d", time.localtime())
    info={'内容':文章,'分类列表':分类列表,'everyday':title,'wz':wz,'time':shijian}
    return render(request, 'myblog/flag.html', info)

import requests
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring,tostring


def get_html():

    url='https://tool.lu/todayonhistory/'
    r=requests.get(url)
    r=r.text
    #print(r)
    soup=BeautifulSoup(r,'html.parser')
    s=soup.find_all('ul',attrs={'id': 'tohlis'})
    s = repr(s[0])
    tree = fromstring(s)
    s = tostring(tree, pretty_print=True)
    soup = BeautifulSoup(s, 'html.parser')
    s=soup.find_all('li')
    s=repr(s[0])
    r1='[a-zA-z]+://[^\s]*'
    r2='[\u4e00-\u9fa5]+'
    r3='[0-9]+年[0-9]+月+[0-9]+日'
    url = re.findall(r1, s)
    title=re.findall(r2,s)
    data=re.findall(r3,s)
    dir = {'URL': url[0], 'title': title[3],'data':data[0]}
    return dir

def get_wz():

    url='http://www.ttmeiwen.com'
    r=requests.get(url)
    r=r.text
    #print(r)
    soup=BeautifulSoup(r,'html.parser')
    s=soup.find_all('ul',attrs={'class': 'list-unstyled'})
    s = repr(s[0])
    tree = fromstring(s)
    s = tostring(tree, pretty_print=True)
    soup = BeautifulSoup(s, 'html.parser')
    s=soup.find_all('li')
    s=repr(s[0])
    s = tostring(tree, pretty_print=True)
    soup = BeautifulSoup(s, 'html.parser')
    s = soup.find_all('a')
    t = soup.find_all('a', attrs={'class': 'title pull-left'})
    s = repr(s[2])
    t = repr(t[0])
    r1='[a-zA-z]+://[^\s]+html'
    r2='[\u4e00-\u9fa5].+[\u4e00-\u9fa5]'
    url=re.findall(r1,s)
    title=re.findall(r2,s)
    t = re.findall(r2, t)
    title = title[0].split('。')
    l = title[0]
    wenzhang={'url':url[0],'title':l,'t':t[0]}
    return wenzhang
