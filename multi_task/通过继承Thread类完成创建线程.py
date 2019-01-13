import threading
import time


class MyThread(threading.Thread): # 类MyThread继承Thread类
    # 两种方法：1: 定义t1 = threading.Thread(target=sing) t1.start()
    # 2: 定义一个类继承Thread类，然后定义run()方法，run方法中写什么将来这个线程就执行什么
    # 如果我要做的一件事情是在一个线程里做而且要分成多个函数，我就可以把多个函数封装成一个方法放在一个类中，该类要继承Thread类

    def run(self):  # 必须定义run方法
        for i in range(3):
            time.sleep(1)
            msg = "I`m" + self.name + '@' + str(i) # name属性中保存的是当前线程的名字


if __name__ == '__main':
    t = MyThread() # 创建一个对象就意味着以后只能创建一个线程，一个线程同一时刻只能执行一个函数
    t.start()   # 此种情况在调用start(),只会执行run()方法