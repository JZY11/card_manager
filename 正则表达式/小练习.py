import re


def main():
    """正则的match(): 只判断开头不判断结尾"""
    names = ["age", "_age", "2age", "age1", "a_age", "age_2_", "age!", "____", "a#123"]

    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print("变量名:%s 符合要求...通过正则匹配出来的数据是：%s" % (name, ret.group()))
        else:
            print("变量名:%s 非法" % name)


if __name__ == "__main__":
    main()