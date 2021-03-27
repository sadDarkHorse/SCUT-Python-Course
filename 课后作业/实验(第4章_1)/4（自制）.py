#输入2个正整数，输出这两个数字之间的全部数字，用逗号分隔，每行5个。注意每行最后一个数字后面没有逗号。运行结果参考下图。
a=eval(input('输入开始数字：'))
b=eval(input('输入结束数字：'))
c=1
for i in range(a,b+1):
    if c%5==0 or i==b:
        print(i)
    else:
        print(i,end=',')
    c+=1
