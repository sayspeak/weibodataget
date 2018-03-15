import requests
import json
def getjson(data):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
              'Cookie': 'WEB3=58d2b12dc53cd1764c5a65500ce67947; _s_tentry=www.baidu.com; UOR=www.baidu.com,data.weibo.com,www.baidu.com; Apache=3972838287088.076.1517499225392; SINAGLOBAL=3972838287088.076.1517499225392; ULV=1517499225396:1:1:1:3972838287088.076.1517499225392:; WBStorage=c5ff51335af29d81|undefined; PHPSESSID=p400j009q6t9h7iq184ttunio0; open_div=close',
              'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
              'Connection': 'keep-alive',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Host': 'data.weibo.com',
              'Referer': 'http://data.weibo.com/index/attribute',
              'X-Requested-With': 'X-Requested-With'}
    url = requests.get(url='http://data.weibo.com/index/ajax/getdefaultattributealldata?', params=data, headers=header)
    json_obj = url.text
    j = json.loads(json_obj)
    return j
data = {'__rnd': 1517922900558}
file = open('weibo.json','w',encoding='utf-8')
json.dump(getjson(data),file,ensure_ascii=False)
file.close()
print(getjson(data))
'Accept':'*/*',
Accept-Encoding
gzip, deflate
Accept-Language
zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection
keep-alive
Content-Type
application/x-www-form-urlencoded
Cookie
UOR=www.baidu.com,data.weibo.c…ge=c5ff51335af29d81|undefined
Host
data.weibo.com
Referer
http://data.weibo.com/index/attribute
User-Agent
Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/58.0
X-Requested-With
XMLHttpRequest