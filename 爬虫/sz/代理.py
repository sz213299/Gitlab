import requests
#
# url = 'https://2024.ip138.com/'
#
# headers = {'User-Agent':
#                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
#
# # 构建代理，代理ip无效自动用真实ip,如果有效显示地址，无效报错
# proxies = {
#     # 第一种写法
#     'https':'113.223.213.43'
#     #     第二种写法
#     #     'http':'http://172.16.17.32:9527'
# }
#
# res=requests.get(url, headers=headers, proxies=proxies)
# print(res.content.decode())

# retrying模块 -------通过装饰器方式实现
from retrying import retry
# @retry(stop_max_attempt_number=3)
# def test():
#     print('123')
#     url='https://www.baidu.com/'
#     response=requests.get(url)
#     print(response.content.decode())
#
# try:
#     test()
#
# except:
#     print("已完成")


# timeout 参数 超时参数

url='https://www.baidu.com/'

request=requests.get(url,timeout=2)  #设置超时时间，两秒内返回相应
print(request.content.decode())










