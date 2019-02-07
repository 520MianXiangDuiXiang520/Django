from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import 华语男歌手,欧美男歌手,日本男歌手,韩国男歌手,其他男歌手,华语女歌手,欧美女歌手,日本女歌手,韩国女歌手,其他女歌手,华语组合,欧美组合,日本组合,韩国组合,其他歌手组合

import re

artists = []
id = []

def get_artists(url,flag):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': '_iuqxldmzr_=32; _ntes_nnid=0e6e1606eb78758c48c3fc823c6c57dd,1527314455632; '
                         '_ntes_nuid=0e6e1606eb78758c48c3fc823c6c57dd; __utmc=94650624; __utmz=94650624.1527314456.1.1.'
                         'utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=blBrSVohtue8%2B6VgDkxOkJ2G0VyAgyOY;'
                         ' JSESSIONID-WYYY=Du06y%5Csx0ddxxx8n6G6Dwk97Dhy2vuMzYDhQY8D%2BmW3vlbshKsMRxS%2BJYEnvCCh%5CKY'
                         'x2hJ5xhmAy8W%5CT%2BKqwjWnTDaOzhlQj19AuJwMttOIh5T%5C05uByqO%2FWM%2F1ZS9sqjslE2AC8YD7h7Tt0Shufi'
                         '2d077U9tlBepCx048eEImRkXDkr%3A1527321477141; __utma=94650624.1687343966.1527314456.1527314456'
                         '.1527319890.2; __utmb=94650624.3.10.1527319890',
               'Host': 'music.163.com',
               'Referer': 'http://music.163.com/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    r = requests.get(url, headers=headers)
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    s = soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    r = '[1-9]+.+的'
    id_r = '([0-9]+[0-9])'
    art_r = '[0-9]+" title="'
    art_r2 = '的'

    for i in s:
        i = repr(i)
        ss = re.findall(r, i)
        ids = re.findall(id_r, ss[0])
        arts = re.sub(art_r, "", ss[0])
        arts = re.sub(art_r2, "", arts)
        if flag=='华语男歌手':
            obj = 华语男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='欧美男歌手':
            obj = 欧美男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='日本男歌手':
            obj = 日本男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='韩国男歌手':
            obj = 韩国男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='其他男歌手':
            obj = 其他男歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='华语女歌手':
            obj = 华语女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='欧美女歌手':
            obj = 欧美女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='日本女歌手':
            obj = 日本女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='韩国女歌手':
            obj = 韩国女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='其他女歌手':
            obj = 其他女歌手(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='华语组合':
            obj = 华语组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='欧美组合':
            obj = 欧美组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='日本组合':
            obj = 日本组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='韩国组合':
            obj = 韩国组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
        elif flag=='其他组合':
            obj = 其他歌手组合(歌手姓名=repr(arts), 歌手ID=ids[0])
            obj.save()
def pachong(flag,geshouid):
    initial = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
               89, 90]
    for jj in initial:
        url = 'https://music.163.com/discover/artist/cat?id=' + repr(geshouid) + '&initial=' + repr(jj)
        get_artists(url, flag)


# Create your views here.
def home(request):
    return render(request, "music/home.html")

def about(request):
    return render(request, "music/about.html")

def update(request):
    flag='华语男歌手'
    pachong(flag,1001)
    flag='华语女歌手'
    pachong(flag,1002)
    flag = '华语组合'
    pachong(flag, 1003)
    flag='欧美男歌手'
    pachong(flag, 2001)
    flag = '欧美女歌手'
    pachong(flag, 2002)
    flag = '欧美组合'
    pachong(flag, 2003)
    flag='日本男歌手'
    pachong(flag, 6001)
    flag = '日本女歌手'
    pachong(flag, 6002)
    flag = '日本组合'
    pachong(flag, 6003)
    flag='韩国男歌手'
    pachong(flag, 7001)
    flag = '韩国女歌手'
    pachong(flag, 7002)
    flag = '韩国组合'
    pachong(flag, 7003)
    flag = '其他男歌手'
    pachong(flag, 4001)
    flag = '其他女歌手'
    pachong(flag, 4001)
    flag = '其他组合'
    pachong(flag, 4001)


    connect={'ID':id,'NAME':artists}
    return render(request, "music/home.html", connect)

def chboy(request):
    name=华语男歌手.objects.all()
    connect={'a':name}
    return render(request, "music/ch.html",connect)

def usboy(request):
    return render(request, "music/ch.html")

def jpboy(request):
    return render(request, "music/ch.html")

def smdboy(request):
    return render(request, "music/ch.html")

def qtboy(request):
    return render(request, "music/ch.html")

def download(request,info_歌手ID):
    connect={'id':info_歌手ID}
    return render(request, "music/download.html",connect)