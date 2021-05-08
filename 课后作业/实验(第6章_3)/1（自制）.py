#1、(程序设计)输入一个字符串，找出该字符串出现次数最多的字符。比如，输入abc12d3ebaa，出现次数最多的字符是a。如果次数最多的有多个字符，输出任意一个即可。注意：不能用max，sort，sorted函数(本题分数:20)
string=input('请输入一个字符串:')
a=list(string)
b=0
for word in string:#计算每个字符出现的次数
    c=a.count(word)
    if b<c:
        b=c
        d=word
print('出现次数最多的字符是{}'.format(d))
