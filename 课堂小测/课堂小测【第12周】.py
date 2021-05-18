'''1、(程序设计)附件是某校今年四级英语考试的成绩。先下载附件，解压到C盘根目录。编写程序，用read函数读取该文件，统计本次考试的总人数，最高分和平均分（保留2位小数）。注意:分数之间用逗号隔开，由于录入人员工作不仔细，两个逗号之间可能只有空格没有分数，需要用程序判断。'''
#评分标准：不是用read函数来读文件，扣30分
f=open('c:/四级成绩.txt','r')
score=f.read()
f.close()
score=score.replace('\n',',')
score=score.replace(' ','')  #数据文件有多余的空格
a=score.split(',')
max=0
s=0
b=0
for i in a:
    if i!='':
        if eval(i)>max:
            max=eval(i)
        s=s+eval(i)
        b=b+1
print('共有{}人，最高分为{},平均分为{:.2f}'.format(b,max,s/b))
