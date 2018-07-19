
from flask import Flask, render_template, request

from datetime import datetime 

app = Flask("HomeApp")

@app.route("/")
def home_default():
	return render_template('Home.html')

@app.route("/dob", methods=["POST"])
def get_dob():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	dateOfBirth =  form_data["dob"] # from the form object getting value of dob field.
	date = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
	month = date.month
	year = date.year
	
	return dob 

def calculate_age(_year):
	weekend = 'N/A'
	if user_year <=2018 and user_month <=6 and user_day <=25:
		weekend = 'Try again when you are 18 or grab a mocktail!' 
	if user_year >=2018 and user_month >=6 and user_day >=26:
		weekend = 'Have a great Weekend!' 
	
   	return weekend

# user_dob = get_dob()
# user_year = datetime.strptime(user_dob,'%m/%d/%Y').year
# user_month = datetime.strptime(user_dob,'%m/%d/%Y').month
# user_day = datetime.strptime(user_dob,'%m/%d/%Y').day
# user_gen = calculate_age(user_year)

# print 'Your DOB :' + user_dob
# print 'Your Weekend:' + user_gen

app.run(debug=True)