'''【1】 (程序设计)编写以下三个函数并依次调用，注意在每个函数内部打开文件并关闭。
(1)定义函数def f_write()：用随机函数生成10行数据，每行数据个数3到8个不等，每个数的范围为[-50,50]。把这些数据保存为data.txt
(2)定义函数def f_read()，用read函数求文件data.txt中全部数字的最大值(不能用max,sort函数)，并输出
(3)定义函数def r_readlines(),用readlines()函数读文件，计算文件data.txt每一行各个数的和，并输出和的最大值。'''
import random
random.seed(1000)
def f_write():#用随机函数生成10行数据，每行数据个数3到8个不等，每个数的范围为[-50,50]。把这些数据保存为data.txt
    fo=open('data.txt','w')
    for i in range(10):
        a=random.randint(3,8)
        for j in range(a):
            fo.writelines(str(random.randint(-50,50)))
            if j!=a-1:
                fo.writelines(',')
        if i!=9:
            fo.writelines('\n')
    fo.close()
def f_read():#求文件data.txt中全部数字的最大值(不能用max,sort函数)，并输出
    fo=open('data.txt','r')
    num=fo.read()
    num=num.replace('\n',',')#将字符串中的换行符换成逗号
    ls=num.split(',')#以逗号分割添加到列表中
    fomax=0
    for i in ls:#求最大值
        if int(i)>fomax:
            fomax=int(i)
    fo.close()
    print('用read求全部数字的最大值：{}'.format(fomax))
def r_readlines():#计算文件data.txt每一行各个数的和，并输出和的最大值
    fo=open('data.txt','r')
    summax=0
    for line in fo.readlines():
        ls=[]
        ls=line.split(',')#以逗号分割将每一个数添加到列表中
        linesum=0
        for i in ls:#计算每一行的和
            linesum += eval(i)
        if linesum>summax:#求最大值
            summax=linesum
    print('用readlines求每行和的最大值：{}'.format(summax))
f_write()
f_read()
r_readlines()
