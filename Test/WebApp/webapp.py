#Import libraries
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from email.mime.text import MIMEText
import sqlite3 as s
import smtplib
import os


#Instantiate flask object and configure it
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


'''
Function to create a table in the sql database
Takes the path to the database and connects to it
Creates a cursor object to execute commands
Creates a table if it doesnt exist in the database with Email and Height columns
Commits the changes so they become permanent
'''
def create_tbl(path:str):
    conn = s.connect(path)
    cur = conn.cursor()

    tbl = "CREATE TABLE IF NOT EXISTS data (Email TEXT, Height INT)"
    cur.execute(tbl)
    conn.commit()


'''
Function to insert data into the table
Connects to database and then checks if the email already exists in the database
If the email exists then the height value is updated
If the email doesnt exist then the height value is inserted
Commit changes
data[0] = email
data[1] = height
'''
def insert(path:str, tablename:str, data:tuple):
    conn = s.connect(path)
    cur = conn.cursor()

    #print("EMAIL:",data[0])
    #print("HEIGHT:",data[1])

    chk = f"SELECT * FROM {tablename} WHERE Email='{data[0]}'"
    cur.execute(chk)
    res = cur.fetchall()
    if len(res)==0:
        ins = f"INSERT INTO {tablename} VALUES{data}"
        cur.execute(ins)
        #print("NEW DATA INSERTED")
    else:
        upd = f"UPDATE {tablename} SET Height='{data[1]}' WHERE Email='{data[0]}'"
        cur.execute(upd)
        #print("HEIGHT UPDATED")
    conn.commit()


'''
Function to get the average height of all users and the number of users whose heights are being considered
Connects to database and fetches all heights from the table
Calculates the formatted average of all the heights and returns the average and the count
'''
def get_avg_height(tablename:str):
    conn = s.connect(path)
    cur = conn.cursor()

    avg = f"SELECT Height FROM {tablename}"
    cur.execute(avg)
    res = cur.fetchall()

    sum_height = 0
    for h in res:
        sum_height+=h[0]
    avg_height = sum_height/len(res)
    avg_height = "{:.2f}".format(avg_height)

    return (avg_height, len(res))


'''
Function to send email to the user
Access the email and password from the environment variables set on the laptop
This protects the email id and password
Uses the smtp library and MIMEText to create an email with subject and body
Send it to the users email id
'''
def sendmail(data:tuple):
    from_email = os.environ.get('backend_mail')
    from_password = os.environ.get('backend_pwd')
    to_email = data[0]

    subject = "Height Data"

    message = "Hey there! Your height is <strong>%s</strong> cm <br>The Average height is <strong>%s</strong> cm from a population of <strong>%s</strong> people" % (data[1],data[2],data[3])

    msg = MIMEText(message, 'html')
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)


# Path used for table
path = "app.db"
create_tbl(path)


# #Decorator -> The output of the function is mapped to this url route
@app.route('/')
def index():
    return render_template("index.html")


#Decorator -> The output of the function is mapped to this url route
#This webpage has post and get methods thus allowing us to access the input data
@app.route('/success', methods=["POST", "GET"])
def success():
    #If the user presses submit a post request is generated
    if request.method == "POST":
        #Fetch the email and height the user has entered
        email = request.form["email_name"]
        height = request.form["height_name"]
        #Create a tuple of the users data
        inp = (email, height)
        #print("USER INPUT:", inp)
        #Insert data into database
        insert(path, "data", inp)

        #Calculate the average height and the number of users that are being considered
        avg_height = get_avg_height("data")[0]
        count = get_avg_height("data")[1]
        #Create a tuple for the mail function
        mail_data = (email, height, avg_height, count)
        #Send a mail to the user
        sendmail(data=mail_data)
    return render_template("success.html")


#IF INPUT IS FILE: UPLOAD DOWNLOAD
#Decorator -> The output of the function is mapped to this url route
# @app.route('/')
# def index_file():
#     return render_template("index_file.html")


#Decorator -> The output of the function is mapped to this url route
#This webpage has post and get methods thus allowing us to access the input data
# @app.route('/success_file', methods=["POST", "GET"])
# def success_file():
#     #Creates a global variable as the file needs to be accessed by two functions
#     global file
#     #If the user presses submit a post request is generated
#     if request.method == "POST":
#         #print("FILE UPLOADED")
#         #Fetch the file that the user has uploaded
#         file = request.files["file"]
#         #Save the file in the same directory
#         file.save(secure_filename("uploaded"+file.filename))
#         #Access the data by reading the file and then store it in a variable
#         #content = file.read()

#         #Write to file
#         with open("uploaded"+file.filename, 'a') as f:
#             f.write("Add any data to file")
#         #Go to page with download button
#         return render_template("index_file.html", btn="download.html")
#     return render_template("success.html")


#Decorator -> The output of the function is mapped to this url route
#This webpage has post and get methods thus allowing us to access the input data
# @app.route('/download', methods=["POST", "GET"])
# def download():
#     #When the download button is clicked we let the user download the file
#     return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)