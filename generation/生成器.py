def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a     # 如果一个函数中有 yield 语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1


obj2 = create_num(20)

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        break