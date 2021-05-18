'''【1】 (程序设计)编写程序，计算1到100的阶乘，把阶乘结果保存到文本文件“阶乘.txt”。'''
fo=open('阶乘.txt','w')
for i in range(101):
    result=1
    for j in range(i):
        result*=(j+1)
    fo.writelines('{}!={}\n'.format(i,result))
fo.close()
