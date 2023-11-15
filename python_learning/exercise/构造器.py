
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