import cv2
import random
import string
from analyze import analyze_picture

#テスト用関数
def return_string():
    return 'this is TEST'

#カメラからスクショして保存
def capture_pic():
    cap = cv2.VideoCapture(0)

    #キャプチャを保存
    ret, frame = cap.read()
    file_name = create_ramdom_chr(16)
    write_img(file_name,frame)

    #メモリを解放して終了するためのコマンド
    cap.release()
    cv2.destroyAllWindows()

    return file_name

#画像を保存
def write_img(file_name:str ,img):
    cv2.imwrite('./img/'+file_name+'.jpg' , img)

#ランダムなn字の文字列を生成(ファイル名用)
def create_ramdom_chr(n: int) -> str:
    random_list = [random.choice(string.ascii_letters) for n in range(n)]
    return "".join(random_list)