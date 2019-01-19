import re


receive = re.match(r"速度与激情\d{1,5}", "速度与激情2234")   # {1,2}表示前面紧挨着的 \d(即数字) 有一位或者两位
print(receive.group())

receive = re.match(r"021-?\d{8}", "021-121345678")   # ?: 它前面紧挨着它的字符可有可无，若有也只能有一个
print(receive.group())

receive = re.match(r"\d{3,4}-?\d{7,8}", "0531-121345678")   # ?: 它前面紧挨着它的字符可有可无，若有也只能有一个
print(receive.group())


html_content = """fasfdgg
gagagag
agagaga
grhry
htrhjtffhhyrr"""  # '''xxx''' 和 """xxx"""  表示可以换行
# print(html_content)

receive = re.match(r".*", html_content, re.S).group()  # .*：可以匹配到除了 \n 以外的所有    re.S添加了这个参数后就可以匹配到 \n 了
print(receive)


rec = re.match(r".+", "a34")
print(rec.group())

"""
匹配多个字符：
    {m}：   必须指定前面的一个字符必须要有m个
    {m,n}:  必须指定前面的一个字符必须要有m - n个
      ?  :  表示匹配前面一个字符出现1次或者0次，即要么1次，要么0次
      +  ： 匹配前一个字符出现1次或者无限次，即至少1次
      *  ： 匹配前一个字符出现0次或者无限次，即可有可无
"""