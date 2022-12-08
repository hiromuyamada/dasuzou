import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import datetime

cred = credentials.Certificate("./env/dasuzou-c609a-firebase-adminsdk-eirnk-7e954d463c.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save(menu_name, menu_info):
    doc_ref = db.collection(menu_name).document()
    doc_ref.set(menu_info)