import re,request

import requests

url = "https://www.douban.com/doulist/3936288/"

payload = {}
headers = {
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"accept-language": "zh-CN,zh;q=0.9",
		"cache-control": "max-age=0",
		"^cookie": "ll=^^118371^^; bid=vbEf9jfJIuM; _pk_id.100001.8cb4=57428e8e36ed98b7.1717295244.; __yadk_uid=D4L2RAfmU5OlGpqNlwZjIGKWaPC3hpWL; __utmc=30149280; _pk_ref.100001.8cb4=^%^5B^%^22^%^22^%^2C^%^22^%^22^%^2C1721052732^%^2C^%^22https^%^3A^%^2F^%^2Fwww.baidu.com^%^2Flink^%^3Furl^%^3DjkIpZrl0ik0iQQW6I7HOBv6MVdOWHfZnHjSV6asMN78OC9okZjlazTQ-VtBfR0Ln8BJ9Vyjh-C-WE-MRqpvLS_^%^26wd^%^3D^%^26eqid^%^3Dd1201fe70011360f0000000266952e27^%^22^%^5D; _pk_ses.100001.8cb4=1; ap_v=0,6.0; __utma=30149280.1562125738.1717294875.1720946501.1721052732.6; __utmz=30149280.1721052732.6.6.utmcsr=baidu^|utmccn=(organic)^|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1721052732^",
		"priority": "u=0, i",
		"referer": "https://www.baidu.com/link?url=jkIpZrl0ik0iQQW6I7HOBv6MVdOWHfZnHjSV6asMN78OC9okZjlazTQ-VtBfR0Ln8BJ9Vyjh-C-WE-MRqpvLS_&wd=&eqid=d1201fe70011360f0000000266952e27",
		"^sec-ch-ua": "^^Not/A)Brand^^;v=^^8^^, ^^Chromium^^;v=^^126^^, ^^Google",
		"sec-ch-ua-mobile": "?0",
		"^sec-ch-ua-platform": "^^Windows^^^",
		"sec-fetch-dest": "document",
		"sec-fetch-mode": "navigate",
		"sec-fetch-site": "cross-site",
		"sec-fetch-user": "?1",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

response = requests.request("GET", url, headers=headers, data=payload)
obj=re.compile(r' <div class="source">.*?<div class="title">(?P<name>.*?)</div>',re.S)
obj=obj.finditer(response.text)
for item in obj:
	print(item.group("name"))
# print("REDTYUIOPIUYFDGHUJI")



# print(response.text)text