# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

# CSVファイルのインポート(
import csv
FILENAME = "C:\Program Files\SikuliX\BO_data.csv"
f = open(FILENAME,"r")
reader = csv.reader(f)
CSVBOLIST = []
for i in reader:
    CSVBOLIST.append(i)
else:
    # 排他ロックの取得（共通処理
    #click("2016-03-15_145134.png")
    #click("2016-03-15_145206.png")
    # スキーマツールへのアクセス（処理待ち    
    #click(Pattern("2016-03-15_140235.png").similar(0.94).targetOffset(-12,0))
    #wait(Pattern("2016-03-15_140321.png").exact(),40)
    for BONAM, BOEXP in CSVBOLIST:
        # BOスキーマ作成
        click("2016-03-15_140321.png")
        click("2016-03-15_140411.png")
        wait("2016-03-15_140430.png", 30*60)
        click("2016-03-15_140458.png")
        click("2016-03-15_140526.png")
        type(Key.TAB)
        paste(BONAM) # BO表示名入力
        type(Key.TAB)
        type(Key.TAB)
        type(Key.TAB)
        type(Key.TAB)
        paste(unicode(BOEXP,"cp932")) # BO説明を入力
        click("2016-03-15_140543.png")
        wait(10)
    else:
        popup("ALLBO setup finish")