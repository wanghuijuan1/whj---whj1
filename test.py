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