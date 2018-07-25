#-*- coding:utf-8 _*-
"""
@author:Sam
@file: urls.py
@time: 2018/07/{DAY}
"""

from django.urls import path
from django_web import  views
from django.conf.urls import url
urlpatterns = [
    #path('user',views.user_info)
    url('^user',views.user_info)
]