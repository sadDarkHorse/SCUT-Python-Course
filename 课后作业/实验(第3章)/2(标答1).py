#编写程序，输入三个数，按从小到大的顺序输出这三个数。提示：使用python内置函数max和min，不需要用if语句。运行结果参考下图。
#方法一：先求出最大值和最小值再输出
#输出结果不对，最多给50分。不用input语句扣20分，输出没有中文提示扣20分
a=eval(input("请输入第一个数:"))
b=eval(input("请输入第二个数:"))
c=eval(input("请输入第三个数:"))
d=max(a,b,c)
e=min(a,b,c)
print("从小到大的顺序为:",e,a+b+c-d-e,d)
