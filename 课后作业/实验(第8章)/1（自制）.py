'''【1】 (程序设计)制作英文学习词典。词典有3个基本功能：添加，查询和退出。程序读取源文件路径下的“我的词典.txt”文件，若没有就创建一个。
程序根据用户的选择进入相应的模块，并显示相应的操作提示。当添加的单词已经存在时，把新输入的中文作为新的释义（即允许多重释义）。
当查询的单词不存在时，要提示“词典库没有该单词”。用户输入其它选项，提示“输入错误”。'''
def menu():#菜单
    print('{:^10}'.format('我的英汉词典'))
    print('-' * 16)
    print('1.增加单词')
    print('2.查询')
    print('3.退出')
    select = input('请选择(1-3):')#进行选择，跳转到相应的函数
    if select == '1':
        addword()
    elif select == '2':
        searchword()
    elif select == '3':
        savedictionary()
    else:
        print('输入错误')
        menu()
def addword():#增加单词
    word = input('请输入英文单词:')
    translation = input('请输入中文释义:')
    if dict.get(word):#如果单词已经存在，就在原意后添加
        dict[word] = dict.get(word) + ';' + translation
    else:#不存在则建立新的
        dict[word] = translation
    menu()
def searchword():#搜索单词
    word = input('请输入英文单词:')
    if dict.get(word):
        print('{}的中文意思是{}'.format(word, dict.get(word)))
    else:
        print('词典里没有{}单词！'.format(word))
    menu()
def savedictionary():#保存字典
    fo = open('我的词典.txt', 'w', encoding='UTF-8')
    fo.write(str(dict))#将字典直接以字符串保存到txt中
    fo.close()
def readdictionary():#读取字典
    fo=open('我的词典.txt', 'a+')#如果文件不存在，则创建
    fo.close()
    fo=open('我的词典.txt', 'r+', encoding='UTF-8')#打开文件并读取
    a=fo.read()
    fo.close()
    if a=='':
        a={}
    else:
        a=eval(a)#将读取到的字符串转为字典
    return a
dict=readdictionary()
menu()
