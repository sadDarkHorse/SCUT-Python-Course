# (程序设计)用随机函数生成10个平面坐标上的点，每个点的坐标都是0-9的整数。输出这10个点的坐标（每行5个），找出距离最远的两个点的坐标。图片是加上seed(1000)得到的结果,可验证程序是否正确。提示：用元组来保存一个坐标点，用列表来保存全部坐标点。计算任意两点的距离，然后找出最大的距离。如果有距离相同的多组坐标，输出其中一组即可。
import random
ls=[]#生成空的列表
random.seed(1000)
for i in range(10):#生成十个坐标，添加到ls中
 b=random.randint(0,9),random.randint(0,9)
 ls.append(b)
c=0
for i in range(10):#计算两两之间的距离
 for j in range(i,10):
  d=(ls[i][0]-ls[j][0])**2+(ls[i][1]-ls[j][1])**2
  if d>=c:#如果两点之间的距离大于已有的距离
   c=d#令c等于该距离
   e=ls[i],ls[j]#e等于这两个点
print('10个点的坐标是:')#输出
for i in range(10):
 print(ls[i],end='')
 if i==4 or i==9:
  print()
print('{}{}{}'.format('距离最大的两个点是',e[0],e[1]))
