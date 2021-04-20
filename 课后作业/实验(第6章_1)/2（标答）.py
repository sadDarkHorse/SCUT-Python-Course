'''评分标准
1.格式与样例不一致，扣10分。如果不用循环输出坐标点，扣20分
2.评分时注意看程序是否有seed(1000)，如果没有请加上，然后和上图比较，看结果是否一致。
  结果错误最多给50分
3.用10个变量来保存10个点坐标，最多给50分
'''
import random

point=[]
for i in range(10):
    point.append((int(random.random()*10),int(random.random()*10)))
m=0
print("10个点的坐标是:")
for p in point:
    print(p,end=' ')
    m=m+1
    if m==5:
        print()
        m=0
distance=0
for p1 in range(len(point)-1):
    for p2 in range(p1+1,len(point)):
            #计算距离，不开方也是可以的
            d=(point[p1][0]-point[p2][0])**2+(point[p1][1]-point[p2][1])**2
            if d>distance:
                distance=d
                result=(p1,p2)
print("距离最大的两个点是{}{}".format(point[result[0]],point[result[1]]))
