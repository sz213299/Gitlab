'''
sign token cookie 

'''
import requests

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-EncKey": "PVX1OMIJXnLbCrDPGsEk4w==",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Origin": "https://webapi.cninfo.com.cn",
    "Referer": "https://webapi.cninfo.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "MALLSSID": "5A3531716D6354334A315534374970374231434530696E7745386C5774692B68394377415856716D393236384E6854576B6557475879397A6E367A757936326D"
}
url = "https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1120"
params = {
    "ctype": "2",
    "@limit": "5"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params)

print(response.json())
print(response)
