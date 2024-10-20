import requests

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://guba.eastmoney.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "qgqp_b_id": "5a63818dc21a1e0b121e0b10cd80f5f2",
    "websitepoptg_api_time": "1729150697295",
    "st_si": "08454107437369",
    "st_asi": "delete",
    "st_pvi": "51955186751946",
    "st_sp": "2024-10-17%2015%3A38%3A17",
    "st_inirUrl": "https%3A%2F%2Fwww.google.com%2F",
    "st_sn": "3",
    "st_psi": "20241017154032778-117001314791-6205963564"
}
url = "https://push2.eastmoney.com/api/qt/ulist.np/get"
params = {
    "fltt": "2",
    "np": "3",
    "ut": "a79f54e3d4c8d44e494efb8f748db291",
    "invt": "2",
    # 翻页 参数
    "secids": "1.603019,1.600611,0.300418,0.300311,1.600622,0.300735,0.000002,0.000617,0.000066,0.000628,0.001696,0.301522,0.002457,0.301297,0.300077,0.002130,1.603038,1.600519,0.830799,1.601211",
    "fields": "f1,f2,f3,f4,f12,f13,f14,f152,f15,f16",
    # "cb": "qa_wap_jsonpCB1729151061487"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
