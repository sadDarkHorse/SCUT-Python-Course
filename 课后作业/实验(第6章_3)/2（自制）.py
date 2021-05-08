'''2、(程序设计)一般来说，一组数据中，出现次数最多的数就叫这组数据的众数。
例如：1，2，3，3，4的众数是3。
但是，如果有两个或两个以上个数出现次数都是最多的，那么这几个数都是这组数据的众数。
例如：1，2，2，3，3，4的众数是2和3。
还有，如果所有数据出现的次数都一样，那么这组数据没有众数。
例如：1，2，3，4，5没有众数。
编写程序，用随机函数产生1000个范围在[100,200]的随机整数，求出这1000个数的众数。如果有多个众数，都要输出。'''
import random
random.seed(10079)
numberlist=[]
for i in range(1000):#生成1000个整数
  numberlist.append(random.randint(100,200))
numberset=set(numberlist)
numberdic={}
for i in numberset:#统计整数的个数
    numberdic[i]=numberlist.count(i)
numberls=list(numberdic.items())
numberls.sort(key=lambda x:x[1],reverse=True)
max=numberls[0][1]
print('众数是',end=' ')
for i in numberdic.items():
    if i[1]==max:
        print(i[0],end=' ')




