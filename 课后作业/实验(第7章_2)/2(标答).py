#评分标准：结果正确，只是第5名的总分不对齐，不扣分
#班别，姓名不对齐，扣10分.总分相同，顺序可以和图片不一致。
#结果不一致，最多给60分
f=open("2015年5月高三模拟考成绩.csv","r",encoding='utf8')
score={}
for line in f:
    if line[0]=='3':
        a=line.split(",")
        b=[a[1],a[2]]  #把班别，姓名，成绩 合并为一个列表
        for i in range(3,9):
            b.append(eval(a[i]))  #成绩要转换为整数，后面要计算总分
        score[a[0]]=b
f.close()

#输出总分前5的学生姓名，班别，总分
print('总分前5名的学生情况')
print('{:4}{:5}{:<6}{:>3}'.format("名次", "班别", "姓名", "总分"))
print("--------------------------")
ls=sorted(score.items(),key=lambda x:-sum(x[1][2:]))
for i in range(5):
    print('{0:^4}{1:^8}{2:{4}<5}{3:<4}'.format(i + 1, ls[i][1][0], ls[i][1][1], sum(ls[i][1][2:]),chr(12288)))
