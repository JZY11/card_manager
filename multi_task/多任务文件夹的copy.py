import os
import multiprocessing

def copy_file(file_name):
    """完成文件的复制"""
    print("--- 模拟copy文件 ---")


def main():
    # 1. 获取要copy的文件夹的名字
    old_folder = input("请输入要copy的文件夹的名字:")

    # 2. 创建一个新的文件夹
    try:
        os.mkdir(old_folder + "[复件]")
    except:
        pass

    # 3. 获取文件夹的所有带copy的文件名字 listdir()
    file_names = os.listdir(old_folder)
    print(file_names)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(file_name, ))

    # 复制原文件夹下的所有文件到新的文件夹中


if __name__ == "__main__":
    main()

