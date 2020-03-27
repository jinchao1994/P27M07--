from django.shortcuts import render
#导入http模版，前端显示格式
from django.http import HttpResponse


#定义index函数，由路由指向
def index(request):
    return HttpResponse("<p>Hello world,hello,Django</p>")

def cpu(request):
    return HttpResponse("<p>'mycpu is 88% </p>")
def ip(request):
    return HttpResponse("<p>'ip: 192.168.0.120 </p>")
def free(request):
    return HttpResponse("<p>'free is 50%</p>")
def ping(request):
    return HttpResponse("<p>'192.168.0.120‘s ping OK'</p>")

# Create your views here.
