

"""
CoDeR= Furkan Ceran
"""
#-------iMPORTLAR---------------------------------------------------------------------------------------------------
import csv
import time
import os
import random
from os import environ
import sys
import urllib
from flask import Flask, redirect, render_template, request, url_for,flash
from flask_socketio import SocketIO, emit
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import requests		
from random import randint
import pymysql.cursors
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
from binance.client import Client
#1998-949

def getbalance(data):
    API_KEY=data["binaceapikey"]
    API_SECRET=data["apisecretkey"]
    client = Client(API_KEY, API_SECRET)

    time_res = client.get_server_time()

    RECV_WINDOW=6000

    class Monitor:
        def __init__(self):
            self.bac = Client(API_KEY,API_SECRET)
        def my_balance(self):
            return(self.bac.get_account(recvWindow=RECV_WINDOW))

    
    m = Monitor()
    balances=m.my_balance()
    for balance in balances["balances"]:
        if balance["asset"]=="BTC":
            BTC=balance["free"] 
            data["Balance"].update({"BTC":BTC})
def createtable():
    connectionObject   = pymysql.connect(host='kriptonitbot.mysql.pythonanywhere-services.com',
                        user='kriptonitbot',
                        password='1998-949',
                        db='kriptonitbot$users',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)
    try:
        # Create a cursor object
        cursorObject        = connectionObject.cursor()                                     
        # SQL query string
        sqlQuery            = "CREATE TABLE login(id int, username varchar(32), passwords varchar(32), binaceapikey varchar(32), apisecretkey varchar(32))"   
        # Execute the sqlQuery
        cursorObject.execute(sqlQuery)
        # SQL query string
        sqlQuery            = "show tables"   
        # Execute the sqlQuery
        cursorObject.execute(sqlQuery)
        #Fetch all the rows
    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connectionObject.close()


def login(user,password):
    try:
        db = pymysql.connect(host='kriptonitbot.mysql.pythonanywhere-services.com',
                                    user='kriptonitbot',
                                    password='1998-949',
                                    db='kriptonitbot$users',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT username, passwords,binaceapikey,apisecretkey FROM login ORDER BY username")
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
            if row["username"] == user:
                if row["passwords"]== password:
                    binanceapi=row["binaceapikey"]
                    secret=row["apisecretkey"]
                    return {"login":True,"binaceapikey":binanceapi,"apisecretkey":secret}
            return False
        cursor.close()
        
    except Exception as error :
        print(error)


def registersystem(username,password,binaceapikey,apisecretkey):
    try:
        conn = pymysql.connect(host='kriptonitbot.mysql.pythonanywhere-services.com',
                                    user='kriptonitbot',
                                    password='1998-949',
                                    db='kriptonitbot$users',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        sql = """insert into `login` (username,passwords,binaceapikey,apisecretkey)
                values (%s, %s, %s, %s) 
            """
        cur.execute(sql,(username,password,binaceapikey,apisecretkey))
        conn.commit()
    except Exception as error :
        print(error)   







def background_thread(data):
    btc=0
    while True:
        
        socketio.sleep(2)

        btc=data["Balance"]["BTC"]

        
        socketio.emit('my_response',
                      {'data':'Values', 'btc': btc},
                      namespace='/carpi')



##################################################################################################################
#--------------------DECODE--------------------------------------------------------------------------------------#
##################################################################################################################

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/navi", methods=['GET', 'POST'])
def navigation():
    return render_template("navigation.html")
@app.route("/message", methods=['GET', 'POST'])	
def message():
    return render_template("chat.html")
@app.route("/about")
def about():
        return render_template("about.html")
@app.route("/exit", methods=['GET', 'POST'])
def exit():
        return render_template("index.html")
@app.route("/register", methods=['GET', 'POST'])
def register():
        return render_template("register.html")
@app.route("/registerform", methods=['GET', 'POST'])
def registerform():
        user = request.form.get("user") # seed formumdan seedi al
        passw = request.form.get("pass")
        binancekey= request.form.get("binancekey")
        secretkey=request.form.get("hiddenkey")
        registersystem(user,passw,binancekey,secretkey)
        return render_template("index.html")
@app.route("/advise")
def advise():
        return render_template("suggestions.html")
@app.route("/sifremiunuttum", methods=['GET', 'POST'])
def sifremiunuttum():
    return render_template("sifremiunuttum.html")
@app.route("/grafik", methods=['GET', 'POST'])
def grafik():
        from grafikyazar import Ceran
        (sicaklik,gerilim,batarya,hiz) = Ceran().ceran()
        json.dumps(sicaklik)
        json.dumps(gerilim)
        json.dumps(batarya)
        json.dumps(hiz)

        return render_template("grafik.html",sicaklik = sicaklik, gerilim = gerilim,batarya = batarya,hiz = hiz)
@app.route("/log", methods=['GET', 'POST'])
def log():
        from logcekici import Logs
        Loglar = Logs().log()
        return render_template("loglariizle.html",Loglar = Loglar)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def server_error(e):
	return render_template('404.html'), 500


mesg = 'we are here...'

	

@socketio.on('connect', namespace='/carpi')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    if json==None:
            print ("json yok")
    else:
        a = str(json)
        print (a)
    



@app.route("/", methods = ["GET", "POST"])	   # GET,POST Methodlari ile html formlarindan veri cekme kisimi:
def search():										   # arama sayfasi tanimladim
        if request.method == "POST":				   # eger post methoduysa
                if request.form["action"] == "controlpanel":     
                    user = request.form.get("user")   # seed formumdan seedi al
                    passw = request.form.get("pass")	# keyword formumdan keywordu al
                    if user=="TABLE":
                        createtable()
                    data=login(user,passw)
                    status=data["login"]
                    if status==True:
                        print ("Giris basarili")
                        templateData=getbalance(data)
                        return render_template('controlpanel.html', async_mode=socketio.async_mode, **templateData, user = user)
                    else:
                        flash("Kullanıcı Adı veya Şifreniz Hatalı") 
                        return redirect(request.url)
                if request.form["register"] == "register":    
                    return redirect(url_for('register'))


                if request.form["action"] == "navi":           
                        return redirect(url_for('navi'))
     
                if request.form["actions"] == "message":
                        return redirect(url_for('message'))                    
                    
                if request.form["sifermiunuttumm"] == "sifermiunuttum":
                            return redirect(url_for('sifermiunuttum'))
                if request.form["grafikk"] == "grafik":
 
                            return redirect(url_for('grafik'))
                if request.form["logg"] == "log":
     
                            return redirect(url_for('loglariizle'))
                if request.form["exitt"] == "cikis_yap":
                            return redirect(url_for('index'))

					# eski sekmede diger sonuclari listelettim
                


        else:
                return redirect(url_for("index"))
if __name__ == '__main__':
    HOST = environ.get('0.0.0.0', 'localhost')
    try:
        PORT = int(environ.get('80', '5000'))
    except ValueError:
        PORT = 80
    #Sinif().sinif()
    app.run(HOST, PORT)
    #socketio.run(app, debug=True)


##################################################################################################################
