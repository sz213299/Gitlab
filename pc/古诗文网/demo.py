import requests

headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "^cookie": "login=flase; Hm_lvt_9007fab6814e892d3020a64454da5a55=1729249447; HMACCOUNT=44707BBC8DDB2E5E; ticketStr=203997549^%^7cgQFv8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAydUhET1FObGVkN2kxZUdkVmhEMWsAAgSqQBJnAwQAjScA; ASP.NET_SessionId=235vorowvol5qx0qebvbl1ad; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1729249500; codeyz=fc4e6baa8350631b^",
    "priority": "i",
    "referer": "https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx",
    "^sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
url = "https://www.gushiwen.cn/RandCode.ashx"
response = requests.get(url, headers=headers)

with open("code.png", "wb") as f:
    f.write(response.content)
