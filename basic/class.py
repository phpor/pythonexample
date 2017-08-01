# coding=utf-8


class A:  # 类定义前最好保留两个空行,注释也不要有的空行
    """
    Only a test class；
        这里是类文档字符串，用三个双引号，虽然三个单引号也没错，但是约定使用三个双引号
        这些文字可以通过 __doc__ 来引用这个类文档
        类的属性没有文档
    """

    name = ""

    def __init__(self, name="phpor"):  # 构造函数
        self.name = name

    def say(self):              # 函数名只用小写字符，看起来好看，很多人也使用大写的
        print("My name is " + self.name)

    def _pri(self):             # 下划线开头的方法约定为私有方法，解释器不强制阻止调用
        print("Don't call me :" + self.name)

    def this_is_self(this):     # 第一个参数取名为self，约定而已，不管叫啥，实质上都是self，python没有self关键字，好的IDE会强烈推荐使用self
        print("Me is " + this.name)

    def can_be_static(self):    # 如果方法体中没有用到self变量，则，IDE可能会提示 maybe a static
        print("This method shuld be a static, because it not use self")

    @staticmethod
    def new(name):  # 静态方法是靠注解实现的
        return A(name)


# 对象属性 和 类属性
"""
对象属性
    __class__

类属性：
    __name__
    __doc__
"""
print(A("phpor").__class__)  # __main__.A
print(A("phpor").__class__.__name__)  # A
print(A.__name__)  # A
print(A.__doc__)
print(A("phpor").__doc__)  # 这里引用到的是类的文档
print(A.name.__doc__)  # 所以这里引用的将不是属性的文档，而是属性所属类的文档

# 对象方法调用
print("--------- only a  spitter line -------")
A("phpor").say()  # 不需要 new 关键字
A("phpor")._pri()  # 下划线前缀仅仅是个约定，编译器会给出提示，但是解释器没有强制阻止


class B(A):
    """
    B is sub class of A
    """

    def run(self):
        print(self.name + " is running")

    @staticmethod
    def fake_static(self):  # IDE 会将这个假的self和真的self用颜色区分开来
        print("This is not self, it only argument " + self)


B.fake_static(": don't use self as not a self")
print(B.__doc__)