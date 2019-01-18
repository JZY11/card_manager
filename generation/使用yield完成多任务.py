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

    while True:
        next(t1)



if __name__ == "__main__":
    main()