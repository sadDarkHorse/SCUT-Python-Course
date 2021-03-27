#使用turtle库绘制一个直径为200像素的圆，再绘制圆的内接正方形，如下图所示。
import turtle
turtle.circle(200)
turtle.seth(45)
turtle.fd(200*2**(1/2))
turtle.seth(135)
turtle.fd(200*2**(1/2))
turtle.seth(225)
turtle.fd(200*2**(1/2))
turtle.seth(315)
turtle.fd(200*2**(1/2))
