#定义函数def GetRandomChar()，返回一个随机的数字或大写或小写字母，每个符号出现的机会相等，不能使用字母对应的常数如65，97等。输入一个整数n（在5-10之间）然后调用该函数n次，生成并输出一个n位的验证码。不能把大小写字母和数字全写出来。
import random
import string
a=eval(input('请输入一个整数：'))
def GetRandomChar():
    char_lists = string.ascii_uppercase + string.ascii_lowercase + string.digits
    c=random.choice(char_lists)
    return c
if a<5 or a>10:
    print('请输入5到10之间的整数')
else:
    d=''
    for i in range(a):
        d+=GetRandomChar()
    print('{}{}'.format('验证码为',d))
