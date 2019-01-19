import re


def main():
    email = input("请输入163邮箱地址：")
    # 如果正则表达式中需要用到了某些普通的字符，比如：. ? 等 需要在他们前面添加 \ 进行转义
    ret = re.match(r"[a-zA-Z_0-9]{4,20}@163.com$", email)
    if ret:
        print("%s符合要求..." % email)
    else:
        print("%s不符合要求..." % email)

if __name__ == "__main__":
    main()


