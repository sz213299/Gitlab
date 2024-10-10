"""
[课程内容]: Python实现12306查票购票程序 https://kyfw.12306.cn/otn/leftTicket/init

[授课老师]: 青灯教育-自游  [上课时间]: 20:05  可以点歌 可以问问题

[环境使用]:
    Python 3.10
    Pycharm

[模块使用]:
    requests --> pip install requests
    prettytable --> pip install prettytable
    DrissionPage --> pip install DrissionPage

素材: 找木子老师微信: python10010 领取
    city.json 城市文件
---------------------------------------------------------------------------------------------------
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信: python10010
---------------------------------------------------------------------------------------------------

案例分为两部分:
    1. 查票:
    2. 购票
cookie:
    1. 重新复制新的cookie
    2. cookie多的字段: 主要校验是那个从参数
        - 逆向分析cookie如何生成的
某些网站cookie是动态:
    比如: 同花顺股票: v boss __zp_token__
"""
# 导入json模块
import json
# 导入时间模块
import time

# 导入数据请求模块 (需要安装)
import requests
# 导入自动化模块
from DrissionPage import ChromiumPage
# 导入自动化键盘操作
from DrissionPage.common import Keys, Actions
# 导入制表模块 (需要安装)
from prettytable import PrettyTable
from pypinyin import pinyin, Style

from password import account, Password


def change(chinese):
    text = pinyin(chinese, style=Style.NORMAL)
    string = ''.join([t[0] for t in text])
    return string


def Buy(FromCity, ToCity, Date, Num):
    # 打开浏览器
    dp = ChromiumPage()
    # 访问网站
    dp.get('https://kyfw.12306.cn/otn/leftTicket/init')
    ac = Actions(dp)
    """通过元素定位, 输入相关信息"""
    # 输入出发城市
    dp.ele('css:#fromStationText').clear()  # 清空
    ac.move_to('#fromStationText').click().type(change(FromCity))
    dp.ele('css:#fromStationText').input(Keys.ENTER)  # 回车
    # 输入目的城市
    dp.ele('css:#toStationText').clear()
    ac.move_to('#toStationText').click().type(change(ToCity))
    dp.ele('css:#toStationText').input(Keys.ENTER)  # 回车
    # 输入出发时间
    dp.ele('css:#train_date').clear()
    dp.ele('css:#train_date').input(Date)
    # 点击查询按钮
    dp.ele('css:#query_ticket').click()
    # 点击预定
    dp.ele(f'css:#queryLeftTable tr:nth-child({2 * int(Num) - 1}) .btn72').click()
    """判断是否有登陆账号"""
    text = dp.ele('css:#login_user').text
    if text == '登录':
        """输入账号密码"""
        time.sleep(1)
        dp.ele('css:#J-userName').input(account)  # 输入账号
        dp.ele('css:#J-password').input(Password)  # 输入密码
        dp.ele('css:#J-login').click()  # 点击登陆
        time.sleep(1)
        dp.ele('css:#id_card').input('4512')  # 输入身份证后四位
        dp.ele('css:#verification_code').click()  # 点击获取验证码
        code = input('请输入验证码:')
        dp.ele('css:#code').input(code)  # 输入验证码
        dp.ele('css:#sureClick').click()  # 点击确定
    else:
        pass

    time.sleep(2)
    # 选择乘车人
    dp.ele('css:#normalPassenger_1').click()
    # 提交订单
    dp.ele('css:#submitOrder_id').click()
    # 座位选择

    # 确认订单
    dp.ele('css:#submitOrder_id').click()


"""用户输入: 出发地+目的地+出发时间"""
from_city = input('请输入你要出发城市: ')
to_city = input('请输入目的城市: ')
# date = input('请输入时间: ')
train_date = '2024-10-09'
# 读取城市文件
f = open('city.json', encoding='utf-8').read()
# 把json字符串转成json字典
city_data = json.loads(f)
"""发送请求"""
# 模拟浏览器
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "If-Modified-Since": "0",
    "Referer": "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E5%8C%97%E4%BA%AC,BJP&ts=%E6%9D%AD%E5%B7%9E,HZH&date=2024-10-08&flag=Y,N,Y",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "_uab_collina": "172838620598742326612636",
    "JSESSIONID": "E136F7D5AB89D05247B7B29267CE7293",
    "tk": "WwdbmuQvddpGmwfugj2T4-ZUgXPTALrGcWA0nkja4WsozS1S0",
    "BIGipServerotn": "2162688266.64545.0000",
    "BIGipServerpassport": "803733770.50215.0000",
    "guidesStatus": "off",
    "highContrastMode": "defaltMode",
    "cursorStatus": "off",
    "route": "c5c62a339e7744272a54643b3be5bf64",
    "uKey": "7aa8e96488fbee7821328fd807fb81b4535a5285f498c32bfc8a24a3de8faa0d",
    "_jc_save_fromDate": "2024-10-08",
    "_jc_save_toDate": "2024-10-08",
    "_jc_save_wfdc_flag": "dc",
    "_jc_save_fromStation": "%u6210%u90FD%2CCDW",
    "_jc_save_toStation": "%u897F%u5B89%2CXAY"
}
# 请求网址
url = f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={train_date}&leftTicketDTO.from_station={city_data[from_city]}&leftTicketDTO.to_station={city_data[to_city]}&purpose_codes=0X00'
# url = f'https://kyfw.12306.cn/otn/leftTicket/queryG?leftTicketDTO.train_date={date}    &leftTicketDTO.from_station={city_data[from_city]}&leftTicketDTO.to_station={city_data[to_city]}&purpose_codes=0X00'
# 发送请求
response = requests.get(url=url, headers=headers, cookies=cookies)
"""获取数据"""
# 获取响应的json数据
json_data = json.loads(response.text)
"""解析数据"""
# 提取车次信息所在result列表
result = json_data['data']['result']
# 实例化对象
tb = PrettyTable()
# 设置字段名
tb.field_names = [
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '特等座',
    '一等',
    '二等',
    '软卧',
    '硬卧',
    '硬座',
    '无座',
]
# 定义变量名
page = 1
# for循环遍历, 提取列表里面元素
for i in result:
    # 字符串分割 -> 返回列表
    index = i.split('|')
    num = index[3]  # 车次
    start_time = index[8]  # 出发时间
    end_time = index[9]  # 到达时间
    use_time = index[10]  # 耗时
    topGrade = index[32]  # 特等座
    first_class = index[31]  # 一等
    second_class = index[30]  # 二等
    hard_sleeper = index[28]  # 硬卧
    hard_seat = index[29]  # 硬座
    no_seat = index[26]  # 无座
    soft_sleeper = index[23]  # 软卧
    tb.add_row([
        page,
        num,
        start_time,
        end_time,
        use_time,
        topGrade,
        first_class,
        second_class,
        soft_sleeper,
        hard_sleeper,
        hard_seat,
        no_seat,
    ])
    page += 1

print(tb)
page_num = input('请输入你要购买车次序号: ')
Buy(FromCity=from_city, ToCity=to_city, Date=train_date, Num=page_num)
