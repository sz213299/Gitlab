from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ma import result
from selenium.webdriver.common.action_chains import ActionChains  # 事件

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 软等待
driver.get("https://www.bilibili.com/")
# time.sleep(0.5)
# 点击登录
driver.find_element(By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div[2]/div/div/div[2]').click()
# time.sleep(0.5)
# 输入账号密码
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/form/div[1]/input').send_keys("13149106384")
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/form/div[3]/input').send_keys("2132998280")
# time.sleep(0.5)
# 登录
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[4]/div[2]/div[2]/div[2]').click()
time.sleep(1)
# 验证码 截图
tu = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[6]/div')
# 是使用 Python 的 pyautogui 库中的 screenshot 函数。它会捕捉当前屏幕的图像，并将其保存为名为 "tu.png" 的文件
tu.screenshot("tu.png")
# 识别验证码
for i in result.split('|'):
    x, y = i.split(",")
    x = int(x)
    y = int(y)
    # 开始点选
    ActionChains(driver).move_to_element_with_offset(tu, xoffset=x, yoffset=y).click().perform()
    time.sleep(0.5)
driver.find_element(By.XPATH, '/html/body/div[20]/div[2]/div[6]/div/div/div[3]/a/div').click()
time.sleep(0.5)
