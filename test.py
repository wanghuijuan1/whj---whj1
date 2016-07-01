# -*- coding:utf-8 -*-
import random
import requests
from faker import Factory
fake=Factory.create('zh_CN')
print fake.ssn() #生成随机验证码


def foo():
    "这个是用来写一大串注视的"
    return True

#**是乘方运算
miles=1000.0
kilometers=1.369*miles
print '%f miles is the same as %f km '%(miles,kilometers)  #%试用实现字符串的替换功能  %s字符串替换 %f 浮点数替换 %d整数替换


#for 每次迭代一个元素
aqdEvents=[x**2 for x in  range(8) if not x%2]
for i in aqdEvents:
    print i

#打开文件，显示文件的内容
filename=raw_input('Enter file name:')
fobj=open(filename,'r')  # fobj=open('D:\districtcode.txt','r')
for eachLine in fobj:
    print eachLine
fobj.close()

#函数定义 def关键字、函数名、函数需要的几个参数 用：结束
def addMe2Me(x):
    'apply+operation to argument'
    return (x+x)
addMe2Me(10)
print addMe2Me(10)

