import requests
import re
import execjs

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://guba.eastmoney.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://gbcdn.dfcfw.com/rank/popularityList.js"
params = {
    "type": "0",
    "sort": "0",
    "page": "1",  # 分页参数
    "v": "2024_10_17_15_1"
}
response = requests.get(url, headers=headers, params=params)

data = response.text
# print(data)
test = re.findall(r"popularityList='(.*?)'", data)[0]
# print(test)
# 读取js代码
jscode = open('./demo.js', 'r', encoding='utf-8').read()
# 加载                        js封装的的函数 传的参数
scriptData = execjs.compile(jscode).call('main123', test)

list = []
for i in scriptData:
    list.append(i['code'])
t123 = ','.join(list)

# 加载                        js封装的的函数 传的参数
secids = execjs.compile(jscode).call('getHQSecIdByMutiCode', t123)
# print(secids)

# 发送新请求
para = {
    "fltt": "2",
    "np": "3",
    "ut": "a79f54e3d4c8d44e494efb8f748db291",
    "invt": "2",
    # 翻页 参数
    "secids": secids,
    "fields": "f1,f2,f3,f4,f12,f13,f14,f152,f15,f16",
    # "cb": "qa_wap_jsonpCB1729151061487"
}
urls = "https://push2.eastmoney.com/api/qt/ulist.np/get"
response = requests.get(urls, headers=headers, params=para)
data = response.json()['data']['diff']
for item in data:
    print(item)
