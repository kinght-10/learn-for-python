# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:38:16 2017

@author: ycb
"""

#如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做
age=20
if age>=18:
    print 'Your age is',age
    print 'adult'

#也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
age=3
if age>=18:
    print 'Your age is',age
    print 'adult'
    
else:
    print 'your age is', age
    print 'teenager'
    
#当然上面的判断是很粗略的，完全可以用elif做更细致的判断
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
   
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x=1
if x:
    print 'True'
    
#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
#所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name    

#再比如我们想计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum

#Python提供一个range()函数，可以生成一个整数序列
sum = 0
for x in range(101):
    sum = sum + x
print sum

#从raw_input()读取的内容永远以字符串的形式返回，把字符串和整数比较就不会
#得到期待的结果，必须先用int()把字符串转换为我们想要的整型
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'    










