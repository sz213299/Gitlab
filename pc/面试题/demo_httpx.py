import httpx
from bs4 import BeautifulSoup
import json

list = []
for page in range(1, 3):
    print(f'---------开始第{page}页--------')
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://deal.ggzy.gov.cn",
        "Referer": "http://deal.ggzy.gov.cn/ds/deal/dealList.jsp",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    url = "http://deal.ggzy.gov.cn/ds/deal/dealList.jsp"
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
        "PAGENUMBER": f"{page}",
        "FINDTXT": ""
    }

    response = httpx.post("http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp", data=data, headers=headers, timeout=5)
    text = response.json()
    res = text["data"]
    for i in res:
        title = i['title']
        time = i['timeShow']
        src = i['url']
        src = src.replace("/html/a", "/html/b").replace("http", "https")
        try:
            response = httpx.get(
                src, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            tr_text = soup.get_text(separator=" ", strip=True)
            cleaned_text = tr_text.replace("\n", "")

            list.append({
                "标题": title,
                "时间": time,
                "正文链接": src,
                "正文详情": cleaned_text,
            })
        except Exception as e:
            print("正在请求在.........")
            continue

    # 打印结果
    for item in list:
        print(item)
    print('结束')

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(list, f, ensure_ascii=False, indent=4)
print("保存完毕")
