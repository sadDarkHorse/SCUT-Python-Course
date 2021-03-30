#评分标准：多运行几次，输出剩余的钱在1900-3000之间为正确，平均在2100左右。模拟次数由程序输入，不扣分
#每次模拟选定固定的一个数，不扣分
import random

money = 10000
for i in range(100000):
    a = int(6*random.random())+1  #自选一个数
    b,c,d = int(6*random.random())+1,int(6*random.random())+1,int(6*random.random())+1
    if b==a or c==a or d==a:
        if b==a:
            money = money+1
        if c==a:
            money = money+1
        if d==a:
            money = money+1
    else:
        money = money -1
print(money)
