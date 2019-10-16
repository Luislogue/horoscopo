from flask import Flask , render_template,request
from horoscope_api import get_horoscope, zodiac_sign
from datetime import datetime

app = Flask("My Flask App")


@app.route("/") 
def default_path():
	return render_template ("index.html") 


@app.route("/horoscope", methods=["POST"])
def read_form():
	form_data = request.form
	date = datetime.strptime(form_data["dob"], '%Y-%m-%d').date()
	month = date.month
	day = date.day
	print(date)
	sign= zodiac_sign (month,day)
	print(sign)
	data = get_horoscope(sign)
	return render_template ("myhoroscope.html",data=data) 
	#return "All OK"


if __name__ == '__main__':
	app.run(debug=True)