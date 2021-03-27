#输入2个正整数，输出这两个数字之间的全部数字，用逗号分隔，每行5个。注意每行最后一个数字后面没有逗号。运行结果参考下图。
for i in range(0,b-a+1):
    if i % 5==4 or i==b-a:
        print(a+i)
    else:
        print(a+i,end=',')
