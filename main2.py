# Source: https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    #app.run(debug=True)
	# app.run(host='0.0.0.0', port=5001)
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))