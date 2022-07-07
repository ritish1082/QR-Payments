import csv
import os
from flask import Flask, render_template, request, url_for, session, send_file
from src import qrcode_generator as qr
from src import prepare_qrcode_data as pqrd

# create flask app
app = Flask(__name__)

app.secret_key="1234"
session_username=None

global data
data = {}

@app.route('/', methods=['GET'])
def homePage():

    session["username"]=session_username
    return render_template('home.html')
    

@app.route('/login', methods=['GET', 'POST'])
def login():

    username = request.form["username"]
    password = request.form["password"]

    registration_file = open('./static/data/UserRegistrationData.csv')
    users_data = csv.reader(registration_file)

    for user_data in users_data:

        if user_data[0]==username and user_data[1]==password:
            session["username"]=username

            return render_template('home.html')

    if session["username"]==None:
        return render_template('Login.html', status="Invalid Login Attempt")


@app.route('/getStalls', methods=['GET'])
def stallsPage():

    stalls_names = ['BombayChat', 'ChillZone', 'FastFood', 'Frankie']

    if session["username"]!=None:

        return render_template('stalls.html', stalls_names=stalls_names)


    else:
        return render_template('Login.html', status=None)


@app.route('/orderFood/<stall_name>', methods=['GET', 'POST'])
def orderFood(stall_name):

    file = open('./static/data/'+stall_name+'.csv')
    file_reader = csv.reader(file)

    food_items = []

    for row in file_reader:

        food_items.append(row)

    file.close()

    no_of_food_items = len(food_items)

    return render_template('orderFood.html', username=session["username"], stall_name=stall_name, no_of_food_items=no_of_food_items, food_items=food_items)


@app.route('/enterPin/<stall_name>', methods=['GET', 'POST'])
def enterPin(stall_name):

    session["stallName"] = stall_name
    global data
    data=dict(request.form)

    return render_template('pin.html', status=None)


@app.route('/generateQRCode', methods=['GET', 'POST'])
def generateQRCode():

    pin=''

    for i in range(1, 7):
        pin+=request.form['digit-'+str(i)]

    registration_file = open('./static/data/UserRegistrationData.csv')
    users_data = csv.reader(registration_file)

    username = session["username"]
    flag=0

    for user_data in users_data:

        if user_data[0]==username and user_data[2]==pin:
            flag=1

    if flag:

        global data
        data["password"]=pin
        data=pqrd.structure_data(session["stallName"], data)

        filename=data["userData"]["username"]+'_qrcode'

        status = qr.generate_qrcode(str(data), filename)

        session[filename]=filename+'.png'

        return render_template('serveQRCode.html', filename=filename+'.png')

    else:

        return render_template('pin.html', status="Invalid Pin")


@app.route('/downloadQRCode/<filename>', methods=['GET'])
def downloadQRCode(filename):

    return send_file('./static/qrcodes/'+filename, as_attachment=True)


@app.route('/clearSession', methods=['GET'])
def clearSession():

    for filename in session.keys():

        try:
            os.remove('./static/qrcodes/'+filename+'.png')

        except:
            continue

    return render_template('home.html')
            

if __name__ == '__main__':
    app.run(debug=True)