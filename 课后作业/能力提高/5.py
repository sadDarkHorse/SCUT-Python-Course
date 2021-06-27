#【5】 (程序设计)输入用“；“间隔的数字串，计算输入数字的和并输出结果。如输入的数字串为：12；23；34；45
a=input('请输入：')
ls=a.split('；')
sum=0
for i in ls:
    sum+=eval(i)
print('结果为{}'.format(sum))
