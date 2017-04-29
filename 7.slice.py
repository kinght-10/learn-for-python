# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:48:05 2017

@author: ycb
"""

L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2

print L

#取一个list或tuple的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print [L[0],L[1],L[2]]

#取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
r=[]
n=3
for i in range(n): 
    r.append(L[i])
print r

#Python提供了切片（Slice）操作符
print L[0:3]
#如果第一个索引是0，还可以省略
print L[:3]
print L[1:3]
#既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print L[-2:]
print L[-2:-1]

L=range(100)
print L
print L[0:10]
#倒数第一个元素的索引是-1
print L[-10:-1]
print L[10:20]
#前10个数，每两个取一个,最后一个参数为间隔
print L[0:10:2]
print L[::5]
#甚至什么都不写，只写[:]就可以原样复制一个list
print L[:]

#tuple也可以用切片操作，只是操作的结果仍是tuple
print (0,1,2,3,4,5)[:3]

#字符串也可以用切片操作，只是操作结果仍是字符串
print 'ABCDEFG'[:3]







