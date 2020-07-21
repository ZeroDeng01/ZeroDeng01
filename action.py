# -*- coding:utf-8 -*-
import time  # 引入time模块
import http.client
import json
import os



updatetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
mtime = ""
gntotal = ""
asymptomNum = ""
econNum = ""



updatetimeStart = "<!--updatetime start-->"
updatetimeEnd = "<!--updatetime end-->"

mtimeStart = "<!--mtime start-->"
mtimeEnd = "<!--mtime end-->"

gntotalStart = "<!--gntotal start-->"
gntotalEnd = "<!--gntotal end-->"

asymptomNumStart = "<!--asymptomNum start-->"
asymptomNumEnd = "<!--asymptomNum end-->"

econNumStart = "<!--econNum start-->"
econNumEnd = "<!--econNum end-->"



con = http.client.HTTPConnection('interface.sina.cn')
con.request("GET", "/news/wap/fymap2020_data.d.json")
res = con.getresponse()
rd = res.read()
jd = json.loads(rd)

mtime = jd['data']['mtime']
gntotal = jd['data']['gntotal']
asymptomNum = jd['data']['asymptomNum']
econNum = jd['data']['econNum']

# print(updatetime)
# print(mtime)
# print(gntotal)
# print(asymptomNum)
# print(econNum)


def mark(startTag,endTag,oldStr,insertStr):
    start = oldStr.find(startTag)+len(startTag)
    end = oldStr.find(endTag)
    if(start<0 or end<0):
        return oldStr
    s = end-start
    newString = oldStr[:start]+insertStr+oldStr[end:]
    return newString


f = open('README.md', 'r', encoding='UTF-8')
md = f.read()
md = mark(updatetimeStart,updatetimeEnd,md,updatetime)
md = mark(mtimeStart,mtimeEnd,md,mtime)
md = mark(gntotalStart,gntotalEnd,md,gntotal)
md = mark(asymptomNumStart,asymptomNumEnd,md,asymptomNum)
md = mark(econNumStart,econNumEnd,md,econNum)
f.flush()
f.close()

f = open('README.md', 'w', encoding='UTF-8')
f.write(md)
f.flush()
f.close()

print("the end")

