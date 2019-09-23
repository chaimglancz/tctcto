import json
from urllib import request
from tkinter import *

def click(i,j):   
    htt('/fill/'+str(gmnum)+'/'+str(i+1)+'/'+str(j+1))
   
def up():
    global gmnum
    if gmnum > 1 :
        gmnum-=1
        htt('/play/'+str(gmnum))
        
def down():   
    global gmnum
    gmnum+=1
    htt('/play/'+str(gmnum))
    
def get_info():
    htt('/play/'+str(gmnum))
    tk.after(2000, lambda: get_info())
        
def disply(info):
    global num1
    num1.configure(text='game number '+str(gmnum))
    trn1.configure(text='')
    won.configure(text='')
    trn1.configure(text=info['message'])
    if info['message']!='please enter two name\'s':
        nm11.delete(0,END)
        nm11.insert(0,'')
        nm21.delete(0,END)
        nm21.insert(0,'')
    for i in range(3):
        for j in range(3):
            btn[i][j].configure(text=info['xo'][i][j],font=('Arial','80'))
    nm11.insert(0,info['name_1'])
    nm21.insert(0,info['name_2'])    
    if 'won'in info:
        won.configure(text=info['won'])
   
def start():
    htt('/names/'+str(gmnum)+'/'+nm11.get()+'/'+nm21.get())
    
def ttt(i,j):
    btn[i].append (Button(tk))
    btn[i][j].place(width=182,height=182,x=j*209,y=i*209)
    btn[i][j].configure(bg='#ffdfff')
    btn[i][j].bind('<Button-1>', lambda event: click(i,j))
    
def htt(url):
    try:
        rspns=request.urlopen('http://'+ip1.get()+url)
        data=json.loads(rspns.read())
        rspns.close()
        disply(data)
    except:    
        trn1.configure(text='please put a volid url')
        
gmnum=1
tk=Tk()
tk.geometry('800x600')
tk.configure(bg = '#000000')
cc=Canvas(tk,bg = '#ffffff')
cc.place(width=200,height=600,x=600,y=0)
ip0=Label(cc)
ip0.place(width=200,height=50,x=0,y=0)
ip0.configure(bg='#c0a080',text='enter ip address and\nport number of server',font=('Arial','10'))
ip1=Entry(cc)
ip1.place(width=200,height=50,x=0,y=50)
ip1.configure(bg='#c0a080',font=('Arial','13'),justify=CENTER)
num0=Label(cc)
num0.place(width=200,height=50,x=0,y=100)
num0.configure(bg='#ffa0ff',text='current game\nuse button\'s to go to other game',font=('Arial','10'))
num1=Label(cc)
num1.place(width=115,height=50,x=0,y=150)
num1.configure(bg='#ffa0ff',text='game number '+str(gmnum),font=('Arial','10'))
num10=Button(cc)
num10.place(width=85,height=25,x=115,y=150)
num10.configure(bg='#ffa0ff',text='previous game',command=up)
num11=Button(cc)
num11.place(width=85,height=25,x=115,y=175)
num11.configure(bg='#ffa0ff',text='next game',command=down)
nm10=Label(cc)
nm10.place(width=200,height=50,x=0,y=200)
nm10.configure(bg='#ffa0a0',text='enter name for first player',font=('Arial','10'))
nm11=Entry(cc)
nm11.place(width=150,height=50,x=50,y=250)
nm11.configure(bg='#ffa0a0',font=('Arial','13'),justify=CENTER)
nm12=Label(cc)
nm12.place(width=50,height=50,x=0,y=250)
nm12.configure(bg='#ffa0a0',text='X = ',font=('Arial','13'))
nm20=Label(cc)
nm20.place(width=200,height=50,x=0,y=300)
nm20.configure(bg='#a0ffa0',text='enter name for second player',font=('Arial','10'))
nm21=Entry(cc)
nm21.place(width=150,height=50,x=50,y=350)
nm21.configure(bg='#a0ffa0',font=('Arial','13'),justify=CENTER)
nm22=Label(cc)
nm22.place(width=50,height=50,x=0,y=350)
nm22.configure(bg='#a0ffa0',text='O = ',font=('Arial','13'))
strt=Button(cc)
strt.place(width=200,height=50,x=0,y=400)
strt.configure(bg='#a0ffff',text='press to start the game',font=('Arial','10'),command=start)
trn1=Label(cc)
trn1.place(width=200,height=50,x=0,y=450)
trn1.configure(bg='#a0a0ff',font=('Arial','13'))
won=Label(cc)
won.place(width=200,height=50,x=0,y=500)
won.configure(bg='#ffffa0',font=('Arial','20'))
btn=[]
for i in range(3):
    btn.append([])
    for j in range(3):
       ttt(i,j)
      
print('client is ready ')
get_info()
tk.mainloop()
