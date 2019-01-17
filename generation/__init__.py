# 生成器是一类特殊的迭代器

# 列表推导式
nums = [x*2 for x in range(10)]
print(str(nums))

# 生成器方式1. 将列表推导式的中括号换成小括号
nums = (x*2 for x in range(10)) # 这就是一个生成器(返回的只是生成数据的方式，节省空间)
print(nums)

for num in nums:
    print(num)


# 生成器方式2.
def creat_num(all_num):
    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        yield a         # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1

# 如果在调用creat_num的时候，发现这个函数有 yield ，那么此时这个就不再是函数，而是创建一个生成器的对象
obj = creat_num(10) # 只要函数creat_num 中含有 yield 那么 obj就是一个生成器对象
ret = next(obj)     # next函数返回的就是 yield 后的值
print(ret)

for num in obj:
    print(num)


