# 封装
class Foo:

    def __init__(self, name='wulal', age=23, gender='男'):
        self.name = name
        self.age = age
        self.gender = gender
    
    def kanchai(self):
        print("%s,%s岁,%s,上山去砍柴"%(self.name, self.age, self.gender))

    def qudongbei(self):
        print("%s,%s岁,%s,开车去东北"%(self.name, self.age, self.gender))

    def dabaojian(self):
        print("%s,%s岁,%s,最爱大保健"%(self.name, self.age, self.gender))

xiaoming = Foo()
xiaoming.kanchai()
xiaoming.qudongbei()
xiaoming.dabaojian()
laowang = Foo(name='laowang',gender='女')
laowang.kanchai()
laowang.dabaojian()


# 继承


#字段
class Province():

    contry = 'china'

    def __init__(self, name):
        self.name = name

obj = Province('hebei')
print(obj.name)
print(Province.contry)

# 方法与属性
class Fangfa():

    def __init__(self,name):
        self.name = name

    @property
    def price(self):
        return ('wulala')
# 普通方法
    def ord_func(self):
        print('普通方法')

    @staticmethod
    def static_func():
        print('静态方法')

    @classmethod
    def class_func(cls):
        print('类方法')

f = Fangfa('wulala')
f.ord_func()
Fangfa.class_func()
Fangfa.static_func()
print(f.price)

class Goods(object):

    def __init__(self):
        self.originnal_price = 100
        self.discount = 0.8

    @property
    def price(self):
        new_price = self.originnal_price*self.discount
        return new_price
    
    @price.setter
    def price(self,value):
        self.originnal_price = value

    

goods = Goods()
goods.price
goods.price = 200

# 公有静态资源
class C():

    name = '公有静态资源'
    __name = '私有静态资源'

    def func(self):
        print(C.name)
        print(C.__name)
class D(C):
    def sow(self):
        print(C.name)
        
C.name # 类访问
c = C()
c.func()
D.name
d = D()
d.sow()
