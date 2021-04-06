'''
评分标准：
1. 计算数字和，如果不用函数，至多给60分
2. 函数内用了print，input扣10分,用了全局变量扣10分
'''
def func(a):
    sum = 0
    while a:  #while a 相当于 while a!=0
        sum += (a%10)
        a = a//10
    return sum
a = int(input('请输入一个整数:'))
print('它的各位数字和为{}'.format(func(a)))
