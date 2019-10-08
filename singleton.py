#单例模式，多线程版

import threading
class Singleton(object):
    _instance_lock =  threading.Lock()  #加锁
    def __init__(self):
        time.sleep(1)

    def __new__(cls,*args,**kwargs):
        if not hasattr(Singleton,"_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton,"_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t. start()
    

# 基于metaclass 实现
class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass=SingletonType):
    def __init__(self,name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1,obj2)

