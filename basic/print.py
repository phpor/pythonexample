# encoding=utf-8

""" 如何输出不换行 """
print 1     # 输出并换行
print 1,    # 通过添加逗号实现不换行的输出


print(1)    # 1
print(1,)   # （1,) 相当于 print (1,)

# python 3 中只有print函数，要想不换行，使用第二个参数end="" , 如下
'''
from __future__ import print_function
print(1, end="")
'''

""" 输出格式化 """

print("%10s%10s%-10s" % (1, 2, 3))
