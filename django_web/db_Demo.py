#-*- coding:utf-8 _*-
"""
@author:Sam
@file: db_Demo.py
@time: 2018/07/{DAY}
"""
'''
    python  manage.py  makemigrations以及python   manage.py  migrate

'''
from django_web.models import bookInfo
#from django.utils import timezone
from  datetime import *

#插入数据到数据库
book = bookInfo()
book.book_title="java"
book.book_datatime=datetime(year=2018,month=4,day=5)
book.save()
#查询：查看数据库的字段
bookInfo.objects.all()[0].book_title
