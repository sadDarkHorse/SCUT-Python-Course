import random
random.seed(1000)
def f_write():
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
def f_read():
    fo=open('data.txt','r')
    num=fo.read()
    num=num.replace('\n',',')
    ls=num.split(',')
    fomax=0
    for i in ls:
        if int(i)>fomax:
            fomax=int(i)
    fo.close()
    print('用read求全部数字的最大值：{}'.format(fomax))
def r_readlines():
    fo=open('data.txt','r')
    summax=0
    for line in fo.readlines():
        ls=[]
        ls=line.split(',')
        linesum=0
        for i in ls:
            linesum += eval(i)
        if linesum>summax:
            summax=linesum
    print('用readlines求每行和的最大值：{}'.format(summax))
f_write()
f_read()
r_readlines()
