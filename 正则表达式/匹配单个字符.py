import re


receive = re.match(r"速度与激情\d{1,5}", "速度与激情2234")   # {1,2}表示前面紧挨着的 \d(即数字) 有一位或者两位
print(receive.group())

