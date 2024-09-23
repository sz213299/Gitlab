import requests
from lxml import etree
url='https://www.zbj.com/sem/index?pmcode=137535808&utm_source=bdpz&utm_medium=SEM'

response=requests.get(url)
html=etree.HTML(response.text)
print(html)
content=html.xpath('/html/body/div[1]/div[5]/div[4]/div/div/div//text()')
print(content)