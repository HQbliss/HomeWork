# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:40:43 2018

@author: lenovo
"""

a,b=3,True
print(b)
score=80
two=100
if score>80 and two==100:
    print("phone")
else:
    print("no pay")
 
    
if 1>2:
    print("1")
elif 2>3:
    print("2")
else:
    print("3")
 
    
#0-60:不及格；60-70：及格；70-90：良；90-100：优秀
fenshu=99
if fenshu>=90:
    print("优秀")
elif fenshu>=70:
    print("良好")
elif fenshu>=60:
    print("及格")
else:
    print("不及格")

#while+break=if
while 1>0:
    print("1")
    break


ls=['当山峰没有棱角的时候','当河水不再流','当时间停住日夜不分','当天地万物化为虚有']
for i in ls:
    print(i)
    

for i in range(1,10):
    print(i)
for i in range(20,10,-3):
    print(i)

yesterday='2016-06-03'
yesterday.index('-')
nian=yesterday[0:4]
yesterday[5:7]
yesterday[8:10]
nian
yesterday.split('-')
fenge=yesterday.split('-')
for i in fenge:
    print(i)
print('a,b,c'.split())
print('a\tb\tc'.split())

i=123456
def test():
    global j
    j=0
    print(j)
test()
print(j)


def sum1(a,b):
    return (int(a)+int(b))
while True:
    a=input("请输入第一个数：")
    b=input("请输入第二个数：")
    sum0=sum1(a,b)
    print("和是："+str(sum0))
    break


#保存文件
open('state.txt','w').write('1')
#读文件
a=open('state.txt','r').readline()
if a=='0':
    print('菜单是：')
else:
    print('欢迎第一次使用，请登记你的名字！')
    print('菜单是：')