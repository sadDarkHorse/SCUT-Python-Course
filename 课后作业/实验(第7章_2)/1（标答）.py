#评分标准：评卷时要注意看“阶乘.txt”的保存位置
#注意检查结果是否完全正确
#如果没有换行，扣50分
#方法一：定义求阶乘的函数
def fact(n):
    s=1
    for i in range(2,n+1):
        s=s*i
    return s
f=open("阶乘.txt","w")
for i in range(1,101):
    f.write(str(i)+"!="+str(fact(i))+"\n")
f.close()


#方法二：一边计算一边保存
f=open("阶乘.txt","w")
t=1
for i in range(1,101):
    t=t*i
    f.write(str(i)+"!="+str(t)+"\n")
f.close()
