from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.settings import api_settings
from django.http import HttpResponse
from jwt import ExpiredSignatureError, PyJWTError, InvalidTokenError


class JwtAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 建立一个白名单
        while_list = ["/user/login"]
        path = request.path
        print(path)
        if path not in while_list and not path.startswith("/media"):

            print("token验证")
            token = request.META.get('HTTP_AUTHORIZATION')
            print('token', token)

            try:
                # 异常验证，总共三种情况
                # jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
                jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

                jwt_decode_handler(token)
            except ExpiredSignatureError:
                return HttpResponse('Token过期，请重新登录')
            except InvalidTokenError:
                return HttpResponse('Token验证失败')
            except PyJWTError:
                return HttpResponse('Token验证异常')

        else:
            print("不要要token验证")
            return None
