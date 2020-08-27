from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

import csv

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def index(page_name=None):
	return render_template(page_name)


def write_to_csv(data):
	with open('./venvv/database.csv',mode='a') as database2:
		Email=data["Email"]
		Subject=data["Subject"]
		Message=data["Message"]
		spamwriter=csv.writer(database2, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([Email, Subject, Message])
	

@app.route('/submit_contact', methods=['POST', 'GET'])
def submit_contact():
	if request.method == 'POST':
		data=request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong'

	
   

