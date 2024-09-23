from django.db import models
from django.core import validators
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100,validators=[validators.MinLengthValidator(limit_value=2)])
    content = models.TextField(validators.MinLengthValidator(limit_value=3))
    # 指定==  true可以不用传值
    created_time = models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=19,blank=True)  #只代表表单验证是空，不代表数据库可以为空