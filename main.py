# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:04:55 2020

@author: HP
"""

from flask import Flask, render_template, request,session,redirect
import random
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)



@app.route("/")
def home():
    
    client=MongoClient("mongodb+srv://mittalabhyu:Abhyudaya@cluster0-fckkh.mongodb.net/tictak?retryWrites=true&w=majority")
    db=client.get_database('tictak')
    client1=MongoClient("mongodb+srv://mittalabhyu:Abhyudaya@cluster0-fckkh.mongodb.net/blackjack?retryWrites=true&w=majority")
    db1=client1.get_database('blackjack')
    ec1=db1.chip
    kj1=list(ec1.find())
    chip=kj1[0]['0']
    new2={'0':100}
    ec1.update_one({'0':chip},{'$set':new2})
    rec=db.play
    rec1=db.result
    k1=list(rec1.find())
    new1={'0':'Player 1 is X'}
    rec1.update_one({'0':'DRAW!!!'},{'$set':new1})
    rec1.update_one({'0':'Player 2 is Winner!!!'},{'$set':new1})
    rec1.update_one({'0':'Player 1 is Winner!!!'},{'$set':new1})
    k=list(rec.find())
    for i in range(10):
        j=str(i)
        new={j:j}
        rec.update_one({j:'X'},{'$set':new})
        rec.update_one({j:'O'},{'$set':new})
        rec.update_one({'0':'1'},{'$set':new})
    
   
   
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
    l=["0","1","2","3","4","5","6","7","8","9"]
    res="Player 1 is X"
    res1="Player 2 is O"
    res2="Player 1 has first turn."
    client=MongoClient("mongodb+srv://mittalabhyu:Abhyudaya@cluster0-fckkh.mongodb.net/tictak?retryWrites=true&w=majority")
    db=client.get_database('tictak')
    rec=db.play
    rec1=db.result
    k1=list(rec1.find())
    k=list(rec.find())
    res=k1[0]['0']
    if res!="Player 1 is X":
        res1=""
        res2=""
    for i in range(10):
        j=str(i)
        l[i]=k[i][j]
    
    g=""
    m="Choice"
    c=0
   
    if res=="Player 1 is X":
        if request.method=='POST':
            n=int(request.form.get('uname'))
            if n>0 and n<10:
                if l[0]=="0" and l[n]!="O" and l[n]!="X":
                    l[n]="X"
                    qq=str(n)
                    new={qq:'X'}
                    new1={'0':'1'}
                    rec.update_one({qq:qq},{'$set':new})
                    rec.update_one({'0':'0'},{'$set':new1})
                elif l[0]=="1" and l[n]!="X" and l[n]!="O":
                    l[n]="O"
                    qq=str(n)
                    new={qq:'O'}
                    new1={'0':'0'}
                    rec.update_one({qq:qq},{'$set':new})
                    rec.update_one({'0':'1'},{'$set':new1})
                else:
                    m="Already_Filled"
            else:
                m="Wrong_Choice"
    else:
        g="GO TO HOME TO PLAY AGAIN!!"
    for i in l:
        if i=="X" or i=="O":
            c+=1
    
    if (l[1]=="X" and l[2]=="X" and l[3]=="X") or (l[4]=="X" and l[5]=="X" and l[6]=="X")or(l[7]=="X" and l[8]=="X" and l[9]=="X"):
        res="Player 1 is Winner!!!"
        new1={'0':'Player 1 is Winner!!!'}
        res1=""
        res2=""
        rec1.update_one({'0':'Player 1 is X'},{'$set':new1})
    elif (l[1]=="O" and l[2]=="O" and l[3]=="O") or (l[4]=="O" and l[5]=="O" and l[6]=="O")or(l[7]=="O" and l[8]=="O" and l[9]=="O"):
        res="Player 2 is Winner!!!"
        new1={'0':'Player 2 is Winner!!!'}
        res1=""
        res2=""
        rec1.update_one({'0':'Player 1 is X'},{'$set':new1})
    elif (l[1]=="X" and l[4]=="X" and l[7]=="X") or (l[2]=="X" and l[5]=="X" and l[8]=="X")or(l[3]=="X" and l[6]=="X" and l[9]=="X"):
        res="Player 1 is Winner!!!"
        new1={'0':'Player 1 is Winner!!!'}
        res1=""
        res2=""
        rec1.update_one({'0':'Player 1 is X'},{'$set':new1})
    elif (l[1]=="O" and l[4]=="O" and l[7]=="O") or (l[2]=="O" and l[5]=="O" and l[8]=="O")or(l[3]=="O" and l[6]=="O" and l[9]=="O"):
        res="Player 2 is Winner!!!"
        new1={'0':'Player 2 is Winner!!!'}
        res1=""
        res2=""
        rec1.update_one({'0':'Player 1 is X'},{'$set':new1})
    elif (l[1]=="O" and l[5]=="O" and l[9]=="O") or (l[3]=="O" and l[5]=="O" and l[7]=="O"):
        res="Player 2 is Winner!!!"
        new1={'0':'Player 2 is Winner!!!'}
        res1=""
        res2=""
        rec1.update_one({'0':'Player 1 is X'},{'$set':new1})
    elif (l[1]=="X" and l[5]=="X" and l[9]=="X") or (l[3]=="X" and l[5]=="X" and l[7]=="X"):
        res="Player 1 is Winner!!!"
        new1={'0':'Player 1 is Winner!!!'}
        res1=""
        res2=""
        rec1.update_one({'0':'Player 1 is X'},{'$set':new1})
    elif c>=9:
        res="DRAW!!!"
        new1={'0':'DRAW!!!'}
        res1=""
        res2=""
        rec1.update_one({'0':'Player 1 is X'},{'$set':new1})
    
        
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
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

    client1=MongoClient("mongodb+srv://mittalabhyu:Abhyudaya@cluster0-fckkh.mongodb.net/blackjack?retryWrites=true&w=majority")
    db1=client1.get_database('blackjack')
    ec=db1.bet
    ec1=db1.chip
    rc=db1.result
    dc=db1.deck
    sm=db1.sum
    pl=db1.play
    ins=db1.index
    leng=db1.length
    insl=list(ins.find())
    sml=list(sm.find())
    kj1=list(ec1.find())
    kj=list(ec.find())
    leng.delete_many({})
    lengd={'0':2,'1':2}
    leng.insert_one(lengd)
    bet=kj[0]['0']
    betd={'0':0}
    index=insl[0]['0']
    newi={'0':47}
    ins.update_one({'0':index},{'$set':newi})
    ec.update_one({'0':bet},{'$set':betd})
    chip=kj1[0]['0']
    ek={'0':''}
    rc.update_one({'0':'Player Busts...Dealer Wins!!'},{'$set':ek})
    rc.update_one({'0':'Dealer Busts...Player Wins!!'},{'$set':ek})
    rc.update_one({'0':'Player Wins!!'},{'$set':ek})
    rc.update_one({'0':'Dealer Wins!!'},{'$set':ek})
    rc.update_one({'0':'Draw!!'},{'$set':ek})
    s1=sml[0]['0']
    s2=sml[1]['1']
    su1={'0':0}
    su2={'1':0}
    sm.update_one({'0':s1},{'$set':su1})
    sm.update_one({'1':s2},{'$set':su2})
    deck=[]
    for i in ranks:
        for j in suits:
            deck.append(i+" of "+j)
    random.shuffle(deck)
    dc.delete_many({})
    pl.delete_many({})
    pl1={}
    pl2={}
    dd={}
    for i in range(0,len(deck)):
        dds=str(i)
        dd[dds]=deck[i]
    dc.insert_one(dd)
    
    s1,s2,ppp=0,0,0
    
    ss,rb,ph="","","Choice"
    one=""
    two=""
    jj,kk=1,1
    three=[]
    one=[]
    if request.method=='POST':
        n=int(request.form.get('uname'))
        if n>chip:
            ss="Enter Valid number"
            return render_template('black.html',ss=ss,chip=chip)
        else:
            new1={'0':n}
            ec.update_one({'0':0},{'$set':new1})
            one.append(deck.pop())
            pl1['0']=one[0]
            ll=list(one[0].split(" "))
            s1+=values[ll[0]]
            one.append(deck.pop())
            pl1['1']=one[1]
            ll=list(one[1].split(" "))
            s1+=values[ll[0]]
            three.append(deck.pop())
            pl2['0']=three[0]
            ll=list(three[0].split(" "))
            s2+=values[ll[0]]
            three.append(deck.pop())
            pl2['1']=three[1]
            ll=list(three[1].split(" "))
            s2+=values[ll[0]]
            sums={'0':s1}
            sumd={'1':s2}
            sm.update_one({'0':0},{'$set':sums})
            sm.update_one({'1':0},{'$set':sumd})
            kk=len(one)
            jj=len(three)
            pl.insert_one(pl1)
            pl.insert_one(pl2)
            
            
            return render_template('bp.html',ph=ph,rb=rb,one=one,two="<hidden>",three=three,j=jj,k=kk,s1=s1,s2=s2)
    return render_template('black.html',chip=chip,ss=ss)
@app.route("/bp",methods=['GET','POST'])
def play4():
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

    client1=MongoClient("mongodb+srv://mittalabhyu:Abhyudaya@cluster0-fckkh.mongodb.net/blackjack?retryWrites=true&w=majority")
    db1=client1.get_database('blackjack')
    ec=db1.bet
    ec1=db1.chip
    rc=db1.result
    sm=db1.sum
    dc=db1.deck
    ins=db1.index
    leng=db1.length
    pl=db1.play
    lengl=list(leng.find())
    pll=list(pl.find())
    sml=list(sm.find())
    lc=list(rc.find())
    kj=list(ec.find())
    kj1=list(ec1.find())
    dcl=list(dc.find())
    bet=kj[0]['0']
    chip=kj1[0]['0']
    rb=lc[0]['0']
    s1=sml[0]['0']
    s2=sml[1]['1']
    ss1=s1
    ss2=s2
    ek={'0':'Player Busts...Dealer Wins!!'}
    do={'0':'Dealer Busts...Player Wins!!'}
    teen={'0':'Player Wins!!'}
    chaar={'0':'Dealer Wins!!'}
    panch={'0':'Draw!!'}
    ph="Choice"
    n=""
    one=[]
    three=[]
    kk=lengl[0]['0']
    jj=lengl[0]['1']
    kk11=kk
    jj11=jj
    for tt in range(0,kk):
        tts=str(tt)
        ones=pll[0][tts]
        one.append(ones)
    for qq in range(0,jj):
        qqs=str(qq)
        twos=pll[1][qqs]
        three.append(twos)

    if rb=="":
        if request.method=='POST':
            n=request.form.get('uname')
            if n=="s" or n=="S":
                while s1 < 17:
                    insl=list(ins.find())
                    index=insl[0]['0']
                    instr=str(index)
                    newi={'0':index-1}
                    pp=dcl[0][instr]
                    ins.update_one({'0':index},{'$set':newi})
                    one.append(pp)
                    ll=list(pp.split(" "))
                    if ll[0]=="Ace":
                        if s1+values[ll[0]]>21:
                            s1+=1
                    else:
                        
                        s1+=values[ll[0]]
                    
                
                    kk=len(one)
            elif n=="h" or n=="H":
                insl=list(ins.find())
                index=insl[0]['0']
                instr=str(index)
                newi={'0':index-1}
                ppp=dcl[0][instr]
                ins.update_one({'0':index},{'$set':newi})
                three.append(ppp)
                ll=list(ppp.split(" "))
                if ll[0]=="Ace":
                    if s2+values[ll[0]]>21:
                        s2+=1
                else:
                    
                    s2+=values[ll[0]]
                
                jj=len(three)
                if s2 > 21:
                     rb="Player Busts..Dealer Wins!"
                     rc.update_one({'0':''},{'$set':ek})
                     chip1=chip-bet
                     new1={'0':chip1}
                     new={'0':0}
                     ec.update_one({'0':bet},{'$set':new})
                     ec1.update_one({'0':chip},{'$set':new1})
            
            else:
                ph="Wrong_Choice"
                return render_template('bp.html',ph=ph,rb=rb,one=one,two="<hidden>",three=three,j=jj,k=kk,s1=s1,s2=s2)
            pl.delete_many({})
            pl1={}
            pl2={}
            for i in range(0,kk):
                kkstr=str(i)
                pl1[kkstr]=one[i]
            for i in range(0,jj):
                jjstr=str(i)
                pl2[jjstr]=three[i]
            pl.insert_one(pl1)
            pl.insert_one(pl2)
            newk={'0':kk}
            newj={'1':jj}
            leng.update_one({'0':kk11},{'$set':newk})
            leng.update_one({'1':jj11},{'$set':newj})
            
    sums={'0':s1}
    sumd={'1':s2}
    sm.update_one({'0':ss1},{'$set':sums})
    sm.update_one({'1':ss2},{'$set':sumd})
    if s2<=21 and n!="h":
        if s1>21:
            chip1=chip+bet
            rb="Dealer Busts.. Player Wins!"
            rc.update_one({'0':''},{'$set':do})
            new1={'0':chip1}
            new={'0':0}
            ec.update_one({'0':bet},{'$set':new})
            ec1.update_one({'0':chip},{'$set':new1})
        elif s1>s2:
            chip1=chip-bet
            rb="Dealer Win!"
            rc.update_one({'0':''},{'$set':chaar})
            new1={'0':chip1}
            new={'0':0}
            ec.update_one({'0':bet},{'$set':new})
            ec1.update_one({'0':chip},{'$set':new1})
        elif s2>s1:
            rb="Player Win!"
            chip1=chip+bet
            new1={'0':chip1}
            new={'0':0}
            rc.update_one({'0':''},{'$set':teen})
            ec.update_one({'0':bet},{'$set':new})
            ec1.update_one({'0':chip},{'$set':new1})
        else:
            rb="Draw"
            new={'0':0}
            rc.update_one({'0':''},{'$set':panch})
            ec.update_one({'0':bet},{'$set':new})
    
       
    
    return render_template('bp.html',ph=ph,rb=rb,one=one,two="<hidden>",three=three,j=jj,k=kk,s1=s1,s2=s2)



