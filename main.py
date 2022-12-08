from flask import Flask
from flask import render_template
from function import capture_pic
from analyze import analyze_picture
from calc_minutes import calc
from flask_cors import CORS
from flask import request
from workflow import work
from apscheduler.schedulers.background import BackgroundScheduler
import json

schedule = BackgroundScheduler(daemon=True)
schedule.add_job(work, 'interval', minutes=1)
schedule.start()

app = Flask(__name__,static_folder='.', static_url_path='',template_folder='template')
CORS(app)

@app.route('/')
def index():
    return render_template('/index.html',message="Welcome! If you want a picture, access '/get'")

@app.route('/get')
def get_people():
    str = capture_pic()
    people_number = analyze_picture(str)

    return render_template('/index.html',message=str+'.jpg',people=people_number)

@app.route('/api/get', methods=['post'])
def get_people_api():
    place = request.data
    place = json.loads(place)['place']
    str = capture_pic()
    people_number = analyze_picture(str)
    minutes = calc(people_number,place)

    return minutes

app.run(host='127.0.0.1', port=8000, debug=True,use_reloader=False)