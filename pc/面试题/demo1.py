import requests

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://deal.ggzy.gov.cn",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://deal.ggzy.gov.cn/ds/deal/dealList.jsp",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
cookies = {
    "JSESSIONID": "9b56bc1ec18acadd4c0836aab95b",
    "insert_cookie": "38171867"
}
url = "http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp"
data = {
    "TIMEBEGIN_SHOW": "2024-10-05",
    "TIMEEND_SHOW": "2024-10-14",
    "TIMEBEGIN": "2024-10-05",
    "TIMEEND": "2024-10-14",
    "SOURCE_TYPE": "1",
    "DEAL_TIME": "02",
    "DEAL_CLASSIFY": "00",
    "DEAL_STAGE": "0000",
    "DEAL_PROVINCE": "0",
    "DEAL_CITY": "0",
    "DEAL_PLATFORM": "0",
    "BID_PLATFORM": "0",
    "DEAL_TRADE": "0",
    "isShowAll": "1",
    "PAGENUMBER": "1",
    "FINDTXT": ""
}
response = requests.post(url, headers=headers, data=data, verify=False)

print(response.text)
print(response)
