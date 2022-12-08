from function import capture_pic
from analyze import analyze_picture
from calc_minutes import calc
from save_to_db import save
import datetime

menus = [
    "curry",
    "teishoku",
    "noodle",
    "soba",
    "sagamiharaLunch",
    "aburasoba",
    ]

def workflow(menu):
    str = capture_pic()  #カメラでキャプチャしてファイル名を返す
    people_number = analyze_picture(str) #人数の検出,人数を返す
    minutes = calc(people_number,menu) #待ち時間の計算
    rtn = {"people":people_number, 
            "minute":minutes, 
            'created_at':datetime.datetime.now()
           }
    return rtn

def work():
    for menu in menus:
        menu_info = workflow(menu)
        print(menu_info)
        save(menu, menu_info)