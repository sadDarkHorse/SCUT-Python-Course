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




