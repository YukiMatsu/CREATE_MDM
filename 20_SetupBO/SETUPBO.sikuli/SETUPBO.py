# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

def SETUP():
    # テーブル名チェック
    click(Pattern("2016-03-22_213356.png").similar(0.81).targetOffset(-1,6))
    type("c",Key.CTRL)
    num = Env.getClipboard()
    if num == BONAM:
        click(Pattern("rireki2.png").similar(0.94).targetOffset(151,10))
        click(Pattern("syousai8.png").exact())    
        click(Pattern("jyoutaikanri.png").similar(0.78).targetOffset(168,153))
        click("save.png")
        wait(10)
        click(Pattern("kihonsyousai.png").exact().targetOffset(-17,0))
        # システムカラムを更新可能に設定
        type(Key.ENTER)
        type(Key.ENTER)
        type(Key.RIGHT)
        type(Key.DOWN)
        click("colum-1.png")
        dragDrop("bar.png","end.png" )
        click(Pattern("putable.png").targetOffset(-3,-156))
        click(Pattern("putable-1.png").targetOffset(-5,-135))
        click(Pattern("putable-2.png").targetOffset(-3,-115))
        click(Pattern("putable-2.png").targetOffset(-3,-93))
        click(Pattern("putable-2.png").targetOffset(-4,-72))
        click(Pattern("putable-2.png").targetOffset(-3,-50))
        click(Pattern("putable-2.png").targetOffset(-5,-32))
        click(Pattern("putable-2.png").targetOffset(-2,-8))
        click(Pattern("putable-2.png").targetOffset(-3,11))
        click(Pattern("putable-2.png").targetOffset(-2,31))
        click(Pattern("putable-2.png").targetOffset(-3,54))
        click(Pattern("putable-2.png").targetOffset(-2,76))
        click(Pattern("putable-2.png").targetOffset(-5,96))
        click(Pattern("putable-2.png").targetOffset(-4,118))
        click("save.png")
        wait(10)
        dragDrop("bar-1.png","start.png")
        click(Pattern("click.png").exact())
        type(Key.LEFT)
        type(Key.LEFT)
    else:
        confexe = popAsk("Uuups,not match " + BONAM)
        wait(3)
        if confexe == True:
            print("not match" + BONAM)
            exit(1)
        else:
            print("not match" + BONAM)
            

# CSVファイルのインポート(
import csv
FILENAME = "C:\Program Files\SikuliX\BO_data_ForIMP.csv"
f = open(FILENAME,"r")
reader = csv.reader(f)
IMPLIST = []
for i in reader:
    IMPLIST.append(i)
else:
    # セットアップの実行
    for TPNAM, BONAM, STNAM, LDNAM in IMPLIST:
        type(Key.DOWN)
        wait(3)
        if exists(Pattern("satag_fail-1.png").exact()):
            print("start_A")
            type(Key.ENTER)
            type(Key.ENTER)
            type(Key.DOWN)
            SETUP()
        else:
            print("start_B")
            type(Key.ENTER)
            type(Key.ENTER)
            SETUP()
    else:
        print("ALL BO SETUP finish")

