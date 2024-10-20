#  访问主页面  .m3u8  读取文件下载  ts  文件
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from lxml import etree


def get_iframe_src(driver):
    iframe = driver.find_element(By.XPATH, '//td[@id="playleft"]//iframe')
    return iframe.get_attribute("src")


def main():
    url = 'https://www.k8dy.net/index.php/vod/play/id/97112/sid/1/nid/1.html'
    driver = webdriver.Chrome()
    driver.get(url)
    iframe_src = get_iframe_src(driver)
    if iframe_src:
        print(iframe_src)
    driver.quit()


if __name__ == '__main__':
    main()
