#【2】 (程序设计)输入一个正整数，输出它的因子分解式。如输入132，则输出132=1*2*2*3*11.
n=eval(input('输入正整数：'))
s=str(n)+'=1*'
a=2
while n>=a:
    if n%a==0:
        s+='*'+str(a)
        n/=a
    else:
        a+=1
print(s)
