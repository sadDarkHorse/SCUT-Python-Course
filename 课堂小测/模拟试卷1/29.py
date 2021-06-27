#(程序设计)附件“成绩.csv”包含若干个学生的学号，语文成绩，数学成绩，英语成绩。编写程序，按语数英三科总分从高到低的顺序输出，参考样例。
fo=open('成绩.csv','r')
ls=[]
for line in fo:
    line=line.replace('\n','')
    a=line.split(',')
    ls.append((a[0],eval(a[1])+eval(a[2])+eval(a[3])))
ls=sorted(ls,key=lambda x:x[1],reverse=True)
print('学号     总分')
for i in ls:
    print('{}   {}'.format(i[0],i[1]))
