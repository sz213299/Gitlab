import time
import re
import os
import json
import requests
import urllib3
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pypinyin import pinyin, Style

# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 代理设置
proxies = {
    "http": "http://172.16.24.25:7001",
    "https": "http://172.16.24.25:7001",
}

# 请求头
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://ciyuandao.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# 创建浏览器选项
options = Options()
options.add_argument('--no-proxy-server')
options.add_argument('--proxy-server="DIRECT"')
driver = webdriver.Chrome(options=options)

# 获取明星名字并转换为拼音
tt = input('请输入你要搜索的明星: ')
ttt = ''.join([item[0] for item in pinyin(tt, style=Style.NORMAL)])


def sanitize_filename(filename):
    """清理文件名中的非法字符"""
    return re.sub(r'[\/:*?"<>|\\]', '_', filename)


def download_image(src, filename):
    """下载图片"""
    if os.path.exists(filename):
        print(f'文件已存在: {filename}')
        return
    for attempt in range(3):  # 尝试下载3次
        try:
            img_src = requests.get(src, headers=headers, timeout=10, verify=False).content
            with open(filename, mode='wb') as f:
                f.write(img_src)
            print(f'下载完成: {filename}')
            return
        except requests.exceptions.RequestException as e:
            print(f'下载失败: {e}, 正在重试 {attempt + 1}/3...')
            time.sleep(2)


# 遍历每一页
for page in range(1, 6):
    driver.get(f'https://com.okmzt.net/photo/model/{ttt}/page/{page}/')
    print(f'*********开始第{page}页********')

    # 等待图片加载
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//img')))

    # 获取图片和名字
    names = [h2.text for h2 in driver.find_elements(By.XPATH, '//h2')]
    srcs = [img.get_attribute('data-src').replace('450', '960') for img in driver.find_elements(By.XPATH, '//img')]

    dir_path = f'{tt}'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    for num, (name, src) in enumerate(zip(names, srcs), start=1):
        clean_name = sanitize_filename(name)  # 清理文件名
        filename = os.path.join(dir_path, f'{clean_name}_{page}.jpg')
        print(f'准备下载文件: {filename}')  # 打印准备下载的文件名
        print("|"
              "|")
        download_image(src, filename)  # 调用下载函数

print('全部完成')
