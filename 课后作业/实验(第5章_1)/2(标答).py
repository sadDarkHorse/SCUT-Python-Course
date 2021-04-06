'''评分标准
1.函数GetRandomChar必须返回一个字符，否则扣10分.如果有循环，扣20分
2.函数GetRandomChar不能有print语句，否则扣10分，用全局变量扣10分
3.不能直接写出0-9，a-z的列表，也不能用程序生成全部字符，否则扣20分
4.每个字符出现的机会相等，如果不等扣20分
5.不用def定义函数，扣50分
'''
import random

def GetRandomChar():
    j = int(62*random.random())  #10个数字+26小写+26大写
    if j<10:
        s = str(j)
    elif j<36:
        s = chr(ord("a")+j-10)
    else:
        s = chr(ord("A")+j-36)
    return s


s = ""
n=int(input('请输入一个整数：'))
if n<5 or n>10:
    print('请输入5到10之间的整数')
else:
    for i in range(n):
        s=s+GetRandomChar()
    print("验证码为{}".format(s))        
