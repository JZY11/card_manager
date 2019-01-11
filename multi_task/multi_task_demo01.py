import time
import threading


def sing():
    """唱歌"""
    for i in range(5):
        print("--- 正在唱两只老虎 --")
        time.sleep(1)


def dance():
    """跳舞"""
    for i in range(5):
        print("--- 正在跳舞 --")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

# 所谓多任务就是当一个程序运行起来后，还可以既做这个又做那个
# 单核CPU在同一时刻只做一件事情    双核CPU意味着在同一时刻有两个核在做各自的事情    注意：单核CPU是不可能完成多任务的  之所以我们感觉像是同时执行
# 原因就是操作系统轮询着给不同的程序分配了足够小的时间片的原因

# 并行：就是多个任务同时执行
# 并发：假的多任务

if __name__ == "__main__":
    main()