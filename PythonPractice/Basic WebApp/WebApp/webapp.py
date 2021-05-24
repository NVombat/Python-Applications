from flask import Flask, render_template

#Instantiate object
app = Flask(__name__)

#Decorator -> The output of the function is mapped to this url route
@app.route('/')
def home():
    return render_template("home.html")

#Decorator -> The output of the function is mapped to this url route
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)