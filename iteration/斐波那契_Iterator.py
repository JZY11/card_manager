from collections import Iterable
from collections import Iterator
import time

class Fibonacci(object):
    """要想让一个对象具有可迭代性，第一：该类必须要实现 __iter__ 方法。 第二：__iter__ 方法的返回得要return一个对象的引用，该对象里必须要有 __iter__ 方法 和 __next__ 方法"""
    def __init__(self, all_num):
        self.current_num = 0 # 实例属性
        self.all_num = all_num
        self.a = 0
        self.b = 1

    def __iter__(self):
        """如果让一个对象成为一个可以迭代的对象即可以使用for  则必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a

            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1

            return ret
        else:
            raise StopIteration          # 如何告诉迭代器已经将数据取完了呢/


fibo = Fibonacci(10)

for num in fibo:
    print(num)
    time.sleep(1)