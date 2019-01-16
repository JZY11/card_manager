class Classmates(object):
    def __init__(self):
        self.names = list() # names 属性指向了 list() 列表


    def add(self, name):
        self.names.append()


classmate = Classmates() # 定义一个实例对象

classmate.add("老二")
classmate.add("老三")
classmate.add("老四")

for name in classmate:
    print(name)