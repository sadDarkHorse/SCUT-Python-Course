fo=open('2015年5月高三模拟考成绩.csv','r',encoding='UTF-8')
ls=[]
for line in fo:
    if line[0].isnumeric():
        line = line.replace("\n","")
        ls.append(line.split(","))
for j in range(len(ls)):
    sum=0
    for i in range(3,9):
        sum+=eval(ls[j][i])
    ls[j].append(sum)
ls=sorted(ls,key=lambda x:-x[9])
print('总分前5名的学生情况')
print('{:<4}{:<4}{:<5}{:<4}'.format('名次','班别','姓名','总分'))
print('-'*22)
for i in range(5):
    print('{:<6}{:<5}{:　<4}{:<4}'.format(i+1,ls[i][1],ls[i][2],ls[i][9]))
