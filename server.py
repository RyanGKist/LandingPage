from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index ():
	return render_template("index.html")


@app.route('/dojos/new')
def dojo_form():
	return render_template("dojos.html")

@app.route('/ninjas')
def ninjas():
	return render_template("ninja.html")

app.run(debug=True)