#评分标准：输入大小写字母，能输出正确的字母图形，如果输入其它字符图形不对，不扣分
#如果用到64，65这样的常数，扣10分。没有考虑到开始大于结束的情况，扣10分
#每行多一个或少一个字符，扣10分。如果用到列表或元组，扣10分
a = input("请输入开始字母:")
b = input("请输入结束字母:")
if a>b:
    a,b=b,a
for i in range(ord(a),ord(b)+1):
    for j in range(i,ord(b)+1):   
        print(chr(j),end='')
    for j in range(ord(a),i):
        print(chr(j),end='')
    print()
