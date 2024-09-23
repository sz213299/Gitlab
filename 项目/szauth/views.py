import string

from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random
# 发送邮件
from django.core.mail import send_mail

from szauth.models import CaptchaModel

from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        pass

def register(request):
    return render(request, 'reg.html')


def send(request):
    # ?emila=xxx
    email=request.GET.get('email')
    if not email:
        return JsonResponse({"code":400,"message":'必须传递参数'})
            # 生成验证码，4为随机验证码
    # ['0','2','9','8']
    captcha="".join(random.sample(string.digits,4))
    # 存储数据库中
    CaptchaModel.objects.update_or_create(email=email,defaults={"captcha":captcha})
    print(captcha)
    # from_email = '2132998280@qq.com'  # 或者使用 DEFAULT_FROM_EMAIL，如果你已经设置了
    send_mail("知了博客验证码", f"你的验证码是:{captcha}",recipient_list=[email],from_email=None)
    return JsonResponse({"code": 200, "message": "邮件发送成功"})


