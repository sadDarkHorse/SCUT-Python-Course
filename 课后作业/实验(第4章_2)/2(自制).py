#输入一元二次方程的系数a,b,c，求解该方程。注意考虑各种可能情况（不是一元二次方程，相等实根，不等实根，共轭虚根），输出格式要与样例一致。共轭虚根要分别计算出实部和虚部，再用complex来构造复数根，不能设置显示的小数位数。
a=ord(input('请输入开始字母:'))
b=ord(input('请输入结束字母:'))
if a>b:
    t=a
    a=b
    b=t
for i in range(a,b+1):
    for j in range(i,b+1):
        print(chr(j),end='')
    for k in range(a,i):
        print(chr(k),end='')
    print()
