#编写程序，输入三个数，按从小到大的顺序输出这三个数。提示：使用python内置函数max和min，不需要用if语句。运行结果参考下图。
#方法二：用if语句（第4章讲），直接判断.如果没考虑相等情况，扣20分
if a<=b<=c:
    print(a,b,c)
if a<=c<=b:
    print(a,c,b)
if b<=a<=c:
    print(b,a,c)
if b<=c<=a:
    print(b,c,a)
if c<=a<=b:
    print(c,a,b)
if c<=b<=a:
    print(c,b,a)
