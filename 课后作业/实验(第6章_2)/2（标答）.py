#评分标准:结果正确，不是按题目的方法，给80分。格式不对齐，再扣10分
#要有一个变量记录最小值的位置，如果没有就是方法不对
#可以假设前面两个是最大值，看程序交换次数是否超过49次
import random

a=[]
n=50

for i in range(n):
    a.append(random.randint(1,999))

for i in range(n):
    k=i                      #k用于记录最小值所在的位置
    for j in range(i+1,n):   #找出最小值
       if a[j] < a[k]:
           k=j
    a[i],a[k]=a[k],a[i]      #交换到合适的位置

for i in range(n):
    print('{0:>5}'.format(a[i]),end='')
    if (i+1)%10==0:
        print()
