import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

drive = webdriver.Edge()
drive.get('https://www.zhipin.com/')
drive.implicitly_wait(8)

drive.find_element(By.CLASS_NAME, 'ipt-search').send_keys('python')
drive.find_element(By.CLASS_NAME, 'btn-search').click()
time.sleep(2)  # 等待搜索结果加载

data_list = []  # 在外部初始化


def Job():
    lis = drive.find_elements(By.CSS_SELECTOR, '.job-card-body')
    for i in lis:
        name = i.find_element(By.CLASS_NAME, 'company-name').text
        price = i.find_element(By.CLASS_NAME, 'salary').text
        home = i.find_element(By.CLASS_NAME, 'job-area').text
        jishu = i.find_element(By.CLASS_NAME, 'tag-list').text.replace('\n', ' | ')
        url = i.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

        print(f'公司名称是 :{name}\n工资是 :{price}\n地址是 :{home}\n技术要求 :{jishu}\n链接是 :{url}')

        data_list.append({
            '公司名称': name,
            '工资': price,
            '链接': url,
            '要求': jishu,
            '地址': home
        })


for page in range(1, 11):
    print(f"开始第{page}页")
    print("*****************")
    Job()
    # 翻页
    next_button = drive.find_element(By.CLASS_NAME, 'ui-icon-arrow-right')
    if next_button:
        next_button.click()
    time.sleep(2)  # 等待下一页加载
    print("=====================")
    print(f"第{page}页搜索完毕")

# 写入 JSON 文件
with open('boss.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data_list, ensure_ascii=False))

with open('boss.csv', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data_list, ensure_ascii=False))

print("保存完毕")
drive.quit()
