'''
按转jsonpath


'''
from jsonpath import jsonpath
# 提取数据方法
# ret=jsonpath(a,'jsonpath语法规则字符串')

# 拉勾网
import requests

url='https://search.douban.com/movie/subject_search?search_text=%E5%8A%A8%E7%94%BB&cat=1002'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
print(response.text)