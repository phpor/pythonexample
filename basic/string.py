# -*-coding:UTF-8-*-
# 参考：http://www.cnblogs.com/yinzx/p/4658533.html
# str 和 unicode 都继承自basestring， 但是二者又有所不同

print(isinstance("hello", str))         # True
print(isinstance(u"hello", str))        # False
print(isinstance(u"hello", unicode))    # True


print(isinstance("hello", basestring))      # True
print(isinstance(u"hello", basestring))     # True

string = "Hello world"

print(string[:3])           # 0,1,2
print(string[1:3])          # 1,2

print(string[3:])           # 3,...
print(string * 2)           # 循环2次
print(string + string)      # 字符串连接
