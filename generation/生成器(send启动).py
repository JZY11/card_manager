def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a     # 如果一个函数中有 yield 语句，那么这个就不再是函数，而是一个生成器的模板
        print(">>>>>>>>>>", ret)
        a, b = b, a + b
        current_num += 1


obj2 = create_num(10) # 生成器对象

ret = next(obj2)
# 程序执行 next() ,然后从create_num() 方法开始执行，当执行到 ret = yield a 语句时  暂停不在往下执行  而是执行 print(ret)
print(ret)

ret = obj2.send("hahah")
# 程序执行到  生成器对象调用 send() 方法时 又重新回到上次暂停处， 把 send(XX) 中的参数XX 赋值给 yield a  即：ret 然后接着往下执行print(">>>>>>>>>>", ret) 。。。
print(ret)