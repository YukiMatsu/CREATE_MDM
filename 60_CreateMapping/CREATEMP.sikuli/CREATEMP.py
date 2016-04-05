# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

# CSVファイルのインポート(
import csv
FILENAME = "C:\Program Files\SikuliX\MP_data_2.csv"
f = open(FILENAME,"r")
reader = csv.reader(f)
CSVMPLIST = []
for i in reader:
    CSVMPLIST.append(i)
else:
    for BONAM, STNAM, MPNAM, MPEXP, LDNAM in CSVMPLIST:
        # BOスキーマ作成
        click(Pattern("stg.png").similar(0.90).targetOffset(3,8))
        click(Pattern("stg1.png").similar(0.80))
        wait("stagco.png", 30*60)
        paste(MPNAM) # STG表示名入力
        type(Key.TAB)
        paste(unicode(MPEXP,"cp932")) # STG説明を入力
        confexe = popAsk(u"STG名とLDG名を指定してください")
        if confexe == True:
            wait(10)
            click("2016-03-15_140543.png")
            wait(20)
            click(Pattern("2016-03-24_134517.png").similar(0.80).targetOffset(19,0))
            click(Pattern("mpp.png").similar(0.74))
            click(Pattern("MKK.png").similar(0.90))
            wait(10) 
            click(Pattern("2016-03-24_134539.png").targetOffset(-34,-1))
    else:
        popup("ALLMP create finish")