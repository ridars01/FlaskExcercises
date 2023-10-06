from flask import Flask , render_template
import datetime 
import calendar


app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template('index.html' , currentdate = datetime.datetime.now() , currentTime = datetime.now())

if __name__ == "__main__":
    app.run(debug=True)