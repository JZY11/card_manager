import threading
import time


def test1():
    for i in range(5):
        print("-------test1------%d" % i)
        time.sleep(1)

    # 如果创建Thread时执行的函数运行结束，那么就意味着这个子线程就结束了

def test2():
    for i in range(10):
        print("-------test2------%d" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1: # 判断条件是线程数小于等于1(即只有一个主线程时循环结束)
            break
        time.sleep(1)


if __name__ == "__main__":
    main()