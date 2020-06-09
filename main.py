# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:04:55 2020

@author: HP
"""

from flask import Flask, render_template, request,session,redirect
import random



app = Flask(__name__)


@app.route("/")
def home():
   
   
    return render_template('index.html')
@app.route("/tictak")
def game1():
   
   
    return render_template('ticabout.html')
@app.route("/sps")
def game2():
   
   
    return render_template('stoneabout.html')
@app.route("/blackjack")
def game3():
   
   
    return render_template('blackabout.html')
@app.route("/ttp",methods=['GET','POST'])
def play1():
    return render_template('tictak.html')
@app.route("/spsp",methods=['GET','POST'])
def play2():
    user=""
    o=""
    m=1
    s=""
    res=""
    r=""
    l=["","Stone","Paper","Sicssor"]
    
    
    if request.method=='POST':
        n=int(request.form.get('uname'))
        if n>3 or n<1:
            s="Wrong Choice"
        else:
            s=l[n]
        m=random.randint(1,3)
        if m==n:
            r="DRAW!!"
        elif n==1 and m==3:
            r="You Win!! Congratulations"
        elif n==2 and m==1:
            r="You Win!! Congratulations"
        elif n==3 and m==2:
            r="You Win!!  Congratulations"
        else:
            r="Computer Win!! Better luck next time"
    return render_template('sps.html',user=l[m],o=s,res=r)
@app.route("/bjp",methods=['GET','POST'])
def play3():
    return render_template('black.html')
app.run(debug="True")

