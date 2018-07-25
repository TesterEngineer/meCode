#coding:utf-8
from django.shortcuts import render
from django.http import request,response
from django_web import  models

# Create your views here.
def get_index(request):
    print("-----------------***hello*******--------------")
    s = "hello java"
    print(s)
    return render(request,"index.html")



def user_info(request):
    #在view里面如何去model里面查询出所要的数据,存放起来？？
    userList=models.user.objects.all()
    context={'userList':userList}
    return render(request,"userInfo.html",context)
    #return render(request, "userInfo.html")

