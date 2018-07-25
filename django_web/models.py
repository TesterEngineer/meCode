from django.db import models
#from mongoengine import  *

# Create your models here.
class bookInfo(models.Model):
    book_title=models.CharField(max_length=28)
    book_datatime=models.DateTimeField()
    def __str__(self):
        return "这是bookInfo的数据model"


class user(models.Model):
    loginname=models.CharField(max_length=50,default=None)
    loginname=models.CharField(max_length=50,default=None)
    email=models.CharField(max_length=50)
    status=models.IntegerField()
    activationCode= models.CharField(max_length=64)