from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
import math
window=Tk()
window.geometry("600x550+350+150")
window.resizable(FALSE,FALSE)
window.title("AdvCalc")
#style = Style(theme="solar")
#style = Style(theme="cyborg")
#style = Style(theme="superhero")
#style = Style(theme="darkly")
style=Style(theme="lumen")
style.configure('custom.TButton', background='yellow')
window = style.master

titleimage=PhotoImage(file="photo/titlesym.png")
window.iconphoto(False,titleimage)
tabs=ttk.Notebook(window,width=500,height=500)
tabs.pack(fill=BOTH,expand=TRUE)
tab1=Frame(tabs)
tab2=Frame(tabs)
tabs.add(tab1,text="Simple Calculator")
tabs.add(tab2,text="Advanced Calculator")

####################simple calculator#############
#####################ENTRY#################
entry=Entry(window,font=("verdana 14 bold"),width=28,bd=10,justify=RIGHT)
entry.insert(0,'O')
entry.place(x=90,y=60)
entry.config(state="normal")
entry1=Entry(tab2,font=("verdana 14 bold"),width=22,bd=10,justify=RIGHT)
entry1.insert(0,'O')
#entry1.pack(side=BOTTOM)
####################FUNCTIONS
temp=''
indicate=0
def numfun(x):
    global indicate
    global temp
    if x==10:
        indicate = 1
        x="("
        temp=""
    if x == 11:
        x = ")"
        indicate = 1
        temp =""
    if indicate==1:
        if entry.get() == "O":
            entry.delete(0, END)
            entry1.delete(0, END)
            temp = temp + x
            entry.insert(0, x)
            entry1.insert(0,x)

        else:
            entry.insert(END, x)
            entry1.insert(END,x)

    elif indicate != 1:
        if entry.get() == "O":
            entry.delete(0, END)
            entry1.delete(0, END)
            entry.insert(0, x)
            entry1.insert(0, x)

        else:
            entry.insert(END, x)
            entry1.insert(END, x)
    else:
        pass
    if x == 11:
        x = ")"
        indicate = 0
        temp = ''
def opfun(x):
    if entry.get()!="O":
        entry.insert(END,opbut[x]["text"])
        entry1.insert(END,opbut[x]["text"])

def clearfun():
    entry.delete(0,END)
    entry1.delete(0,END)
    entry.insert(0,"O")
    entry1.insert(0,"O")
displaylist=[]
def equalfun():

    content=entry.get()
    content1=entry1.get()
    result=eval(content1)
    result=round(result,2)
    #print(result)
    #print("content1",content1)
    entry.delete(0,END)
    entry.insert(0,result)
    displaylist.append(content)
    displaylist.reverse()
    history.config(text="History : "+"|".join(displaylist[0:5]))

def deletefun():
    length=len(entry.get())
    if length==1:
        entry.delete(0,END)
        entry1.delete(0,END)
        entry.insert(0,"O")
        entry1.insert(0,"O")
    else:
        entry.delete(length-1,END)
        entry1.delete(length-1,END)
    if entry1.get()=="math.":
        entry1.delete(-4,END)

def trigfun(x):
    global y
    if x==0:
        x="sin"
        y="math.sin"
    elif x==1:
        x="cos"
        y = "math.cos"
    elif x==2:
        x="tan"
        y = "math.tan"
    elif x==3:
        x="rad"
        y = "math.radians"
    elif x==4:
        x="log"
        y = "math.log"
    elif x==5:
        x="fact"
        y = "math.factorial"
    elif x==6:
        x="deg"
        y = "math.degrees"
    if entry.get()=="O":
        entry.delete(0,END)
        entry1.delete(0,END)
        entry.insert(0,x)
        entry1.insert(0,y)
    else:
        entry.insert(END,x)
        entry1.insert(END,y)

def invtrigfun(x):
    global y
    if x==0:
        x="sin^-1"
        y="math.asin"
    if x==1:
        x="cos^-1"
        y="math.acos"
    if x==2:
        x="tan^-1"
        y="math.atan"
    if entry.get()=="O":
        entry.delete(0,END)
        entry1.delete(0,END)
        entry.insert(0,x)
        entry1.insert(0,y)
    else:
        entry.insert(END,x)
        entry1.insert(END,y)

def hyptrigfun(x):
    global y
    if x==0:
        x="sinh"
        y="math.sinh"
    if x==1:
        x="cosh"
        y="math.cosh"
    if x==2:
        x="tanh"
        y="math.tanh"
    if entry.get()=="O":
        entry.delete(0,END)
        entry1.delete(0,END)
        entry.insert(0,x)
        entry1.insert(0,y)
    else:
        entry.insert(END,x)
        entry1.insert(END,y)

def invhyptrigfun(x):
    global y
    if x==0:
        x="sinh^-1"
        y="math.asinh"
    if x==1:
        x="cosh^-1"
        y="math.acosh"
    if x==2:
        x="tanh^-1"
        y="math.atanh"
    if entry.get()=="O":
        entry.delete(0,END)
        entry1.delete(0,END)
        entry.insert(0,x)
        entry1.insert(0,y)
    else:
        entry.insert(END,x)
        entry1.insert(END,y)
################NUMBERS##############
numbut=[]
for i in range(0,10):
    numbut.append(ttk.Button(tab1,text=str(i),width=4,style='success.Outline.TButton',command=lambda x=i:numfun(x)))
    style.configure(numbut[i], font=("Times 15 bold"))
for i in range(10,13):
    numbut.append(ttk.Button(tab1,width=4,style='success.Outline.TButton',command=lambda x=i:numfun(x)))
    style.configure(numbut[i], font=("Times 15 bold"),background="blue")
numbut[10]["text"]="("
numbut[11]["text"]=")"


#   PACKING NUMBERS
butnum=1 #button number
for i in range(0,3):
    for j in range(0,4):
        numbut[butnum].place(x=90+j*90,y=120+i*70)
        butnum+=1

###############Operators############
opbut=[]
for i in range(0,5):
    opbut.append(ttk.Button(tab1,style='success.Outline.TButton',width=4,command=lambda x=i:opfun(x)))

opbut[0]["text"]="+"
opbut[1]["text"]="-"
opbut[2]["text"]="*"
opbut[3]["text"]="/"
opbut[4]["text"]="**"


###########Packing Operators#########
for i in range(0,4):
    opbut[i].place(x=450,y=120+i*70)
opbut[4].place(x=360,y=260)

##############Other button########
zerobut=ttk.Button(tab1,text="0",style='success.Outline.TButton',width=4,command=lambda x=0:numfun(x))
zerobut.place(x=90,y=330)
clearbut=ttk.Button(tab1,text="C",style='success.Outline.TButton',width=4,command=clearfun)
clearbut.place(x=90,y=400)
dotbut=ttk.Button(tab1,text=".",style='success.Outline.TButton',width=4,command=lambda x=".":numfun(x))
dotbut.place(x=180,y=400)
equalbut=ttk.Button(tab1,text="=",style='success.Outline.TButton',width=4,command=equalfun)
equalbut.place(x=270,y=400)
deletebut=ttk.Button(tab1,text="<--",width=4,style='success.Outline.TButton',command=deletefun)
deletebut.place(x=360,y=400)
history=Label(tab1,text="History :",font=("verdana 12 bold"),bd=5,anchor=W,relief=SUNKEN)
history.pack(side=BOTTOM,fill=X)
###################Advanced calculator###############
label1=Label(tab2,text="Basic Trigonometric functions",font=("Times 15 bold"))
label1.place(x=100,y=90)
trigbut=[]
for i in range(0,3):
    trigbut.append(ttk.Button(tab2,style='success.Outline.TButton',width=6,command=lambda x=i:trigfun(x)))
trigbut[0]["text"]="sin"
trigbut[1]["text"]="cos"
trigbut[2]["text"]="tan"
trigbut.append(ttk.Button(tab1,style='success.Outline.TButton',width=4,command=lambda x=3:trigfun(x)))
trigbut.append(ttk.Button(tab1,style='success.Outline.TButton',width=4,command=lambda x=4:trigfun(x)))
trigbut.append(ttk.Button(tab1,style='success.Outline.TButton',width=4,command=lambda x=5:trigfun(x)))
trigbut.append(ttk.Button(tab1,style='success.Outline.TButton',width=4,command=lambda x=6:trigfun(x)))
trigbut[3]["text"]="rad"
trigbut[4]["text"]="log"
trigbut[5]["text"]="fact"
trigbut[6]["text"]="deg"

###########Packing Operators#########
trignum=0
for i in range(0,1):
    for j in range(0,3):
        trigbut[trignum].place(x=100+j*90,y=150+i*90)
        trignum+=1
trigbut[3].place(x=450,y=400)
trigbut[4].place(x=270,y=330)
trigbut[5].place(x=360,y=330)
trigbut[6].place(x=180,y=330)
###############Inverse functions#########
label2=Label(tab2,text="Basic Inverse Trigonometric functions",font=("Times 15 bold"))
label2.place(x=100,y=200)
invtrigbut=[]
for i in range(0,3):
    invtrigbut.append(ttk.Button(tab2,style='success.Outline.TButton',width=6,command=lambda x=i:invtrigfun(x)))
invtrigbut[0]["text"]="sin^-1"
invtrigbut[1]["text"]="cos^-1"
invtrigbut[2]["text"]="tan^-1"

##########placing inv trig func
invtrignum=0
for i in range(0,1):
    for j in range(0,3):
        invtrigbut[invtrignum].place(x=100+j*90,y=250+i*90)
        invtrignum+=1
###############Hyperbolic functions#########
label3=Label(tab2,text="Hyperbolic Trigonometric functions",font=("Times 15 bold"))
label3.place(x=100,y=300)
hyptrigbut=[]
for i in range(0,3):
    hyptrigbut.append(ttk.Button(tab2,width=6,style='success.Outline.TButton',command=lambda x=i:hyptrigfun(x)))
hyptrigbut[0]["text"]="sinh"
hyptrigbut[1]["text"]="cosh"
hyptrigbut[2]["text"]="tanh"
##########placing inv trig func
hyptrignum=0
for i in range(0,1):
    for j in range(0,3):
        hyptrigbut[hyptrignum].place(x=100+j*90,y=350+i*90)
        hyptrignum+=1

###############InvHyperbolic functions#########
label4=Label(tab2,text="Inverse Hyperbolic Trigonometric functions",font=("Times 15 bold"))
label4.place(x=100,y=400)
invhyptrigbut=[]
for i in range(0,3):
    invhyptrigbut.append(ttk.Button(tab2,style='success.Outline.TButton',width=6,command=lambda x=i:invhyptrigfun(x)))

invhyptrigbut[0]["text"]="sinh^-1"
invhyptrigbut[1]["text"]="cosh^-1"
invhyptrigbut[2]["text"]="tanh^-1"
##########placing inv hyptrig func
invhyptrignum=0
for i in range(0,1):
    for j in range(0,3):
        invhyptrigbut[invhyptrignum].place(x=100+j*90,y=450+i*90)
        invhyptrignum+=1

window.mainloop()