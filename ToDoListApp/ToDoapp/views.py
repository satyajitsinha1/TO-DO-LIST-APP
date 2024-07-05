from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from.forms import taskform
from.models import tasks

# Create your views here.

# function for home

def home(request):
    if request.user.is_authenticated:
        mytasks = tasks.objects.filter(user=request.user)
        if request.method=="POST":
            fm= taskform(request.POST)
            if fm.is_valid():   
                task = fm.save(commit=False)
                task.user = request.user 
                task.save()
                fm=taskform()
        else:
            fm = taskform()
        return render (request,'ToDoapp/home.html',{'form':fm,'mytasks':mytasks})
    else:
        return HttpResponseRedirect('/login/')



# function for singup

def register(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=UserCreationForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/login/')
        else:
            fm = UserCreationForm()
        return render (request,'ToDoapp/register.html',{'form':fm})
    else:
        return HttpResponseRedirect('/')



# function for login

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm= AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data['username']
                password=fm.cleaned_data['password']
                user= authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            fm = AuthenticationForm()
        return render   (request, 'ToDoapp/login.html',{'form':fm})   
    else: 
        return HttpResponseRedirect('/')



# function for logout

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def finished(request,id):
    if request.method=='POST':
        task= tasks.objects.get(pk=id)
        if task.status ==0 :
            task.status =1
            task.save()
            print('completed')
            return HttpResponseRedirect('/')
        else:
            print('rejected')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        
        
def delete(request,id):
    if request.method=='POST':
        task= tasks.objects.get(pk=id)
        task.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

        