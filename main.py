
from flask import Flask, render_template, request
import random

l=["0","1","2","3","4","5","6","7","8","9"]
three=[]
turn=1
res="Player 1 is X"
res1="Player 2 is O"
res2="Player 1 has first turn."
g=""
ss=""
s1,s2=0,0
kk,jj=1,1
one=[]
chip,bet=100,0
rb=""
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
deck=[]


app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home():
    global l
    global turn
    global res
    global g
    global res1
    global res2
    global chip,bet
    chip,bet=100,0
    res="Player 1 is X"
    res1="Player 2 is O"
    res2="Player 1 has first turn."
    g=""
    l=["0","1","2","3","4","5","6","7","8","9"]
    turn=1

   
   
    return render_template('index.html')
@app.route("/tictak",methods=['GET','POST'])
def game1():
   
   
    return render_template('ticabout.html')
@app.route("/sps",methods=['GET','POST'])
def game2():
   
   
    return render_template('stoneabout.html')
@app.route("/blackjack",methods=['GET','POST'])
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
    global chip,bet,one,three
    global ss,s1,s2,kk,jj
    global rb
    s1,s2,bet,ppp=0,0,0,0
    for i in ranks:
        for j in suits:
            deck.append(i+" of "+j)
    random.shuffle(deck)
    ss,rb,ph="","","Choice"
    s1,s2=0,0
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
            bet=n
            
            one.append(deck.pop())
            ll=list(one[0].split(" "))
            s1+=values[ll[0]]
            one.append(deck.pop())
            ll=list(one[1].split(" "))
            s1+=values[ll[0]]
            three.append(deck.pop())
            ll=list(three[0].split(" "))
            s2+=values[ll[0]]
            three.append(deck.pop())
            ll=list(three[1].split(" "))
            s2+=values[ll[0]]
            
            kk=len(one)
            jj=len(three)
            return render_template('bp.html',ph=ph,rb=rb,one=one,two="<hidden>",three=three,j=jj,k=kk,s1=s1,s2=s2)
    return render_template('black.html',chip=chip,ss=ss)
@app.route("/bp",methods=['GET','POST'])
def play4():
    global chip,bet,one,two,three
    global ss,rb,s1,s2,kk,jj
    ph="Choice"
    n=""

    if rb=="":
        if request.method=='POST':
            n=request.form.get('uname')
            if n=="s" or n=="S":
                while s1 < 17:
                    pp=deck.pop()
                    one.append(pp)
                    ll=list(pp.split(" "))
                    if ll[0]=="Ace":
                        if s1+values[ll[0]]>21:
                            s1+=1
                    else:
                        
                        s1+=values[ll[0]]
                    
                
                    kk=len(one)
            elif n=="h" or n=="H":
               
                ppp=deck.pop()
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
                     chip=chip-bet
            else:
                ph="Wrong_Choice"
                return render_template('bp.html',ph=ph,rb=rb,one=one,two="<hidden>",three=three,j=jj,k=kk,s1=s1,s2=s2)
    if s2<=21 and n!="h":
        if s1>21:
            chip=chip+bet
            rb="Dealer Busts.. Player Wins!"
        elif s1>s2:
            chip=chip-bet
            rb="Dealer Win!"
        elif s2>s1:
            rb="Player Win!"
            chip=chip+bet
        else:
            rb="Draw"
       
    
    return render_template('bp.html',ph=ph,rb=rb,one=one,two="<hidden>",three=three,j=jj,k=kk,s1=s1,s2=s2)


