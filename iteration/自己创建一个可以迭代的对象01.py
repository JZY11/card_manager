from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    """要想让一个对象具有可迭代性，第一：该类必须要实现 __iter__ 方法。 第二：__iter__ 方法的返回得要return一个对象的引用，该对象里必须要有 __iter__ 方法 和 __next__ 方法"""
    def __init__(self):
        self.names = list() # names 属性指向了 list() 列表

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果让一个对象成为一个可以迭代的对象即可以使用for  则必须实现__iter__方法"""
        return ClassIterator(self)  # 返回的是一个迭代器的对象(该对象中必须有 __iter__ 方法 和 __next__ 方法， 特点就是可以循环取值)

class ClassIterator(object):
    """通过这个类创建出来的对象就可以当做上面方法__iter__ 的返回"""
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0 # 实例属性

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration          # 如何告诉迭代器已经将数据取完了呢?  - 让其抛出一个异常后程序就停止了


classmate = Classmate() # 定义一个实例对象

classmate.add("老二")
classmate.add("老三")
classmate.add("老四")

print("判断classmate是否是可迭代对象：", isinstance(classmate, Iterable)) # 判断对象是否具有可迭代性

classmate_iterator = iter(classmate) # 这个函数的返回值就是 __iter__ 方法的返回值(一个迭代器)
print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))

# print(next(classmate_iterator))

for name in classmate:    # classmate是一个可迭代的对象因为有 __iter__ 方法，然后for循环就调用这个方法的返回对象的 __next__ 方法 ，这个方法返回什么就给name变量什么
    print(name)
    time.sleep(1)