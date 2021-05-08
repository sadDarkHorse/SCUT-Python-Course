import random
a={}  #用字典来计数'
random.seed(10027)
for i in range(1000):
    x=int(random.random()*101+100)
    a[x]=a.get(x,0)+1
b=sorted(a.items(),key=lambda x:-x[1])

#众数可能有多个,b是列表，有顺序
print(b)  #先观察数据


print('众数是 ',end='')
for i in b:
    if i[1]==b[0][1]:
        print(i[0],end='  ')
    else:   #出现次数和第一个不相等，肯定不是众数了
        break
