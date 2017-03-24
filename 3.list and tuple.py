# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:19:55 2017

@author: ycb
"""

#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
classmates=['Mike','Bob','Tracy']
print classmates
print len(classmates)

#要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1
print classmates[0]
print classmates[1]
print classmates[2]
print classmates[-1]

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print classmates

#也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'Jack')
print classmates

#要删除list末尾的元素，用pop()方法
classmates.pop()
print classmates

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(3)
print classmates

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1]='Sarsh'
print classmates

#list里面的元素的数据类型也可以不同
L=['apple',1,True]
print L

#list元素也可以是另一个list,要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组
s=['python', 'java', ['asp', 'php'], 'scheme']
print s
print s[2][1]

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print classmates

#括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
#这种情况下，按小括号进行计算，计算结果自然是1
t=(1)
n=(1,)
print t,n

#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = ('a', 'b', ['A', 'B'])
t[2][0]='X'
t[2][1]='Y'
print t




