import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://xueqiu.com",
    "priority": "u=1, i",
    "referer": "https://xueqiu.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
cookies = {
    "cookiesu": "901728822450297",
    "device_id": "b7b56b0bbad8deefc4f5118c3f063bf6",
    "xq_a_token": "f84a0b79c9e449cb1003cb36412faa34001a6697",
    "xqat": "f84a0b79c9e449cb1003cb36412faa34001a6697",
    "xq_r_token": "b24e38a4224932f5c7abd28126e8fc377b42755b",
    "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTczMTgwNDgwNiwiY3RtIjoxNzI5MjQ4NjUwNzIxLCJjaWQiOiJkOWQwbjRBWnVwIn0.EukdXd6iomvVm6PueSS0XCkMr8GUNXLgUkfl2gAVY2GiDytcZ_WsASUpF07lG0AlA231PSv7whOMDCp-dMIiURM3nM7dyLEnoRiQRA5HKA5gFzyOQMgpZawoaq98KUDzz8i4NkA8K8tUJM9G-0nDdL_ErR1GWUHzjpt9TneXJWAaEz3KI_JLxhWf25zxa1o91_XYE75BQc7cGbaTlq6UWKCDjLeraNy0MnNlgOLFcSThAtKbplB49_3qcc_ubQE6Ms5sF39QPjm9hHrBJXOkLLxwfUvAnt101esNsEfJDP06xuBGvLb0dWrSpSJAwKRPz_56yTHQsqUVx45o5IkEtQ",
    "u": "901728822450297",
    "Hm_lvt_1db88642e346389874251b5a1eded6e3": "1728822452,1729248704",
    "HMACCOUNT": "44707BBC8DDB2E5E",
    "s": "ao17v8bmko",
    "Hm_lpvt_1db88642e346389874251b5a1eded6e3": "1729248811",
    "ssxmod_itna": "Yq+x0iq7qGqQu4BcDB+ht+e0=qitqDn00imBPK6Ex05xi=rDSxGKidDqxBWmZA2eqqzOBcdFe1Aoe3FzCeRPuAh9iGpxjT+DB3DEx0=Y8RDYY1Dt4DTD34DYDiEQGIDieDFCTXUkDbxYQDYqGRDB=0GqDfIqGWCq=DmMNDGwKXD7QDIdtqDDNqDPxPCGx5LudY5lbDAuhSQ2=DjdTD/SP8=06oLZFqRLtH=hrFiL04xBQD7kiyDYo0Um+B9w2o+bmYD8DK+BY4CGDKi2D5WYpv4oe4lGGrnAZ=33mHWHwj6yDDGbhMoiD===",
    "ssxmod_itna2": "Yq+x0iq7qGqQu4BcDB+ht+e0=qitqDn00imBPK6xn93h+xDseQqDLQDWuIZLlKqk34Ou2I73W7dn=5RWi7Oux2RgOoNYaaITE+xLDQIQDLxiQq4D"
}
url = "https://stock.xueqiu.com/v5/stock/screener/quote/list.json"
params = {
    "page": "1",
    "size": "10",
    "type": "sha",
    "order_by": "percent",
    "order": "desc"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
