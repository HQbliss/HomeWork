# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 21:37:17 2018

@author: AS-US
"""

input("欢迎查看天气预报情况！")
import urllib.request as r
city=input("请输入想要查看的城市:")
add='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
infor=r.urlopen(add.format(city)).read().decode('utf-8','ignore')
print(infor)

import json
qingkuang=json.loads(infor)

print("1.查看当前城市天气，2.退出查询")
men=input("请输入菜单: ")

if men=="1":
    print("1.查看当前城市天气")
    print()
    print("这个城市是: "+str(qingkuang['city']['name']))
    print("该城市的人口是: "+str(qingkuang['city']['population']))
    
    a1=qingkuang['list'][19]['dt_txt']
    print("现在时间是："+str(a1))
    
    a2=qingkuang['list'][19]['main']['temp_max']
    print("最高温度是："+str(a2))
    
    a3=qingkuang['list'][19]['main']['temp_min']
    print("最低温度是："+str(a3))
    
    a4=qingkuang['list'][19]['main']['pressure']
    print("当前气压是："+str(a4))
    
    a5=qingkuang['list'][19]['weather'][0]['description']
    print("当前天气是："+str(a5))
    print('.................................')
    
    
    a1=qingkuang['list'][30]['dt_txt']
    print("现在时间是："+str(a1))
    
    a2=qingkuang['list'][30]['main']['temp_max']
    print("最高温度是："+str(a2))
    
    a3=qingkuang['list'][30]['main']['temp_min']
    print("最低温度是："+str(a3))
    
    a4=qingkuang['list'][30]['main']['pressure']
    print("当前气压是："+str(a4))
    
    a5=qingkuang['list'][30]['weather'][0]['description']
    print("当前天气是："+str(a5))
    print('.................................')
    
    
    a1=qingkuang['list'][38]['dt_txt']
    print("现在时间是："+str(a1))
    
    a2=qingkuang['list'][38]['main']['temp_max']
    print("最高温度是："+str(a2))
    
    a3=qingkuang['list'][38]['main']['temp_min']
    print("最低温度是："+str(a3))
    
    a4=qingkuang['list'][38]['main']['pressure']
    print("当前气压是："+str(a4))
    
    a5=qingkuang['list'][38]['weather'][0]['description']
    print("当前天气是："+str(a5))
    print('.................................')
    
if men=="2":
    print("2.退出查询")
input('欢迎使用，谢谢！')
