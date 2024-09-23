import requests

url = 'https://v.qq.com/x/cover/mzc00200l8h0d9p/y00471ce6rc.html?report_recomm_player=ptag%3Dv_qq_com%7Crtype%3D%7CalgId%3D%7CbucketId%3D%7Creason%3D%7CreasonType%3D%7Ccid%3D%7Cvid%3D%7Cpid%3D%7Cmodule%3D%7CpageType%3DfilmIndex%7Cseqnum%3D'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referrer': 'https://film.qq.com/',
    # 省略了Cookie，因为它可能包含敏感信息且不是必要的（除非网站要求）
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html = response.text  # 这里已经是解码后的字符串了
    print(html)  # 直接打印字符串
else:
    print(f"请求失败，状态码：{response.status_code}")