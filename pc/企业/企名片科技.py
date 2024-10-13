import json

import requests
import execjs

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://research.qmpsee.com",
    "Referer": "https://research.qmpsee.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://wyiosapi.qimingpian.cn/web/webSiteCaNews"

# 表单 或请求体
data = {
    "page": "4",
    "num": "8",
    "type": "榜单"
}
#  动态接口
#  第三方库 执行post请求

response = requests.post(url, headers=headers, data=data)

# print(response.text)
encrypt_data = json.loads(response.text)['encrypt_data']
# utf-8 gbk字节不一样                                              执行call('Z') Z是方法  encrypt_data是传参数
text = execjs.compile(open('./qiye.js', 'r', encoding='utf-8').read()).call('Z', encrypt_data)
for i in text['list']:
    print(i)
