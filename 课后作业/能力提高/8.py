'''【8】 (程序设计)用户输入一行字符串，统计并输出其中空格、数字、英文字母、其他字符的个数，输入输出格式如下：
例如：
请输入字符串：Version 3.1415
输入的字符串有1个空格，5个数字，7个英文字母，1个其它字符'''
a=input('请输入字符串：')
kongge,shuzi,zimu,qita=0,0,0,0
for i in a:
    if ord(i)>=ord('a') and ord(i)<=ord('z'):
        zimu+=1
    elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
        zimu+=1
    elif ord(i)>=ord('0') and ord(i)<=ord('9'):
        shuzi+=1
    elif i==' ':
        kongge+=1
    else:
        qita+=1
print('输入的字符串有{}个空格，{}个数字，{}个英文字母，{}个其它字符'.format(kongge,shuzi,zimu,qita))
