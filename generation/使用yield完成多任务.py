import time


def task1():
    while True:
        print("--- 1 ---")
        time.sleep(0.1)
        yield 10

def task2():
    while True:
        print("--- 2 ---")
        time.sleep(0.1)
        yield 100


def main():
    t1 = task1()     # 因为task1()  task2() 中有 yield 所以 t1 、 t2 就成了生成器对象
    t2 = task2()
    # 先让t1运行一会，当t1中遇到 yield 的时候，在返回到22行，然后
    # 运行t2，当它要yield的时候，再次切换到t1中
    # 这样 t1/t2/t1/t2的交替运行，最终实现了多任务 ... 协程

    while True:
        next(t1)
        next(t2)



if __name__ == "__main__":
    main()