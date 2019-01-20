from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.


def home(request):
    if request.method=="POST":
        if request.POST['待办']=='':
            connect = {'警告':'内容不可以为空！','清单': Todo.objects.all()}
            return render(request, "todolist/home.html", connect)
        else:
            a_row=Todo(thing=request.POST['待办'], done=False)
            a_row.save()
            connect={'成功提示':'待办添加成功！','清单': Todo.objects.all()}
            return render(request,"todolist/home.html",connect)
    else:
        connect = {'清单': Todo.objects.all()}
        return render(request, "todolist/home.html", connect)

def about(request):
    return render(request,"todolist/about.html")

def edit(request,everything_id):
    a = Todo.objects.get(id=int(everything_id))
    if request.method=="POST":
        a.thing=request.POST['change']
        a.save()
        return redirect("todolist:主页")
    else:
        return render(request, "todolist/edit.html",{'事件名称':a.thing})

def delete(request,everything_id):
    a=Todo.objects.get(id=everything_id)
    a.delete()
    return redirect("todolist:主页")

def success(request,everything_id):
    a = Todo.objects.get(id=int(everything_id))
    a.done=True
    a.save()
    return redirect("todolist:主页")

def unsuccess(request,everything_id):
    a = Todo.objects.get(id=int(everything_id))
    a.done = False
    a.save()
    return redirect("todolist:主页")