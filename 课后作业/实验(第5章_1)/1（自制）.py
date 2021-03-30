#设计一个函数 func(a)，它接受一个正整数a，函数返回这个数字每个位上数字的和（函数内不能有input,print语句，不能使用global语句），例如，func(123)，返回6，因为1+2+3=6。
a=input('请输入一个整数:')
def func(c):
    b=0
    c=a
    for i in c:
        b+=int(i)
    return b
print('{}{}'.format('它的各位数字和为',func(a)))
