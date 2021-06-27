#【12】 (程序设计)（根据2019高考数学I卷试题改编）甲、乙两队进行篮球决赛，采取七场四胜制（当一队赢得四场胜利时，该队获胜，决赛结束）．根据前期比赛成绩，甲队的主客场安排依次为“主主客客主客主”．设甲队主场取胜的概率为0.7，客场取胜的概率为0.5，且各场比赛结果相互独立。什么样的比分（甲:乙）出现概率最大？
import random
def gameOver(a,b):
    return a==4 or b==4

def awin(a,b):
    c=a+b
    result=random.random()
    if c in [0,1,4,6]:
        if result<=0.7:
            return True
        else:
            return False
    else:
        if result<=0.5:
            return True
        else:
            return False

def simoneGames():
    proba,probb=0,0
    while not gameOver(proba,probb):
        if awin(proba,probb):
            proba+=1
        else:
            probb+=1
    return proba,probb

def simNGames():
    sumgames={}
    for i in range(10000):
        game=simoneGames()
        sumgames[game]=sumgames.get(game,0)+1
    ls=sorted(sumgames.items(),key=lambda x:x[1],reverse=True)
    return ls[0][0]

print(simNGames())
