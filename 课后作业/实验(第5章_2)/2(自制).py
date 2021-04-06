#编写程序，输入一个十进制整数n，再输入一个进制base，把n转换为base进制，用七段数码管显示结果。
#要求：
#（1）写一个整数n转换为任意进制（小于等于16）的函数： def convert(n,base) 其中n是十进制整数，base表示进制。如convert(2019,16)表示把十进制整数2019转换为16进制。
#（2）作图窗口设置为800*400，从左边开始显示。颜色、画笔大小可自由设定，不能用默认值。
#（3）用字母A,b,C,d,E,F...依次表示10，11，12...
#（4）可以使用教材P140例7.2的函数
import turtle
n=eval(input('请输入一个十进制整数:'))
base=eval(input('请输入进制:'))
def convert(n,base):
    a=n
    b=base
    c=['0','1','2','3','4','5','6','7','8','9','A','b','C','d','E','F']
    d=''
    while a>1:
        e=a%b
        d=c[e]+d
        a=a//b
    return d
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):#绘制单条线
    drawGap()
    turtle.pendown() if draw else turtle.penup()#如果draw为True则画笔启动
    turtle.fd(100)
    drawGap()
    turtle.right(90)#向前移动40像素后，前进方向右转90度
def drawDigit(digit):#绘制单个数字，调用drawLine()函数
    drawline(True) if digit in ['2','3','4','5','6','8','9','A','b','d','E','F'] else drawline(False)
    drawline(True) if digit in ['0','1','3','4','5','6','7','8','9','A','b','d'] else drawline(False)
    drawline(True) if digit in ['0','2','3','5','6','8','9','b','C','d','E'] else drawline(False)
    drawline(True) if digit in ['0','2','6','8','A','b','C','d','E','F'] else drawline(False)
    turtle.left(90)#方向左转90度
    drawline(True) if digit in ['0','4','5','6','8','9','A','b','C','E','F'] else drawline(False)
    drawline(True) if digit in ['0','2','3','5','6','7','8','9','A','C','E','F'] else drawline(False)
    drawline(True) if digit in ['0','1','2','3','4','7','8','9','A','d',] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.pensize(5)
    turtle.pencolor('#520793')
    turtle.seth(180)
    turtle.fd(395)
    turtle.seth(0)
    for i in q:
        drawDigit(i)
    turtle.hideturtle()
    turtle.done()
q=convert(n,base)
print(q)
main()
