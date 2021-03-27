#使用turtle库，绘制一个边长为100的八角图形。
#方法二 
import turtle

a=0
for i in range(8):
    turtle.seth(a)
    turtle.fd(100)
    a=a+135
