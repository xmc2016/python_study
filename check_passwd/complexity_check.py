# -*- coding:utf-8 -*-
# Author: xueminchao
# @Time: 2019-09-11 9:55

# 密码复杂性检查
import  re

# 检查特征
NUMBER  = re.compile(r'[0-9]')     #数字
LOWER_CASE = re.compile(r'[a-z]')  #小写
UPPER_CASE = re.compile(r'[A-Z]')  #大写
OTHERS = re.compile(r'[^0-9a-zA-Z]')  #其他字符

#  强度的属性,是否是有效密码(valid),强度(strength),友好的提示信息(message)
class Strenth:
    def __init__(self,valid,strength,message):
        self.valid = valid
        self.strength = strength
        self.message = message
        print(valid, strength,message)


#加载密码本
def load_common_password():
    words = []
    with open('passwd.txt','r') as f:
        for word in f.readlines():
            words.append(word.strip())
    return words
COMMON_WORDS = load_common_password()

class Password:
    # 密码等级
    TERRIBLE = 0
    SIMPLE = 1
    MEDIUM = 2
    STRONG = 3

    @staticmethod
    # 判断密码顺序是否为键盘顺序
    def is_reqular(input):
        revser = input[::-1]
        regular = ''.join(['qwertyuiop','asdfghjkl','zxcvbnm'])
        return input in regular or revser in regular

    @staticmethod
    # 判断密码顺序是否为ASCII码顺序
    def is_by_step(input):
        delta = ord(input[1]) -ord(input[0])

        for i in range(2,len(input)):
            if ord(input[i]) - ord(input[i-1]) != delta:
                return False
        return True

    @staticmethod

    def is_common(input):
        return input in COMMON_WORDS


    def __call__(self,input,min_length=6,min_types=3,leverl=STRONG):
        if len(input) < min_length:
            return Strenth(False,'terrible','密码太短了')

        if self.is_reqular(input) or self.is_by_step(input):
            return Strenth(False,'simple','密码有规则')

        if self.is_common(input):
            return Strenth(False,'simple','密码很常见')

        types = 0

        if NUMBER.search(input):
            types  +=1

        if LOWER_CASE.search(input):
            types += 1


        if UPPER_CASE.search(input):
            types +=1

        if OTHERS.search(input):
            types +=1

        if types < 2:
            return Strenth(leverl <= self.SIMPLE,'simple','密码太简单了')

        if types < min_types:
            return Strenth(leverl <= self.MEDIUM, 'medium','密码不错')

        return Strenth(True,'strong','完美的密码')






a=Password()
a("123Cd")









