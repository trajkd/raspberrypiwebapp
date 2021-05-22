from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("./ServiceAccountKey.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		now = datetime.now()
		doc_ref = db.collection(u'data').document(u'person'+now.strftime("%d%m%Y|%H:%M:%S"))
		doc_ref.set({
			u'name': request.form['name'], 
			u'surname': request.form['surname']
			}, merge=True)
		return request.form['name'] + " " + request.form['surname'] + " succesfully added."
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')