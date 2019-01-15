import multiprocessing
import time, os, random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getPid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%s" % (t_stop - t_start))

def main():
    po = multiprocessing.Pool(3)
    for i in range(0,10):
        po.apply_async(worker, (i, ))

    print("---- start ----")
    po.close()
    po.join()
    print("--- end ---")

if __name__ == "__main__":
    main()