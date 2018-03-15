import requests
import json
def getjson(data):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
              'Cookie': 'UOR=www.baidu.com,data.weibo.com,www.baidu.com; SINAGLOBAL=3972838287088.076.1517499225392; ULV=1517922880487:3:3:2:7853918774313.802.1517922880481:1517826048657; WEB3=16eecaac1b039ffa98ceae90acb175f9; _s_tentry=www.baidu.com; Apache=7853918774313.802.1517922880481; PHPSESSID=7gd6eebsjthr4839vo396v1ot3; WBStorage=c5ff51335af29d81|undefined',
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
    sex = j['data']['sex']['key2']
    age = j['data']['age']['key2']['0']
    tag = j['data']['tag']['key2']['0']
    star = j['data']['star']['key2']['0']
    return [sex,age,tag,star]
def writejson(jsonobj):
    file = open('weibo.json', 'w', encoding='utf-8')
    json.dump(jsonobj, file, ensure_ascii=False)
    file.close()
data = {'__rnd': 1517922900558}      # 歌曲名字id  url中在__rnd之后的id信息，变更id则能够爬取不同电影数据
writejson(jsonobj = getjson(data))
