from django.db import models
from datetime import datetime


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pub_time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)

    class Meta:
        db_table = 'sz_table'
        ordering = ['-pub_time', 'name']


class Author(models.Model):
    is_active = models.BooleanField()  # 布尔
    username = models.CharField(max_length=100)  # 可变字符
    date_json = models.DateTimeField(auto_now_add=True)  # 保存第一次的数据
    email = models.EmailField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=200, db_column='Tagname')
    created_time = models.DateTimeField(default=datetime.now)
    # 1.可用，2.不可用
    # status=models.SmallIntegerField(default=0)
