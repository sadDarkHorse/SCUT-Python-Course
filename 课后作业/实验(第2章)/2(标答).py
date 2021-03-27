#使用turtle库绘制一个直径为200像素的圆，再绘制圆的内接正方形，如下图所示。
import turtle

r=200
a=r*1.414  #正方形的边长
turtle.circle(r)
turtle.seth(45)
turtle.fd(a)
turtle.seth(135)
turtle.fd(a)
turtle.seth(225)
turtle.fd(a)
turtle.seth(315)
turtle.fd(a)
