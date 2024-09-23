import requests
import re
import json
from pprint import pprint




# url='https://xy39x164x247x107xy.mcdn.bilivideo.cn:8082/v1/resource/1563754770-1-30232.m4s?agrr=1&build=0&buvid=0BE24B1A-20A5-BF34-7625-CD3D90E633CF78508infoc&bvc=vod&bw=11510&deadline=1717330427&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=A0020000&mcdnid=50003771&mid=1682764729&nbs=1&nettype=0&og=cos&oi=2087883938&orderid=0%2C3&os=mcdn&platform=pc&sign=2a5d2b&traceid=trZPGvFaCKjVPq_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=95f4185994aa558d785d15b832f63e2a'
# url='https://xy39x164x247x113xy.mcdn.bilivideo.cn:8082/v1/resource/1563754770-1-30232.m4s?agrr=1&build=0&buvid=0BE24B1A-20A5-BF34-7625-CD3D90E633CF78508infoc&bvc=vod&bw=11510&cdnid=4309&deadline=1717332835&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=80000000&mid=1682764729&nbs=1&nettype=0&og=cos&oi=2087883938&orderid=0%2C3&os=bcache&platform=pc&sign=2a5d2b&traceid=trEuiXvlkJDpno_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=103662e1154c5763d237d956d375cc9c'
# url=' https://xy39x166x162x12xy.mcdn.bilivideo.cn:8082/v1/resource/1563754770-1-30232.m4s?agrr=0&build=0&buvid=0BE24B1A-20A5-BF34-7625-CD3D90E633CF78508infoc&bvc=vod&bw=11510&deadline=1717333619&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv2&logo=A0020000&mcdnid=50003771&mid=1682764729&nbs=1&nettype=0&og=cos&oi=2087883938&orderid=0%2C3&os=mcdn&platform=pc&sign=2b73c1&traceid=tryJwqLXAWwpKI_0_e_N&uipk=5&uparams=e%2Cuipk%2Cnbs%2Cdeadline%2Cgen%2Cos%2Coi%2Ctrid%2Cmid%2Cplatform%2Cog&upsig=2ef132b8757d6d65cb5ca8f536565b49'

url = 'https://www.bilibili.com/video/BV1d7421d7Mg/?spm_id_from=333.1007.tianma.5-2-16.click&vd_source=a26fdfb04c2189a36ffb2ce6f147255d'
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 '
               'Safari/537.36',

           'Referrer': 'https://www.bilibili.com/video/BV1d7421d7Mg/?spm_id_from=333.1007.tianma.5-2-16.click&vd_source=a26fdfb04c2189a36ffb2ce6f147255d',

           # 'Cookie': 'buvid3=0BE24B1A-20A5-BF34-7625-CD3D90E633CF78508infoc; b_nut=1713623478; _uuid=A38E4817-7CA2-7F3D-E151-7CE71BDFD63579103infoc; buvid_fp=13958665f978b6a63d4203df65df09cf; buvid4=64931FB7-E8D5-8E37-6745-08D10A00317B79857-024042014-AmiPP3yGrXrFB3T5gSXK5WBPuSx4RVUP1vc%2BMmuP5lBptqPt1DRsw0D72d5wEN%2Bg; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; home_feed_column=5; DedeUserID=1682764729; DedeUserID__ckMd5=852a806e4c7d59fe; rpdid=0zbfVH6QPW|1KRlKOYy|2UY|3w1RYbLm; PVID=1; b_lsid=DFB2F985_18FD85D22EF; bsource=search_baidu; header_theme_version=CLOSE; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; SESSDATA=b7ab9f3f%2C1732873936%2C6b998%2A61CjC5M1Hv5QHlA4hzdv0D4Y8-YfjD61AKfw6G527nHmQt-5oUHGAKV8ZEh01Iel5EENwSVk5nd25aeFhweDFDSWN1TXZQaFB5RHJZT3dFNFVmMklwOFJ6cXREVk1yMVlwaGVfSnp1QkN5WUpYTEliZUQ3WWhpZl9WbDBwOEVMQmd0V3FSR0ZDaElBIIEC; bili_jct=783a1407d019bf703f21530c5a75d638; CURRENT_BLACKGAP=0; sid=77i1eooi; CURRENT_FNVAL=4048; browser_resolution=1494-307; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTc1ODExNzcsImlhdCI6MTcxNzMyMTkxNywicGx0IjotMX0.OjR6mvUDp2ybftLguA1WW5kqkR0hM0bxUQMi8oMVhFE; bili_ticket_expires=1717581117; bp_t_offset_1682764729=937271153761714181'

           }

response = requests.get(url, headers=headers)
html = response.text
print(html)
# 解析数据，提取标题
title = re.findall('<h1 data-title="(.*?)" class="video-title', html)[0]

# 提取视频信息内容
video_info = re.findall('<script>window.__playinfo__=(.*?)</script>', html)[0]

# json字符串转成json字典数据
json_data = json.loads(video_info)

# 字典取值，音频链接
audio = json_data['data']['dash']['audio'][0]['baseUrl']
# 视频画面链接
video = json_data['data']['dash']['video'][0]['baseUrl']
# 保存数据
audio_content = requests.get(url=audio, headers=headers).content
video_content = requests.get(url=video, headers=headers).content

title = title.replace('"', '').replace(' ', '').replace('title="', '').replace('！！', '') + '.mp3'
with open('sz\\'+title+'.mp3', 'wb') as a:
    a.write(audio_content)
with open('sz\\'+title+'.mp4', 'wb') as v:
    v.write(video_content)


#
# # 请求连接
# link='https://api.bilibili.com/pgc/web/variety/feed?cursor=0&page_size=14'
# # 发送请求
# link_data=requests.get(url=link, headers=headers).json()
# # 循环
# for i in link_data:
#     print(i)


print(title)
print(video)
print(audio)

# 合并 ffmprg软件，配置环境变量

