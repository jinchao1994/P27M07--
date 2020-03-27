from django.urls import path
from . import views

urlpatterns = [
#当接到主url后转到自身url，拼接自身url后便是客户访问的url
    path('cpu/',views.cpu,name='index'),
    path('free/',views.free,name='index'),
    path('ip/',views.ip,name='index'),
    path('ping/',views.ping,name='index'),

]

