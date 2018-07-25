from django.contrib import admin
from .models import bookInfo
# Register your models here.



#admin.site.register(Question, managerAdmin)


class managerAdmin(admin.ModelAdmin):
    list_display = ['id','book_title','book_datatime']
    list_filter = ['book_title']
    #查询的字段
    search_fields = ['book_title']

admin.site.register(bookInfo,managerAdmin)