# -*-coding:UTF-8-*-
# 参考：http://www.cnblogs.com/yinzx/p/4658533.html
# str 和 unicode 都继承自basestring， 但是二者又有所不同

print(isinstance("hello", str))         # True
print(isinstance(u"hello", str))        # False
print(isinstance(u"hello", unicode))    # True


print(isinstance("hello", basestring))      # True
print(isinstance(u"hello", basestring))     # True

