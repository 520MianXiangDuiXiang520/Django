from django.shortcuts import render,redirect

# Create your views here.
id=1
lst=[
    {'事件名称':'遛狗','完成情况':False},
    {'事件名称':'pp','完成情况':True},
]

def home(request):
    global lst
    if request.method=="POST":
        if request.POST['待办']=='':
            connect = {'警告':'内容不可以为空！','清单': lst}
            return render(request, "todolist/home.html", connect)
        else:
            lst.append({'事件名称': request.POST['待办'], '完成情况': False})
            connect={'成功提示':'待办添加成功！','清单': lst}
            return render(request,"todolist/home.html",connect)
    else:
        connect = {'清单': lst}
        return render(request, "todolist/home.html", connect)

def about(request):
    return render(request,"todolist/about.html")

def edit(request,forloop_counter):
    if request.method=="POST":
        connect={'事件名称': request.POST['change'], '完成情况': False}
        lst[int(forloop_counter)-1]=connect
        return redirect("todolist:主页")
    else:
        return render(request, "todolist/edit.html",{'事件名称': lst[int(forloop_counter)-1]['事件名称']})

def delete(request,forloop_counter):
    lst.pop(int(forloop_counter)-1)
    return redirect("todolist:主页")

def success(request,forloop_counter):
    lst[int(forloop_counter)-1]['完成情况']=True
    return redirect("todolist:主页")

def unsuccess(request,forloop_counter):
    lst[int(forloop_counter)-1]['完成情况']=False
    return redirect("todolist:主页")