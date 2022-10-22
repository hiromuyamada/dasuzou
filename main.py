from flask import Flask
from flask import render_template
from function import write_img,create_ramdom_chr,capture_pic
from analyze import analyze_picture

import cv2

app = Flask(__name__,static_folder='.', static_url_path='',template_folder='template')

@app.route('/')
def index():
    return render_template('/index.html',message="Welcome! If you want a picture, access '/get'")

@app.route('/get')
def get_people():
    str = capture_pic()
    people_number = analyze_picture(str)

    return render_template('/index.html',message=str+'.jpg',people=people_number)

app.run(port=8000, debug=True)