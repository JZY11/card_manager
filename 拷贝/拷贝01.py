import copy


# 当一个变量=XXX的时候，约定为这个变量指向了这个XXX
a = [11, 22]

# copy.copy() 能够完成浅拷贝的功能
a = [11, 22]    # a 指向列表
b = [33, 44]    # b 指向另外一个列表
c = [a, b]      # c 指向一个列表，而a，b分别指向上边的列表(对象的引用)
d = c
e = copy.copy(c)    # e 指向了一个新的列表  实际上只拷贝最上面一层即：你让我拷c 那我就只拷贝c 里的东西，而c 里面指向的东西不拷  让e指向一个新的

# copy.deepcopy() 能够完成深拷贝的功能
f = copy.deepcopy(c)    # f 指向了一个c 的列表 完全拷贝了  再改变c 对f 没有影响了