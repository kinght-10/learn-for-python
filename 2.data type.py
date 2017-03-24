# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:49:07 2017

@author: ycb
"""

#''或""括起来的是字符串，如果要输出'或者"用转义字符\
print "I'm OK"
print"I'm \"OK\""

#转义字符\n,\t,r''里面的字符不转义
print 'I\'m learning\nPython.'
print '\\\n\\'
print '\\\t\\'
print r'\\\t\\'

#Python允许用'''...'''的格式表示多行内容
print '''line1
line2
line3'''

#布尔值true、false
print True
print False
print 2>3
print 3<5

#布尔值可以用and、or和not运算
print True and False
print True or False
print not False

#变量名必须是大小写英文、数字和_的组合，且不能用数字开头,可以赋值数字，字符串，布尔值
a=1
t_007='asm'
answer=True
print(a,t_007,answer)

#python是动态语言，变量可以赋值不同变量类型
a=1
a='ABC'
print a

#Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换
print ord('A')
print chr(65)

#写u'中'和u'\u4e2d'是一样的，\u后面是十六进制的Unicode码
print u'中文'
print u'\u4e2d'

#把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')

#英文字符转换后表示的UTF-8的值和Unicode值相等,而中文字符转换后1个Unicode字符将变为3个UTF-8字符
print len('ABC')
print len(u'ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

#把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法
print 'abc'.decode('utf-8')
print  '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#输出格式化的字符串:
print 'Hello,%s' % 'world'
print  'Hi, %s, you have $%d.' % ('Michael', 1000000)


#其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print '%2d-%02d' % (3,1)
print '%.2f' % 3.1415926