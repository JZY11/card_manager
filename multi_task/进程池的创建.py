import multiprocessing
import time, os, random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getPid()))

    # random.random() 随机生成 0 - 1 之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%s" % (t_stop - t_start))

def main():
    po = multiprocessing.Pool(3)    # 定义一个进程池，最大进程数为3

    for i in range(0, 10):
        # po.apply_async(要调用的目标, (传递给目标的参数元组, ))
        # 每次循环都会用空闲出来的子进程来调用目标
        po.apply_async(worker, (i, ))

    print("---- start ----")
    po.close()      # 关闭进程池，关闭后po不再接受新的请求
    po.join()       # 等待po中所有的子进程执行完毕，必须要放在close语句之后
    print("--- end ---")

if __name__ == "__main__":
    main()