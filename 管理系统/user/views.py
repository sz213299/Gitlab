from django.shortcuts import render
from django.views import View
from rest_framework_jwt.settings import api_settings

from user.models import SysUser, SysUserSerializer
from django.http import JsonResponse


# Create your views here.
class LoginView(View):
    def post(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            user = SysUser.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 载荷
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 解码
            # 将用户对象传进去，获取到搞对象的属性
            paylod = jwt_payload_handler(user)
            # 将属性值编码成jwt格式的字符串
            token = jwt_encode_handler(paylod)
        except Exception as e:
            print(e)
            return JsonResponse({'code': 500, 'info': '用户名或密码错误'})
        # 传入实例化对象，有一个属性data，直接返回实例化对象
        return JsonResponse({'code': 200, 'token': token, 'user': SysUserSerializer(user).data, 'info': '登录成功', })


class TestView(View):
    def get(self, request):
        # 获取token
        token = request.META.get('HTTP_AUTHORIZATION')
        if token is not None and token != '':
            # json  序列还
            userList_obj = SysUser.objects.all()  # 所有用户信息
            user_dict = userList_obj.values()  # 转换为字典
            UserList = list(user_dict)  # 把外层容器转换成列表
            print(UserList)
            return JsonResponse({'code': 200, 'info': '测试', 'data': UserList})
        else:
            return JsonResponse({'code': 401, 'info': '没有访问权限', })


class JwtTestView(View):
    def get(self, request):
        user = SysUser.objects.get(username='sz', password='123456')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 载荷
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 解码
        # 将用户对象传进去，获取到搞对象的属性
        paylod = jwt_payload_handler(user)
        # 将属性值编码成jwt格式的字符串
        token = jwt_encode_handler(paylod)
        return JsonResponse({'code': 200, 'token': token})
