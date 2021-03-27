#编写程序，输入三个数，按从小到大的顺序输出这三个数。提示：使用python内置函数max和min，不需要用if语句。运行结果参考下图。
a=int(input('请输入第一个数：'))
b=int(input('请输入第二个数：'))
c=int(input('请输入第三个数：'))
MAX=max(a,b,c)
MIN=min(a,b,c)
MIDDLE=a+b+c-MAX-MIN
print('从小到大的顺序为：{0} {1} {2}'.format(MIN,MIDDLE,MAX))
