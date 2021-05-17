import random

random.seed(1000)  #这句不是必需的，没有也不扣分
filename="d:/data.txt"
def f_write():
    f=open(filename,"w")
    for i in range(10):
        c=int(6*random.random()+3)   #随机数3-8
        for j in range(c):
            x=int(101*random.random()-50)  #产生-50,50之间的随机整数
            if j==c-1:
                f.write(str(x)+'\n')       #这里不需要生成列表，直接写到文件就可以了
            else:
                f.write(str(x)+',')
    f.close()

#用read函数求所有数的最大值
def f_read():
    f=open(filename,"r")
    s=f.read()  #读入全部内容
    a=s.split("\n")
    max=''    #表示还没有最大值
    for i in a:
        b=i.split(",")
        for j in b:
            if max=='':
                max = eval(j)
            elif j != '':
                if eval(j)>max:
                    max=eval(j)
    f.close()
    print("用read求全部数字的最大值:{}".format(max))

#方法二   用read函数求所有数的最大值
def f_read2():
    f=open(filename,"r")
    s=f.read()  #读入全部内容
    a=s.split("\n")
    a.remove('')         #把空字符串都删除
    max=eval(a[0][0])    #表示还没有最大值
    for i in a:
        b=i.split(",")
        for j in b:
            if eval(j)>max:
                max=eval(j)
    f.close()
    print("用read求全部数字的最大值:{}".format(max))

#用readlines求每行数字和的最大值
def f_readlines():
    f=open(filename,"r")
    max=''
    for line in f.readlines():  #这句也可以改成 for line in f:
        b=line.split(",")
        sum=0
        for j in b:
            sum = sum + eval(j)
        if max=='':
            max = sum
        elif sum>max:
            max = sum
    f.close()
    print("用readlines求每行和的最大值:{}".format(max))

f_write()
f_read()
f_readlines()
