# -*-coding:UTF-8-*-

# encode和decode都是针对unicode进行“编码”和“解码”，所以encode是unicode->str的过程，decode是str->unicode的过程；
# decode 的作用是将其他编码的字符串转换成 Unicode编码，eg
# name.decode(“GB2312”)，表示将GB2312编码的字符串name转换成Unicode编码
# encode 的作用是将Unicode编码转换成其他编码的字符串，eg
# name.encode(”GB2312“)，表示将GB2312编码的字符串name转换成GB2312编码


name = u"超级飞侠"   # 中文字符最好转成unicode再赋值，否则encode成其他编码就报错哦
print(name)
print(name.encode("GB2312"))
print(name.encode("GB2312").decode("gb2312"))  # 编码名称大小写不敏感

# ### len 函数 ######
# 对于unicode编码，len函数返回字符个数
# 对于非unicode编码，len函数返回字节数
# 参考： http://www.cnblogs.com/yinzx/p/4658533.html
print(len(name))   # 4
print(len(name.encode("GB2312")))  # 8


