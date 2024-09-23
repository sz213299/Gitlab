import requests

cookies = {
    'SNUID': '50F0538FFAFDE6CB47334242FBE89796',
    'IPLOC': 'CN5100',
    'SUID': 'AB0AA9746B54A20B000000006693897F',
    'cuid': 'AAHECO9mTQAAAAuiVJewfgAASQU=',
    'SUV': '1720945034478843',
    'browerV': '3',
    'osV': '1',
    'ABTEST': '8|1720945074|v17',
    'sst0': '499',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'SNUID=50F0538FFAFDE6CB47334242FBE89796; IPLOC=CN5100; SUID=AB0AA9746B54A20B000000006693897F; cuid=AAHECO9mTQAAAAuiVJewfgAASQU=; SUV=1720945034478843; browerV=3; osV=1; ABTEST=8|1720945074|v17; sst0=499',
    'Referer': 'https://www.sogou.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'query': '周杰伦',
    '_asf': 'www.sogou.com',
    '_ast': '',
    'w': '01019900',
    'p': '40040100',
    'ie': 'utf8',
    'from': 'index-nologin',
    's_from': 'index',
    'sut': '3420',
    'sst0': '1720945084499',
    'lkt': '0,0,0',
    'sugsuv': '1720945034478843',
    'sugtime': '1720945084499',
}

response = requests.get('https://www.sogou.com/web', params=params, cookies=cookies, headers=headers)
print(response.text)