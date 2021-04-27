string=input('请输入一个字符串:')
stringlist=list(string)#将字符串转化为列表
stringset=set(stringlist)#将字符串转化为集合
stringtimesdic={}
for i in stringset:#用字典列表储存字符出现次数
    stringtimesdic[i]=stringlist.count(i)
stringtimeslist=list(stringtimesdic.items())#将出现次数的字典转化为列表
stringtimeslist.sort(key=lambda x:x[1],reverse=True)#将出现次数的列表按次数排序
strappeardic={}
for i in stringset:#用字典储存字符第一次出现的位置
    strappeardic[i]=string.index(i)
for i in range(len(stringtimeslist)-1):#按照出现次数和第一次出现的位置交换列表中的位置
    for j in range(i+1,len(stringtimeslist)):
        if stringtimeslist[i][1]==stringtimeslist[j][1] and strappeardic.get(stringtimeslist[i][0])<strappeardic.get(stringtimeslist[j][0]):
            stringtimeslist[i],stringtimeslist[j]=stringtimeslist[j],stringtimeslist[i]
print('不重复的字符是:',end='')
for i in stringtimeslist:
    print(i[0],end='')
