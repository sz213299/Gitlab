import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'BIDUPSID=3DAC9C6A21C200FB91915F6B945477BE; PSTM=1712899555; BAIDUID=60530FEB48F0D5C01D60468DAA95D8CB:FG=1; H_WISE_SIDS=60336_60346; H_PS_PSSID=60446; BA_HECTOR=agal0h2g0h258l8g018005a18ohln81j971gk1v; H_WISE_SIDS_BFESS=60336_60346; delPer=0; PSINO=2; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=60530FEB48F0D5C01D60468DAA95D8CB:FG=1; ZFY=:BbDOQp3097RTZ3bSHGeLJgVttHEyJ8HED9FPkREFkfw:C; ab_sr=1.0.1_MzY0ZGMzNDg0ZThjZjY5NGI3MmJhN2NmYTM3YjM3NmI0YmIxNjUxNzA0ZjA0ZGExODBkODQ0OTAwZDY5ZGZiNWMyYjcxNGIwN2E5ZmVkY2Q2MDQ5MGM1N2Q0ZDQ5NGMxM2NlYjExNGU0ZDg0NjFhYTRmMTY2NDQ5NWI0ZDhiNjQwMDY1NzE4ZWEwODJhMzhiYjQ1NGQ5ZDM4YjJlNzNhOTE4OGIwMDA0OWNkZWQ4N2YzYTQ2MmNmZjdhNDIwYmVhYjQ3Y2UxYjZmMmUxYzE2Nzc2ZDExYzEyNThkZjU0MGY=; RT="z=1&dm=baidu.com&si=80433f5a-3472-44ad-b015-5c155d77685e&ss=lylaocdx&sl=8&tt=dwd&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5bl5"',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/mtpe-individual/multimodal?query=d&lang=en2zh',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
s=input("请输入你要翻译的英文单词")
data = {
    'kw':s,
}
url='https://fanyi.baidu.com/sug'
response = requests.post(url, headers=headers, data=data)
print(response.json())