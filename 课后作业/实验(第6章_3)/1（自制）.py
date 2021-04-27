string=input('请输入一个字符串:')
a=list(string)
b=0
for word in string:#计算每个字符出现的次数
    c=a.count(word)
    if b<c:
        b=c
        d=word
print('出现次数最多的字符是{}'.format(d))
