# -*- coding:utf-8 -*-
# Author: xueminchao
# @Time: 2019-09-11 10:11

"""
生成随机密码
1.要求输入次数
2. 要求密码必须包含大写字母、小写字母和数字,长度至少8位，不能重复
"""

import random,string

def wite_file(list_passwd):
    with open('passwd.txt','w') as f:
        for i in list_passwd:
            f.write(i+'\n')
    pass

def  generator(number):
    src = string.ascii_letters + string.digits

    count = number
    list_passwds =[]
    for i in range(int(count)):
        list_passwd_all = random.sample(src,5) #从字母和数字中随机取出5位
        list_passwd_all.extend(random.sample(string.digits,1))  #让密码中一定要包含数字
        list_passwd_all.extend(random.sample(string.ascii_lowercase,1)) # 让密码中一定要包含小写字母
        list_passwd_all.extend(random.sample(string.ascii_uppercase,1))  # 让密码中一定包含大写字母
        random.shuffle(list_passwd_all)   #打乱顺序
        str_passwd = ''.join(list_passwd_all)  # 将列表转化为字符串
        if str_passwd not in list_passwds:
            list_passwds.append(str_passwd)


    wite_file(list_passwds)
    print(list_passwds)

if __name__ == '__main__':
    count = input('请确认要生成几条密码: ')
    generator(count)
