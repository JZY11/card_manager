def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a     # 如果一个函数中有 yield 语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1

    return "ok......."

obj2 = create_num(10)

while True:
    try:
        ret = next(obj2)    # 通过next 来启动生成器来生成下一个值
        print(ret)
    except Exception as ret:
        print(ret.value)    # ret.value 是生成器的模板 create_num 的返回值: "ok......."
        break