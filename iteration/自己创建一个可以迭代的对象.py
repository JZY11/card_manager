from collections import Iterable

class Classmates(object):
    """要想让一个对象具有可迭代性，第一：该类必须要实现 __iter__ 方法。 第二：__iter__ 方法的返回得要return一个对象的引用"""
    def __init__(self):
        self.names = list() # names 属性指向了 list() 列表

    def add(self, name):
        self.names.append()

    def __iter__(self):
        """如果让一个对象成为一个可以迭代的对象即可以使用for  则必须实现__iter__方法"""
        return ClassIterator()

class ClassIterator(object):
    """通过这个类创建出来的对象就可以当做上面方法__iter__ 的返回"""
    def __iter__(self):
        pass

    def __next__(self):
        pass


classmate = Classmates() # 定义一个实例对象

classmate.add("老二")
classmate.add("老三")
classmate.add("老四")

print("判断classmate是否是可迭代对象：", isinstance(classmate, Iterable)) # 判断对象是否具有可迭代性

for name in classmate:
    print(name)