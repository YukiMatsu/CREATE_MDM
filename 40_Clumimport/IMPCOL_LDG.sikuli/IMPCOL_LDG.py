# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

def CloumCheck():
    # テーブル名チェック
    click(Pattern("2016-03-22_213356.png").similar(0.81).targetOffset(-1,6))
    type("c",Key.CTRL)
    num = Env.getClipboard()
    if num == LDNAM:
        type(Key.ENTER)
        click(Pattern("2016-03-22_230923.png").similar(0.83).targetOffset(12,0))
        type(Key.RIGHT)
        type(Key.DOWN) # 「カラム」を開く
        click("imp.png")
        # 接続情報の入力
        wait(1)
        type(Key.TAB)
        wait(1)
        paste("10.36.114.188")
        wait(1)
        type(Key.TAB)
        wait(1)
        paste("XXDEVD01")
        type(Key.TAB)
        wait(1)
        paste("xmdevdb3")
        type(Key.TAB)
        wait(1)
        paste("1433")
        type(Key.TAB)
        wait(1)
        paste("sa")
        type(Key.TAB)
        wait(1)
        paste("pndZCq3e")
        type(Key.TAB)
        type(Key.TAB)
        type(Key.TAB)
        type(Key.TAB)
        type(Key.ENTER)
        # テーブル名の検索
        click(Pattern("2016-03-22_161609.png").exact().targetOffset(0,14))
        type("c",Key.CTRL)
        r = Env.getClipboard()            
        while r != TPNAM:
            type(Key.DOWN)
            type("c",Key.CTRL)
            r = Env.getClipboard()
        else:
            type(Key.TAB)
            type(Key.TAB)
            type(Key.TAB)
            type(Key.ENTER)
            #click(Pattern("2016-03-22_200803.png").targetOffset(138,89))
            # インポートカラムのチェック 
            click("2016-03-h22_151056.png")
            type(Key.TAB)
            type(Key.TAB)
            type(Key.ENTER)
            # 保存
            click("save.png")
            wait(10)
            click(Pattern("click.png").similar(0.89))
            type(Key.LEFT)
            type(Key.LEFT)
    else:
        confexe = popAsk("Uuups,not match " + LDNAM)
        if confexe == True:
            print("not match" + BONAM)
            exit(1)
        else:
            print("not match" + BONAM)
# CSVファイルのインポート(
import csv
FILENAME = "C:\Program Files\SikuliX\BO_data_ForIMP_3.csv"
f = open(FILENAME,"r")
reader = csv.reader(f)
IMPLIST = []
for i in reader:
    IMPLIST.append(i)
else:
    for TPNAM, BONAM, STNAM, LDNAM in IMPLIST:
        type(Key.DOWN)
        wait(3)
        if exists(Pattern("satag_fail-1.png").exact()):
            print("start_A")
            click(Pattern("2016-03-22_230923.png").exact().targetOffset(12,0))
            type(Key.DOWN)
            CloumCheck()
        else:
            print("start_B")
            CloumCheck()
    else:
        print("ALL LDG import finish")
