#编写程序，输入行数，输出由星号组成的平行四边形（四条边的星号个数都相同）。
n=eval(input('请输入行数：'))
for i in range(1,n+1):
    if i==1:
        print('{}{}'.format((n-i)*'  ',n*'* '))
    if i!=1 and i!=n:
        print('{}{}{}{}'.format((n-i)*'  ','* ',(n-2)*'  ','*'))
    if i==n:
        print('{}'.format(n*'* '))
