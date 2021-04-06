#)定义一个函数def DrawPic(n, char),它的功能是显示由字符char组成的图形，图形上半部分共n行，请参考下图
n=eval(input('请输入一个整数：'))
char=input('请输入一个字符：')
def DrawPic(n, char):
    a=n
    b=char
    for i in range(1,a+1):
        q=i*2-1
        print((a-i)*' ',q*b,(a-i)*' ')
    for i in range(a-1,0,-1):
        q=i*2-1
        print((a-i)*' ',q*b,(a-i)*' ')
DrawPic(n, char)
