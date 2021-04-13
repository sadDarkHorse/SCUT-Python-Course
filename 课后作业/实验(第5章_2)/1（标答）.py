#如果没有定义函数，扣20分。函数内有input语句，扣10分
def DrawPic(n,char):
    for i in range(n):
        print('{}{}'.format((n-i-1)*' ',(2*i+1)*char))
        
    #下半部分只有n-1行
    for i in range(1,n):
        print('{}{}'.format(i*' ',(2*(n-i)-1)*char))


n=eval(input('请输入一个整数:'))
c=input('请输入一个字符:')
DrawPic(n,c)
