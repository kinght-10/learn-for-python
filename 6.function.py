# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:46:19 2017

@author: ycb
"""
#通过help(abs)查看abs函数的帮助信息
help(abs)

#调用abs函数,如果传入的参数数量和类型不对，会报TypeError的错误
print abs(100)
print abs(-20)
print abs(12.34)

#比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1
print cmp(1,2)
print cmp(1,1)
print cmp(2,1)

#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print int(12.34)
print int('123')
print float('12.34')
print str('1.23')
print unicode(100)
print bool(1)
print bool('')

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a=abs
print a(-1)

#自定义一个求绝对值的my_abs函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
   
print my_abs(-1)

#如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass

#实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
age=20
if age>=18:
    pass

#如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别
print my_abs('A')
#print abs('A')

#让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print my_abs(1)

#在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x,y

#Python函数返回的仍然是单一值
r= move(100, 100, 60, math.pi / 6)
print r

#除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数
#使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5,3)

#定义n=2为默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#利用可变参数，我们把函数的参数改为可变参数,在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

print calc(1,2,3,4)

#如果已经有一个list或者tuple，要调用一个可变参数
num=[1,2,3]
print calc(*num)

#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw

#关键字参数有什么用？它可以扩展函数的功能,如果调用者愿意提供更多的参数，我们也能收到
person('Mike',30)
person('Bob',35,city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

#可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

#参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b',x=99)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args,**kw)

#如果一个函数在内部调用自身本身，这个函数就是递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print fact(5)

#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)

#python并没有对递归进行优化，还是会栈溢出
print fact(1000)

