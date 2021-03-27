#输入两个整数，输出它们的最小公倍数（注意输出结果是不含有小数点的）。提示：可以用math库的函数。运行结果如下图所示。
import math
a=int(input('请输入第一个整数：'))
b=int(input('请输入第二个整数：'))
c=math.gcd(a,b)
d=int(a*b/c)
print('{0}、{1}的最小公倍数是{2}'.format(a,b,d))
