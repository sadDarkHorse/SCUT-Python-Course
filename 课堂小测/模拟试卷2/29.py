#29、(程序设计)下载附件，该附件包含若干个学生的考号，班别，语数英等各科成绩。编写程序，统计各班数学的平均分并按从高到低的顺序输出（平均分保留2位小数），输出结果参考下图。附件是utf8格式。
fo=open('2015年5月高三模拟考成绩.csv','r',encoding='utf8')
score={}
for line in fo:
    if line[0]=='3':
        a=line.split(',')
        score[a[1]]=(score.get(a[1],(0,0))[0]+eval(a[4]),score.get(a[1],(0,0))[1]+1)
fo.close()
ls=sorted(score.items(),key=lambda x:x[1][0]/x[1][1],reverse=True)
print('名次\t班别\t数学平均分')
for i in range(len(ls)):
    print('{}\t\t{}\t\t{:.2f}'.format(i+1,ls[i][0],ls[i][1][0]/ls[i][1][1]))
#之前写的
'''
fo=open('2015年5月高三模拟考成绩.csv','r',encoding='utf-8')
chengji={}
for line in fo:
    if line[0]=='3':
        a=line.split(',')
        b=chengji.get(a[1],[0,0])
        b[0]=b[0]+eval(a[4])
        b[1]=b[1]+1
        chengji[a[1]]=b
fo.close(),
ls=sorted(chengji.items(),key=lambda x:-x[1][0]/x[1][1])
print('名次\t班别\t数学平均分')
for i in range(len(ls)):
    print('{:3}\t{}\t{:.2f}'.format(i+1,ls[i][0],ls[i][1][0]/ls[i][1][1]))
'''
