def IsPerfectSquare(n):
    a=int(pow(n,1/2))
    if a*a==n:
        return True
    else:
        return False
def IsSameDigit(n):
    a=str(n)
    b=list(a)
    new=[]
    for i in b:
        if i not in new:
            new.append(i)
    if len(b)==len(new):
        return False
    else:
        return True
a=int(input("请输入整数a:"))
b=int(input("请输入整数b:"))
S=0
for m in range(a,b+1):
    if IsPerfectSquare(m):
        if IsSameDigit(m):
            S+=1
print("在[{0},{1}]共有{2}个数满足条件".format(a,b,S))
