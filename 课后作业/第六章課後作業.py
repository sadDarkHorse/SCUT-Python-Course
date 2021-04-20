import datetime,turtle
#把 n 转换为 base 进制，结果是字符串
def Convert(n,base):
    if n==0:
        return "0"
    else:
        s = ""
        while n>0:
            a = n % base 
            if a>9:
                s = chr(ord("A")+a-10) + s
            else:
                s = str(n%base) + s
 
            n //= base
        return s
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
 
def drawLine(draw): #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap() 
    turtle.right(90)
 
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in '2345689ABDEF' else drawLine(False)
    drawLine(True) if d in '013456789ABD' else drawLine(False)
    drawLine(True) if d in '0235689BCDE' else drawLine(False)
    drawLine(True) if d in '0268ABCDEF' else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in '045689ABCEF' else drawLine(False)
    drawLine(True) if d in '02356789ACEF' else drawLine(False)
    drawLine(True) if d in '01234789AD' else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
n = eval(input("请输入一个十进制整数:"))
base = eval(input("请输入进制:"))
s = Convert(n,base)
print(s)
turtle.setup(800,400)
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pencolor("blue")
turtle.pensize(5) 
for i in s:
    drawDigit(i)
turtle.hideturtle()
		
