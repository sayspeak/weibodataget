
import requests
import json
import xlwt


class getMSG:
    def __init__(self):
        self.url = 'http://data.weibo.com/index/ajax/getdefaultattributealldata?'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Cookie': 'WEB3=58d2b12dc53cd1764c5a65500ce67947; _s_tentry=www.baidu.com; UOR=www.baidu.com,data.weibo.com,www.baidu.com; Apache=3972838287088.076.1517499225392; SINAGLOBAL=3972838287088.076.1517499225392; ULV=1517499225396:1:1:1:3972838287088.076.1517499225392:; WBStorage=c5ff51335af29d81|undefined; PHPSESSID=p400j009q6t9h7iq184ttunio0; open_div=close',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'data.weibo.com',
            'Referer': 'http://data.weibo.com/index/attribute',
            'X-Requested-With': 'X-Requested-With'}

    def getdata(self, data):
        self.html = requests.get(self.url, params=data, headers=self.header)
        json_obj = self.html.text
        j = json.loads(json_obj)
        sex = j['data']['sex']['key2']
        age = j['data']['age']['key2']['0']
        tag = j['data']['tag']['key2']['0']
        star = j['data']['star']['key2']['0']
        result = (sex,age,tag,star)
        print(result)

        def readExcel(file):
            with open(file, 'r', encoding='utf8') as fr:
                data = json.loads(fr)
            return data

        def writeM():
            a = result.__str__()

            title = ["女", "男", "电影名", "0-12", "12-18", "19-24", "25-34", "35-50", "other", "名人明星", "视频音乐", "旅游", "娱乐",
                     "美食",
                     "天秤座", "天蝎座", "金牛座", "射手座", "处女座", "水瓶座", "摩羯座", "双子座", "双鱼座", "巨蟹座", "白羊座", "狮子座"]
            book = xlwt.Workbook()
            sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)
            for i in range(len(title)):
                sheet.write(0, i, title[i])
            for line in a:
                sheet.write(int(line), 0, line)
                for i in range(len(a[line])):
                    sheet.write(int(line), i + 1, a[line][i])
            book.save('weibo.xls')


getmsg = getMSG()
data = {'__rnd': 1517543281126}
getmsg.getdata(data)

