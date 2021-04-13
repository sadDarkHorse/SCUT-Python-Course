def DrawPic(n,char):
    for i in range(n):
        single1=char+char*(2*i)
        print(" "*(n-(i+1)),end="")
        print("{0:}".format(single1))
    for i in range(n):
        if i != 0:
            print(" "*i,end="")
            single2=char+char*2*(n-1-i)
            print("{0:}".format(single2))
n=int(input("请输入一个整数："))
char=input("请输入一个字符：")
DrawPic(n,char)
