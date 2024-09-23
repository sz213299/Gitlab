'''
1.异步加载
像网站进行一次请求，一次直传部分数据
2.豆瓣电影
'''
import  requests
#
# url='https://movie.douban.com/explore'
#
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}


# response = requests.get(url, headers=headers)
# print(response.text)

# 文本数据分类
# 结构化相应内容
# json字符串：可以使用re/json模块来提取特定的数据
# xml字符串，可以使用re/lxml来提取特定的数据
# 给结构化相应内容

# html字符串可以使用re/lxml模块来提取特定的数据

import  json
# python数据转换成json
dic={"name":"你好"}

dic2=json.dumps(dic,ensure_ascii=False)
print(type(dic2))


# json转换成python

js=json.loads(dic2)
print(type(js))