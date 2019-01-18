import gevent
import time


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)  虽然gevent遇到延时就会切换任务  但是time.sleep(0.5)不行
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


g1 = gevent.spawn(f1, 5) # 创建gevent对象 g1     第一个参数指定将来的协程具体去哪执行
g2 = gevent.spawn(f2, 5)
g3 = gevent.spawn(f3, 5)

g1.join()   # 等待 g1 执行完   gevent遇到延时操作就切换
g2.join()
g3.join()