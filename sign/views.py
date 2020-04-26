from django.shortcuts import render
from  django.http import  HttpResponse, HttpResponseRedirect
from django.contrib import  auth
from  django.contrib.auth.decorators import login_required

# 登录页
def index(requset):
    return render(requset,"index.html")
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        #if username=='admin' and password==('123456'):
            #response=HttpResponseRedirect('/event_manage/')
            #response.set_COOKIE('user',username,3600)
        if user is not None:
            auth.login(request,user)
            request.session['user']=username
            response=HttpResponseRedirect('/event_manage/')

            return response
        else:
            return render(request,'index.html',{'error':'login faild， check your account information!'})
#发布会页
@login_required
def event_manage(request):
    #username=request.COOKIES.get('user', '')
    username=request.session.get('user','')
    return render(request,"event_manage.html",{"user":username})