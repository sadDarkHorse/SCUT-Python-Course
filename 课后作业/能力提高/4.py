#【4】 (程序设计)输入一个正整数，输出这个整数的二进制表示中1的个数。比如输入整数13，其二进制表示为1101，有3个1，因此输出结果为3,输出格式请参考样例。
n=int(input('请输入一个正整数:'))
a=str(bin(n))
sum=0
for i in a:
    if i=='1':
        sum+=1
print('{}的二进制表示中有{}个1'.format(n,sum))
'''第二种

n=int(input('请输入一个正整数:'))
def zhuanhuan(z):
    s=''
    while z>0:
        s=str(z%2)+s
        z//=2
    return s
a=zhuanhuan(n)
sum=0
for i in a:
    if i=='1':
        sum+=1
print('{}的二进制表示中有{}个1'.format(n,sum))
'''
