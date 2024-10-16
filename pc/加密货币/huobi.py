import requests

PROXY = {
    "http": "http://36.158.107.38:8085",  # 示例端口
    "https": "http://36.158.107.38:8085"  # 示例端口
}

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-ts": "1728800402750",
    "encryption": "true",
    "language": "zh",
    "origin": "https://www.coinglass.com",
    "priority": "u=1, i",
    "referer": "https://www.coinglass.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
url = "https://capi.coinglass.com/api/openInterest/info"
params = {
    "symbol": "ETH"
}
response = requests.get(url, headers=headers, params=params, proxies=PROXY)

print(response.text)
print(response)
