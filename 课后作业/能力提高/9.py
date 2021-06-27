#【9】 (程序设计)从1，2，3，4，5随机抽取3个数字组成一个三位数。用随机函数编写程序，模拟产生100000次三位数，输出此100000个三位数中能被9整除的概率（同时输出允许相同数字如112、233等和不允许有相同数字的结果）。（结果约为0.152,0.096）
import random
n=0
m=0
for i in range(100000):
    a=str(random.randint(1,5))+str(random.randint(1,5))+str(random.randint(1,5))
    if eval(a)%9==0:
        n+=1
for i in range(100000):
    b=random.sample(['1','2','3','4','5'],3)
    c=b[0]+b[1]+b[2]
    if eval(c)%9==0:
        m+=1
print(n/100000,m/100000)
