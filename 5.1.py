def func(a):
    total=0
    for i in a:
        total+=int(i)
    return total
a=input("请输入一个整数：")
s=func(a)
print("它的各位数字和为：{}".format(s))
    
