import multiprocessing

def  download_from_web():
    """下载数据"""
    # 模拟从网上下载的数据
    data = [11, 22, 33, 44]


def analysis_data():
    """数据处理"""


def  main():
    p1 = multiprocessing.Process(target=download_from_web)
    p2 = multiprocessing.Process(target=analysis_data)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()