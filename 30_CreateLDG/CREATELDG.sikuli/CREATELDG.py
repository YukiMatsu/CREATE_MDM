# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

# CSVファイルのインポート(
import csv
FILENAME = "C:\Program Files\SikuliX\LDG_data.csv"
f = open(FILENAME,"r")
reader = csv.reader(f)
CSVLDGLIST = []
for i in reader:
    CSVLDGLIST.append(i)
else:
    for LDNAM, LDEXP in CSVLDGLIST:
        # BOスキーマ作成
        click("2016-03-15_140321.png")
        click("2016-03-15_140411.png")
        wait("2016-03-15_140430.png", 15)
        click("2016-03-15_140458.png")
        click("2016-03-16_140802.png")
        type(Key.TAB)
        paste(LDNAM) # BO表示名入力
        type(Key.TAB)
        type(Key.TAB)
        type(Key.TAB)
        type(Key.TAB)
        paste(unicode(LDEXP,"cp932")) # BO説明を入力 
        click("2016-03-15_140543.png")
        wait(20)
        #wait("2016-03-16_151622.png",180)
    else:
        popup("ALL LDG setup finish")