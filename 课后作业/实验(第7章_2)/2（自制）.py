fo=open('2015年5月高三模拟考成绩.csv','r',encoding='UTF-8')
ls=[]
for line in fo:#将csv文件读取到列表中
    if line[0].isnumeric():
        line = line.replace("\n","")
        ls.append(line.split(","))
fo.close()
for j in range(len(ls)):#对每个人的成绩求和，添加到末尾
    sum=0
    for i in range(3,9):
        sum+=eval(ls[j][i])
    ls[j].append(sum)
ls=sorted(ls,key=lambda x:-x[9])#按照总分进行排序
print('总分前5名的学生情况')
print('{:<4}{:<4}{:<5}{:<4}'.format('名次','班别','姓名','总分'))
print('-'*22)
for i in range(5):
    print('{:<6}{:<5}{:　<4}{:<4}'.format(i+1,ls[i][1],ls[i][2],ls[i][9]))#中间加入中文全角空格填充来对齐
