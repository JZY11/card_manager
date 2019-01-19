import re


receive = re.match(r"速度与激情\d{1,5}", "速度与激情2234")   # {1,2}表示前面紧挨着的 \d(即数字) 有一位或者两位
print(receive.group())

receive = re.match(r"021-?\d{8}", "021-121345678")   # ?: 它前面紧挨着它的字符可有可无，若有也只能有一个
print(receive.group())

