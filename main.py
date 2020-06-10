# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:04:55 2020

@author: HP
"""

from flask import Flask, render_template, request,session,redirect
import random

l=["0","1","2","3","4","5","6","7","8","9"]
turn=1
res="Player 1 is X"
res1="Player 2 is O"
res2="Player 1 has first turn."
g=""
app = Flask(__name__)


@app.route("/")
def home():
    global l
    global turn
    global res
    global g
    global res1
    global res2
    res="Player 1 is X"
    res1="Player 2 is O"
    res2="Player 1 has first turn."
    g=""
    l=["0","1","2","3","4","5","6","7","8","9"]
    turn=1

   
   
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
    
    global turn
    global l
    global res
    global g
    global res1
    global res2
    m="Choice"
    c=0
   
    if res=="Player 1 is X":
        if request.method=='POST':
            n=int(request.form.get('uname'))
            if n>0 and n<10:
                if turn==1 and l[n]!="O":
                    l[n]="X"
                    turn=2
                elif turn==2 and l[n]!="X":
                    l[n]="O"
                    turn=1
            else:
                m="Wrong_Choice"
    else:
        g="GO TO HOME TO PLAY AGAIN!!"
    for i in l:
        if i=="X" or i=="O":
            c+=1
    if c>=9:
        res="DRAW!!!"
        res1=""
        res2=""
    elif (l[1]=="X" and l[2]=="X" and l[3]=="X") or (l[4]=="X" and l[5]=="X" and l[6]=="X")or(l[7]=="X" and l[8]=="X" and l[9]=="X"):
        res="Player 1 is Winner!!!"
        res1=""
        res2=""
    elif (l[1]=="O" and l[2]=="O" and l[3]=="O") or (l[4]=="O" and l[5]=="O" and l[6]=="O")or(l[7]=="O" and l[8]=="O" and l[9]=="O"):
        res="Player 2 is Winner!!!"
        res1=""
        res2=""
    elif (l[1]=="X" and l[4]=="X" and l[7]=="X") or (l[2]=="X" and l[5]=="X" and l[8]=="X")or(l[3]=="X" and l[6]=="X" and l[9]=="X"):
        res="Player 1 is Winner!!!"
        res1=""
        res2=""
    elif (l[1]=="O" and l[4]=="O" and l[7]=="O") or (l[2]=="O" and l[5]=="O" and l[8]=="O")or(l[3]=="O" and l[6]=="O" and l[9]=="O"):
        res="Player 2 is Winner!!!"
        res1=""
        res2=""
    elif (l[1]=="O" and l[5]=="O" and l[9]=="O") or (l[3]=="O" and l[5]=="O" and l[7]=="O"):
        res="Player 2 is Winner!!!"
        res1=""
        res2=""
    elif (l[1]=="X" and l[5]=="X" and l[9]=="X") or (l[3]=="X" and l[5]=="X" and l[7]=="X"):
        res="Player 1 is Winner!!!"
        res1=""
        res2=""
    
        
    return render_template('tictak.html',l=l,m=m,res=res,g=g,res1=res1,res2=res2)
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

