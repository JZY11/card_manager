import gevent
import time
from gevent import monkey


# 有耗时操作时需要
monkey.patch_all()  # 这样就可以将程序中用到的耗时操作的代码，换为gevent中自己实现的代码  即：第12行就可以正常延时了


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)   # 虽然gevent遇到延时就会切换任务  但是time.sleep(0.5)不行
        # gevent.sleep(0.5)   # 耗时   再切换


gevent.joinall([       # 等待这个列表中的所有的协程都做完之后程序才结束
    gevent.spawn(f, 5),  # 创建gevent对象 g1     第一个参数指定将来的协程具体去哪执行
    gevent.spawn(f, 5),
    gevent.spawn(f, 5)
])

# 进程是资源分配的单位，线程执行代码  一个线程只能做一件事情   想要多任务只需要多线程就可以了
# 但是现在的情况是：仍然是单线程但是利用的是：当一个任务在浪费时间的时候我利用起来去做其他的事情  这就是所谓的协程
# 协程依赖于线程   线程依赖于进程