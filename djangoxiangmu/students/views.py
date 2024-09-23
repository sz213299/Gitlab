import uuid

from django.db.migrations import serializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
# 这是api导入的一个包
from rest_framework.views import APIView

import students
from students.models import User, Student
from django.views.generic import TemplateView


# 403错误 首先改成CBV 叫做Class Base View 基于类型的视图
# restFul开发风格，是一种约定
# restful规定，返回的数据是字符串，这个字符串必须遵循json格式
# python的list 是json的array
# python的DICtionary，就是json的object
# jsonArray = 【23123，313，131，31，31，31，31，‘dada’,{'eq':23}】
# jsonObject = {}


# class mainview(APIView):
#     def get(self, request, *args, **kwargs):
#         print(request)
#         print(args)
#         print(kwargs)
#
#         # return HttpResponse('CBV的视图')
#         return JsonResponse({"code": 0, "msg": "请求方法不支持"})
#
#     def post(self, request, *args, **kwargs):
#         account = request.POST["account"]
#         pwd = request.POST["pwd"]
#         try:
#             u = User.objects.get(account=account, password=pwd)
#             session = request.session
#             session["account"] = account
#             return JsonResponse({"code": 1, "msg": "登陆成功"})
#         except User.DoesNotExist as e:
#             return JsonResponse({"code": 2, "msg": "用户名密码错误"})


class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        # return HttpResponse('CBV的视图')
        return JsonResponse({"code": 0, "msg": "请求方法不支持"})

    def post(self, request, *args, **kwargs):
        account = request.POST["account"]
        pwd = request.POST["pwd"]
        try:
            u = User.objects.get(account=account, password=pwd)
            session = request.session
            session["account"] = account
            return JsonResponse({"code": 1, "msg": "登陆成功"})
        except User.DoesNotExist as e:
            return JsonResponse({"code": 2, "msg": "用户名密码错误"})


class StudentSerializer(serializers.ModelSerializer):
    # 验证谁写谁
    def validate_realName(self, *args, **kwargs):
        realName = args[0]
        if len(realName) < 2:
            raise serializers.ValidationError("真实姓名小于2")
        else:
            return realName

    class Meta:
        model = Student
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=32, required=True)
    password = serializers.CharField(max_length=32, required=True)
    role = serializers.IntegerField(required=True)

    def validate_account(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("账号长度必须超过六")
        else:
            return value

    def create(self, validated_data):
        account = validated_data.pop("account")
        password = validated_data.pop("password")
        role = validated_data.pop("role")
        user = User.objects.create(account=account, password=password, role=role)
        return user


class StudentView(APIView):

    def get(self, request, *args, **kwargs):
        result = Student.objects.all()
        # 序列化
        # l = [str(x) for x in result]
        serializers = StudentSerializer(result, many=True)
        return JsonResponse({"code": 1, "data": serializers.data, "msg ": "查询成功"})

    # 确定添加方法
    def post(self, request, *args, **kwargs):
        if request.POST.get('pro') == '1':

            account = request.POST["account"]
            pwd = request.POST["pwd"]
            us = UserSerializer(data={"account": account, "password": pwd, "role": 3})
            user = None
            if us.is_valid():
                user = us.save()
            else:
                print(us.errors)
            # User.objects.create(account=account, password=pwd, role=3)
            # u = User.objects.get(account=account)
            realName = request.POST["realName"]
            gender = request.POST["gender"]
            college = request.POST["college"]
            clazz = request.POST["clazz"]
            # 反序列化
            print(user)
            serializer = StudentSerializer(
                data={"realName": realName, "gender": gender, "college": college, "clazz": clazz, "uid": user.id})
            if serializer.is_valid():
                # save
                serializer.save()
                return Response({"code": 1, "msg": "添加成功"})
            else:
                # Student.objects.create(realName=realName, gender=gender, college=college, clazz=clazz, uid=u.id)
                return Response({"code": 2, "msg": serializer.errors})

        elif request.POST.get('pro') == '2':
            uids = request.POST["id"]
            uuid = [int(x) for x in uids.split(",")]
            for uid in uuid:
                # 使用Django的ORM查询User模型，查找ID为uid的用户对象。
                # filter方法返回的是一个查询集（QuerySet），即使只有一个结果。
                user = User.objects.filter(id=uid)
                # 使用Django的ORM查询Student模型，获取ID为uid的学生对象。
                # get方法用于获取单个对象，如果找不到对象会抛出异常。
                student = Student.objects.get(id=uid)
                student.delete()
                user.delete()
                return Response({"code": 1, "msg": "删除成功"})
            return Response({"code": 2, "msg": "删除失败"})

            # uids = request.POST["id"]
            # uuid=[int(x) for x in uids.split(",")]
            # for uid in uuid:
            #     user = User.objects.filter(id=uid)
            #     student = Student.objects.get(id=uid)
            #     student.delete()
            #     user.delete()
            #     return Response({"code": 1, "msg": "删除学生"})
            # return Response({"code": 0, "msg": "删除失败"})
