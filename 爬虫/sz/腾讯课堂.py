import requests
from lxml import etree
import json
from jsonpath import jsonpath

url = 'https://ke.qq.com/course/list/%E5%85%AD%E6%98%9F'

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
res = json.loads(response.text)
resu = jsonpath(res, '$..agency_name')
print(resu)
