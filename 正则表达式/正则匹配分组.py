import re


def main():
    email = input("请输入邮箱地址：")
    ret = re.match(r"([a-zA-Z_0-9]{4,20})@(163|126)\.com$", email)
    if ret:
        print("%s符合要求..." % email)
        print(ret.group())
        print(ret.group(1))
        print(ret.group(2))
    else:
        print("%s不符合要求..." % email)

    regx()


def regx():
    html_str = "<body><h1>haohhfjjs</h1></body>"
    # ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html_str).group()
    ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", html_str).group()
    print(ret)


if __name__ == "__main__":
    main()

"""
    | : 匹配左右任意一个表达式
  (ab): 将括号中的字符作为一个分组
  \num: 引用分组num匹配到的字符串： 如 \1  \2
(?P<name>): 分组起别名
(?P=name): 引用别名为name分组匹配到的字符串
"""
