def GetRandomChar():
    import random
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b="abcdefghijklmnopqrstuvwxyz"
    c="0123456789"
    random_str=""
    single=random.choice(a+b+c)
    random_str+=single
    return random_str
code=""
for i in range(8):
    code+=GetRandomChar()
print("8位验证码为:{}".format(code))
