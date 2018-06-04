# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

data=['周一','周二','周三','周四','周五','周六','周天']
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
print(data[6])
print('今天是: '+data[5])

msg={"地址":"北京海定","手机号码":"1838334","寄件人":"leshan"}
print(msg["地址"])
print(msg["手机号码"])
print(msg["寄件人"])

wo={"姓名":"胡琴","身高":"155","性别":"girl","年龄":"1"}
print(wo["姓名"])
print(wo["身高"])
print(wo["性别"])
print(wo["年龄"])

xue={"name": "张韶涵","songs": ['隐形的翅膀','欧若拉'],"nicheng": "张","boyfriend": [1,2,3]}
songs=xue['songs']
print(songs)
print("歌曲数目:"+str(len(songs)))
print(max(xue['boyfriend']))

tianqi={"未来5天的温度":[20,21,23,25],"未来5天的天气":['晴','阴','小雨'],
        "日期":['周一','周二','周三','周四','周五','周六','周天']}
tq=tianqi['未来5天的天气']
print(tq)
print(max(tianqi['未来5天的温度']))

city=input("请输入城市:")
print(city)
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996' 
print(address.format(city))

print("welcome")
print("1.查看当前城市天气，2.查看其他城市天气,3.保存")
menmo=input("请输入菜单: ")
if menmo=="1":
    print("1.查看当前城市天气")
if menmo=="2":
    print("2.查看其他城市天气")
if menmo=="3":
    print("3.保存")
    
#引用其他工具包 import 包名
import urllib.request as r
city=input("请输入城市:")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996' 
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
print(info)

import json
data=json.loads(info)
data['weather'][0]['description']
data['main']['temp_max']
data['main']['pressure']
print("最高温度是："+str(data['main']['temp_max']))
print("最高气压是："+str(data['main']['pressure']))
print("天气情况是："+str(data['weather'][0]['description']),
      "最高温度是："+str(data['main']['temp_max']),
      "最高气压是："+str(data['main']['pressure']))