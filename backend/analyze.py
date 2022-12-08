# 画像解析のモジュール
# HOG特徴量+SVMを用いた解析(リサイズあり)
#

import numpy as np
import cv2
import os


def analyze_picture(file_name):

    # 解析結果の人数をreturnするために空のリストを作成する
    return_human = ""

    # 入出力ファイル
    input_dir = './img/'
    output_dir = './img/img_out/'
    file = file_name + '.jpg'
    file_path = input_dir + file

    # ファイル読込
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    
    #ファイルの読み込みに失敗した場合return
    if(image is None):
        return 'an error occured'

    hog = cv2.HOGDescriptor()
    hog = cv2.HOGDescriptor((48, 96), (16, 16), (8, 8), (8, 8), 9)

    # SVMによる人検出
    hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

    # リサイズした方が精度がよかった
    finalHeight = 800.0
    scale = finalHeight / image.shape[0]
    image = cv2.resize(image, None, fx=scale, fy=scale)

    # 人を検出した座標
    human, r = hog.detectMultiScale(image, hitThreshold=0.6, winStride=(
        8, 8), padding=(32, 32), scale=1.05)
    # 全員のバウンディングボックスを作成

    for (x, y, w, h) in human:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # ファイルを保存
    cv2.imwrite(output_dir + file, image)
    print(file + ":" + str(len(human)) + "人")
    return_human = str(len(human))
    # print(return_human)

    #ファイル削除
    os.remove(file_path)

    return (return_human)
