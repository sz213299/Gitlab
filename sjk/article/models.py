from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class UserExtension(models.Model):
    birthday=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    user=models.OneToOneField('User',on_delete=models.CASCADE) # 一点一OneToOneField







class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pubtime = models.DateTimeField(auto_now_add=True,null=True)

    # 外键定义  ForeignKey  一对多关系
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    Tags = models.ManyToManyField('Tag', related_name='article')  #多对多 ManyToManyField


class Tag(models.Model):
    name = models.CharField(max_length=100)








class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey('self', on_delete=models.CASCADE)


