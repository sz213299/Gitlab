from django.db import models


# Create your models here.
class User(models.Model):
    account = models.fields.CharField(max_length=32, unique=True, null=False)
    password = models.CharField(max_length=32, null=False)
    role = models.BigIntegerField(null=False)

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户名'
        verbose_name_plural = verbose_name
        ordering = ['account']
    #     新建表使用命令  python manage.py makemigrations 文件迁移，出现creat student就是好的 然后使用后python manage.py migrate


class Student(models.Model):
    realName = models.CharField(max_length=32, null=False)
    gender = models.CharField(max_length=2)
    college = models.CharField(max_length=32, null=False)
    clazz = models.CharField(max_length=32, null=False)
    # 表关联
    uid = models.IntegerField(null=False)

    # def __str__(self): str = '"id":"{}","realName":"{}","gender":"{}","college":"{}","clazz":"{}",
    # "uid":"{}"'.format(self.id,self.realName,self.gender,self.college,self.clazz,self.uid)
    # return "{" + str + "}"
    # 序列化与反序列化

    class Meat:
        db_table = 'students_student'
        verbose_name = '学生信息表'
        verbose_name_plural = 'verbose_name'
        ordering = ['id']
