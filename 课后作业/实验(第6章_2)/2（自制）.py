# coding=UTF-8
#(程序设计)用随机函数生成50个范围在[1,999]的随机整数，把这50个整数保存到列表。编写程序，对这50个数从小到大进行排序，并按每行10个输出（要求数据的个位对齐）。注意：不能使用sort,sorted,max, min,index函数，在排序的时候原列表不能删除元素，不能增加元素，不能生成新的列表，只能原地排序。方法：先找出全部数据的最小值，把它放在第0个位置，然后在剩下的数据找最小值放在第1个位置，依此类推。不能用其它方法。
import random
ls=[]
for i in range(50):#生成50个随机整数
    ls.append(random.randint(1,999))
def selectionSort(arr):#对这五十个数从小到大进行排序
    for i in range(len(arr) - 1):#选择排序
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
selectionSort(ls)
a=0
for i in ls:
    print('{:>3}'.format(i),end='  ')
    a+=1
    if a==10:
        print()
        a=0
