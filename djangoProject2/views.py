from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todos
from .forms import listform, UserLogin, UserRegister
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model,login, logout

def index(request):
    if request.method =="POST":
        form = listform(request.POST or None)
        if form.is_valid:
            form.save()
            todolist = todos.objects.all()
            return render(request, "todo/index.html", {'todo_list': todolist})
    else:
        todolist = todos.objects.all()
        return render(request,"todo/index.html", {'todo_list':todolist})

def about(request):
    return render(request, "todo/about.html")

def create(request):
    if request.method == "POST":
        form = listform(request.POST or None)
        if form.is_valid:
            form.save()
            todolist = todos.objects.all()
            return render(request, "todo/create.html", {'todo_list': todolist})
    else:
        todolist = todos.objects.all()
        return render(request, "todo/create.html", {'todo_list': todolist})

def delete(request, todos_id):
    todo = todos.objects.get(pk=todos_id)
    todo.delete()
    return redirect("index")

def finish(request, todos_id):
    todo = todos.objects.get(pk=todos_id)
    todo.finished = False
    todo.save()
    return redirect("index")

def nofinish(request, todos_id):
    todo = todos.objects.get(pk=todos_id)
    todo.finished = True
    todo.save()
    return redirect("index")

def update(request,todos_id):
    if request.method == "POST":
        todo_li = todos.objects.get(pk=todos_id)
        form = listform(request.POST or None, instance=todo_li)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:
        todolist = todos.objects.all()
        return render(request, "todo/update.html", {'todo_list': todolist})

def loginview(request):
    form = UserLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect('index/')
    context = {
        'form': form,
    }
    return render(request,"todo/login.html", context)

@login_required(login_url='/todo/index.html/')

def home(request):
    return render(request, "todo/index.html",{})

