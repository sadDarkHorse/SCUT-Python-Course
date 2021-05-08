s=input("请输入字符串:")
a=set(s)
count,ch=0,''
for i in a:
    j=s.count(i)
    if j>count:
        count,ch=j,i
print('出现次数最多的字符是{}'.format(ch))
