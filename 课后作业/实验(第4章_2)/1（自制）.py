#输入一元二次方程的系数a,b,c，求解该方程。注意考虑各种可能情况（不是一元二次方程，相等实根，不等实根，共轭虚根），输出格式要与样例一致。共轭虚根要分别计算出实部和虚部，再用complex来构造复数根，不能设置显示的小数位数。
a=eval(input('请输入系数a:'))
b=eval(input('请输入系数b:'))
c=eval(input('请输入系数c:'))
d=b**2-4*a*c
if a==0:
    print('不是一元二次方程')
elif d>0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    print('方程有两个不等实根')
    print('x1=',x1,',x2=',x2)
elif d==0:
    x1=(-b+d**0.5)/(2*a)
    print('方程有两个相等的实根 x1=x2=',x1)
elif d<0:
    d=-d
    shi=-b/(2*a)
    xu=d**0.5/(2*a)
    x1=complex(shi,xu)
    x2=complex(shi,-xu)
    print('方程有两个共轭虚根')
    print('x1=',x1)
    print('x2=',x2)
    
