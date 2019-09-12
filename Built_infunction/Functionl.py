# enumerate() 函数 ,取出索引与元素本身

L = ['Admin','Lisa','Bart','Paull']
a = tuple(enumerate(L))

for  i in enumerate(L):
    index = i[0]
    name = i[1]
    print(index, name)

L = (1, 'Lisa')
for index ,name in enumerate(L):
    print(index,name)

a = list(zip([10,20,30],['A','B','C']))

print(a)

#利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
def format_name(s):
    s = s[0].upper() + s[1:].lower()
    return s
print(list(map(format_name, ['adam', 'LISA', 'barT'])))


#利用recude()来求积：
from functools import reduce
def prod(x,y):
    return x*y

print(reduce(prod,[2,4,5,7,12]))

#用filter()过滤出1~100中平方根是整数的数
def is_sqr(x):
    num = int(x**0.5)

    return x and num*num == x

print(list(filter(is_sqr,list(range(1,101)))))
