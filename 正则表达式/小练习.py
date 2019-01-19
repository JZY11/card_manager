import re

names = ["name1", "_name", "2_name", "_name_"]

for name in names:
    ret = re.match("[a-zA-Z]+[\w]]*", name)
    if ret:
        print("变量名 %s 符合要求" % ret.group())
    else:
        print("变量名 %s 非法" % ret.group())