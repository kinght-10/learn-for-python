# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:15:10 2017

@author: ycb
"""

#只要是可迭代对象，无论有无下标，都可以迭代
d={'a':1,'b':2,'c':3}
for key in d:
    print key

#默认情况下，dict迭代的是key。如果要迭代value可以用
for value in d.itervalues():
    print value
    
#如果要同时迭代key和value，可以用
for k,v in d.iteritems():   
        print k,v

#由于字符串也是可迭代对象，因此，也可以作用于for循环
for ch in 'ABC':
    print ch
    
#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate([1,2,3]):
    print i,value

#同时引用了两个变量，在Python里是很常见的
for x,y in[(1,1),(2,2),(3,3)]:
    print x,y