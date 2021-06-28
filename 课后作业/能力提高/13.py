#【13】 (程序设计)编写程序，输入正整数a和b，产生a个范围在[100,999]的随机整数。输出这a个随机数(每行5个，数据之间用一个空格隔开)，找出能被b整除的数据个数。注意：不能使用列表、元组、集合、字典等组合数据类型。
import random
a=eval(input('请输入整数a：'))
b=eval(input('请输入整数b：'))
d=0
for i in range(1,a+1):
    c=random.randint(100,999)
    if i%5==0:
        print(c)
    else:
        print('{} '.format(c),end='')
    if c%b==0:
        d+=1
print('总共{}个数能被{}整除'.format(d,b))
