import random
a=eval(input('请输入一个整数：'))
def GetRandomChar():
    list = []
    for i in range(ord('0'),ord('9')+1):
        list.append(i)
    for i in range(ord('a'),ord('z')+1):
        list.append(i)
    for i in range(ord('A'),ord('Z')+1):
        list.append(i)
    c=chr(random.choice(list))
    return c
if a<5 or a>10:
    print('请输入5到10之间的整数')
else:
    d=''
    for i in range(a):
        d+=GetRandomChar()
    print('{}{}'.format('验证码为',d))
