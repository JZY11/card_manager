import re


def main():
    ret1 = re.search(r"\d+", "阅读次数为：999，点赞次数为：6766")
    ret2 = re.findall(r"\d+", "阅读次数为：999，点赞次数为：6766")  # findall(): 可以返回所有匹配到的，返回的必然是一个列表
    ret3 = re.sub(r"\d+", "998", "python = 997")    # 先拿着正则表达式(即第一个参数)在第3个参数("python = 997")中进行匹配,匹配到之后再用第二个参数进行替换

    ret4 = re.sub(r"\d+", add, "python = 990")  # python正则中的sub()的第二个参数支持一个函数的引用，匹配到之后会相当于调用引用的函数(其中的参数就是匹配到的)，将函数的返回值替换给第3个参数

    print(ret1.group())
    print(ret2)
    print(ret3)
    print(ret4)

    splitregx()


def splitregx():
    ret5 = re.split(r":| ", "info:XiaoZhang 33 shandong")
    print(ret5)


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


if __name__ == "__main__":
    main()

"""
    match(): 是从头开始匹配的
    search(): 并不是从头开始匹配而且只要找到一个就立即返回，不会再继续往下匹配   但如果在正则规则中加上：^ 就可以达到match的功能
    sub():
    split(): 根据匹配进行切割字符串，并返回一个列表
"""