"""  构造器 """
def add_methond(func):
    def inner(n):
        a = 1
        b = 2
        print("""ssssssssss"""+str(a+b))
        #如果n的值发生了变化的话，后面主题函数的打印结果也会发生变化
        func(n)
    return inner

@add_methond
def zz(num):
    print("""打印结果"""+str(num))


zz(66)

""" 带参数的构造器 """

def dfes(flag):
    def prints(flg):
        def inner():
            print(flag+"----")
        return inner
    return prints

@dfes("uuu")
def ff():
    print("""dddddddd""")

ff()

# 生成器
abc = (i for i in range(5,200))
zzz=next(abc)
print("""2222sxd""",zzz)