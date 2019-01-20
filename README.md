## 环境
### 虚拟环境
#### 搭建虚拟环境
安装虚拟环境
```python

pip install virtualenv
```
新建一个文件夹，作为虚拟环境，通过cd命令进入，执行
```python
virtualenv .
```
该命令可以把当前文件夹作为虚拟文件
#### 启用虚拟环境
进入虚拟环境文件夹，可以看到一个Scripts文件夹，进入，运行activate
```txt
E:\>cd testvir\Scripts

E:\testvir\Scripts>activate
```
成功启用后会看见路径前面加了一个括号，里面是虚拟环境文件夹名
```python
(testvir) E:\testvir\Scripts
```
### 项目
#### 创建项目
在虚拟环境文件夹中新建一个文件用来存放所有Django项目  
进入该项目文件夹，运行
```python
django-admin startproject  (项目名称)
```
#### 启动服务器
进入创建的项目文件夹，会有manage.py的一个文件，运行
```python
python manage.py runserver
```
运行成功会有如下提示
>Performing system checks...
System check identified no issues (0 silenced).
You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
January 20, 2019 - 09:47:57
Django version 2.1.4, using settings 'ToDouList.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

访问 http://127.0.0.1:8000/ 可以看到Django欢迎界面
#### 各文件作用
##### urls
该文件用来处理url 原理是对匹配的url 进行切割，切割后的url传递给app中urls处理，如
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',include(todolist.urls))
]
```
在浏览器中输入 `http://127.0.0.1:8000/todo/home/1/` 其中`http://127.0.0.1:8000/`是服务器，会被直接分掉，在`http://127.0.0.1:8000/ `之后的`/todo/home/1/`与`urlpatterns`匹配，就会把`todo/`之后的东西分发给`todolist.urls`处理
##### settings
该文件是创建项目时自动生成的，用来设置项目相关的数据库，app等信息
## Django APP
在Django中，每个App负责一个功能
### App注册
#### 新建App
在项目文件夹下面运行
```python
python manage.py startapp (app名称)
```
#### 注册app
新建app后，需要注册，才能使Django识别
打开 <font color=#9ACD32 >项目文件夹</font>下面的setting.py文件中的
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
这就是目前项目中所有用到的app,这些都是官方提供的，我们按照格式填上自己新建的app，在最后写上app名即可
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todolist',
]
```
### App中重要文件作用
#### urls
该文件夹需要自己创建，用来处理从项目文件夹中分发过来的url，原理与项目文件夹相同
#### views
用来实现app视图相关的大部分后端逻辑
#### static
django推荐的静态文件文件夹，需要自己创建，用来储存css,js,图片等静态文件，为了避免静态文件重名，一般在static中再建一个与app同名的文件夹，静态文件分类放在该文件夹中
#### templates
django推荐的存放html页面的文件夹，同样为了避免重名，在内部可以建一个与app同名的文件夹

### 模板继承
诸如导航栏之类的，每个页面都有的东西，不必要复制很多，可以新建一个html 文件，django推荐命名是base.html,作为父模板，每个页面需要这些元素时，只需要继承该模板即可，具体方法是：  

* base.html
```txt
# 这些是父模板，诸如导航栏之类

{% block 导航栏 %}
{% endblock 导航栏 %}
```
**注意：** `导航栏`是block标签名
* 子页
```python
{% extends "todolist/base.html"%}
{% block 导航栏 %}
{% endblock 主题 %}
```
**注意：** `{% extends "todolist/base.html"%}`要写在最前面，用来声明要继承的模板位置`{% block 导航栏 %}{% endblock 主题 %}`之间是子页面自己的东西
<br />
**总结：** 模板继承其实就是把子页中的`{% block 导航栏 %}{% endblock 主题 %}`之间的内容放在模板`{% block 导航栏 %}{% endblock 导航栏 %}`之间

hahhahahahahahahhah