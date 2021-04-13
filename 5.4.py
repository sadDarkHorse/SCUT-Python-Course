def IsPrime(m):
    if m <= 1:
        return False
    i = 2
    while i*i <= m:
        if m % i == 0:
            return False
        i += 1
    return True
m=int(input("请输入整数m:"))
n=int(input("请输入整数n:"))
total=0
for i in range(m,n+1):
    if IsPrime(i):
        total+=i
print("范围在[{0}，{1}]的素数和为:{2}".format(m,n,total))
