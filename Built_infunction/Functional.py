# enumerate() ���� ,ȡ��������Ԫ�ر���

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


#����map()��������һ��list���������ɲ��淶��Ӣ�����֣����һ�������淶Ӣ�����ֵ�list��
def format_name(s):
    s = s[0].upper() + s[1:].lower()
    return s
print(list(map(format_name, ['adam', 'LISA', 'barT'])))




#����recude()�������
from functools import reduce
def prod(x,y):
    return x*y

print(reduce(prod,[2,4,5,7,12]))





#��filter()���˳�1~100��ƽ��������������
def is_sqr(x):
    num = int(x**0.5)

    return x and num*num == x


print(list(filter(is_sqr,list(range(1,101)))))