#【10】 (程序设计)（2019高考数学I卷）甲、乙两队进行篮球决赛，采取七场四胜制（当一队赢得四场胜利时，该队获胜，决赛结束）．根据前期比赛成绩，甲队的主客场安排依次为“主主客客主客主”．设甲队主场取胜的概率为0.6，客场取胜的概率为0.5，且各场比赛结果相互独立。用随机函数模拟100000次，求甲队以4∶1获胜的概率。
import random
win41=0
for i in range(100000):
    awin,bwin=0,0
    for j in range(7):
        if awin==4 or bwin==4:
            break
        if j in (0,1,4,6):
            a=random.randint(1,10)
            if a<=6:
                awin+=1
            else:
                bwin+=1
        else:
            a=random.randint(1,10)
            if a<=5:
                awin+=1
            else:
                bwin+=1
    if awin==4 and bwin==1:
        win41+=1
print(win41/100000)
