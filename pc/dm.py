# 导入时间模块
import time

# 导入数据请求模块 (需要安装)
# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入自动化键盘操作
from DrissionPage.common import Keys, Actions

from password import account, Password

# 导入制表模块 (需要安装)

dp = ChromiumPage()
dp.get('https://kyfw.12306.cn/otn/leftTicket/init')
# 打开浏览器
dp = ChromiumPage()
# 访问网站
dp.get('https://kyfw.12306.cn/otn/leftTicket/init')
ac = Actions(dp)
"""通过元素定位, 输入相关信息"""
# 输入出发城市
dp.ele('css:#fromStationText').clear()  # 清空
ac.move_to('#fromStationText').click().type('changchun')
dp.ele('css:#fromStationText').input(Keys.ENTER)  # 回车
# 输入目的城市
dp.ele('css:#toStationText').clear()
ac.move_to('#toStationText').click().type('harbinger')
dp.ele('css:#toStationText').input(Keys.ENTER)  # 回车
# 输入出发时间
dp.ele('css:#train_date').clear()
dp.ele('css:#train_date').input('2024-10-09')
# 点击查询按钮
dp.ele('css:#query_ticket').click()
# 点击预定
dp.ele(f'css:#queryLeftTable tr:nth-child(1) .btn72').click()

dp.ele('css:#J-userName').input(account)  # 输入账号
dp.ele('css:#J-password').input(Password)  # 输入密码
dp.ele('css:#J-login').click()  # 点击登陆
time.sleep(1)
dp.ele('css:#id_card').input('3576')  # 输入身份证后四位
dp.ele('css:#verification_code').click()  # 点击获取验证码
code = input('请输入验证码:')
dp.ele('css:#code').input(code)  # 输入验证码
dp.ele('css:#sureClick').click()  # 点击确定

time.sleep(2)
# 选择乘车人
dp.ele('css:#normalPassenger_0').click()
# 提交订单
dp.ele('css:#submitOrder_id').click()
# 座位选择
time.sleep(2)
# 确认订单
dp.ele('css:#qr_submit_id').click()
