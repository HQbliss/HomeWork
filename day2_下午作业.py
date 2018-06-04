# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:33:11 2018

@author: AS-US
"""

print("欢迎查看城市天气预报情况！")
import urllib.request as r
city=input("请输入想要查看的城市:")

add='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
infor=r.urlopen(add.format(city)).read().decode('utf-8','ignore')

import json
hh=json.loads(infor)
print("1.查看当前城市天气，2.退出查询")
men=input("请输入菜单: ")


if men=="1":
    print("这个城市是: "+str(hh['city']['name']))
    days=range(16,36,2)
    def printhh(hh,day):
        print("现在时间是："+str(hh['list'][day]['dt_txt']))
        print("最高温度是："+str(hh['list'][day]['main']['temp_max']))
        print("最低温度是："+str(hh['list'][day]['main']['temp_min']))
        print("当前气压是："+str(hh['list'][day]['main']['pressure']))
        print("当前天气是："+str(hh['list'][day]['weather'][0]['description']))
        print('.................................')
    for day in days:
        printhh(hh,day)
if men=='2':
    print("退出查询")
input("欢迎使用，谢谢！")

    

