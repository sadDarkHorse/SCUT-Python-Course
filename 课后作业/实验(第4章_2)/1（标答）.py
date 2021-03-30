#评分标准：4种情况：不是一元二次方程（10分），另三种情况每种30分。
#输出格式要与样例一致，不一致视情况扣10-20分。
import math
a=eval(input("请输入系数a:"))
b=eval(input("请输入系数b:"))
c=eval(input("请输入系数c:"))
if a==0:
    print("不是一元二次方程")
else:
    d=b*b-4*a*c
    if d==0:
        print("方程有两个相等的实根 x1=x2=",-b/2/a)
    elif d>0:
        x1=(-b+math.sqrt(d))/2/a
        x2=(-b-math.sqrt(d))/2/a
        print("方程有两个不等实根")
        print("x1=",x1,",x2=",x2)
    else:
        x1=complex(-b/2/a,math.sqrt(-d)/2/a)
        x2=complex(-b/2/a,-math.sqrt(-d)/2/a)
        print("方程有两个共轭虚根")
        print("x1=",x1)
        print("x2=",x2)
