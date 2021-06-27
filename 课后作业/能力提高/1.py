'''【1】 (程序设计)如果一个数恰好等于它的因子之和，这个数就称为“完数”。例如28=1+2+4+7+14则28就是一个完数。编写程序，输出1000以内的所有完数个数。'''
geshu=0
for i in range(1,1000):
    sum=0
    for k in range(1,i):
        if i%k==0:
            sum+=k
    if sum==i:
        geshu+=1
print(geshu)
