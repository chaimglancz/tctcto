from tkinter import *

def wn(s):
    if dic[str(dicnum)]['xo'][int(s[0])][int(s[1])]==dic[str(dicnum)]['xo'][int(s[2])][int(s[3])]==dic[str(dicnum)]['xo'][int(s[4])][int(s[5])]=='O':
        return True
    elif dic[str(dicnum)]['xo'][int(s[0])][int(s[1])]==dic[str(dicnum)]['xo'][int(s[2])][int(s[3])]==dic[str(dicnum)]['xo'][int(s[4])][int(s[5])]=='X':
        return True
    
def win():
    trn=[nm11,nm21]
    if wn('000102')or wn('101112')or wn('202122')or wn('001020')or wn('011121')or wn('021222')or wn('001122')or wn('021120'):
        won.configure(text=trn[dic[str(dicnum)]['cnt']%2].get()[2:]+' won')
        dic[str(dicnum)]['cnt']+=6
        trn1.configure(text='game finish\'d' )
   
def click(i,j):
    if dic[str(dicnum)]['cnt'] < 9 :
        if dic[str(dicnum)]['xo'][i][j]=='':
            trn=[nm11,nm21]
            lst=['X','O']
            dic[str(dicnum)]['xo'][i][j]=lst[dic[str(dicnum)]['cnt']%2]
            win()
            if dic[str(dicnum)]['cnt'] < 9:
                dic[str(dicnum)]['cnt']+=1
    for i in range(3):
        for j in range(3):
            btn[i][j].configure(text=dic[str(dicnum)]['xo'][i][j],font=('Arial','80'))
          
def up():
    global dicnum
    if dicnum > 1:
        dic[str(dicnum)]['n1']=nm11.get()[2:]
        dic[str(dicnum)]['n2']=nm21.get()[2:]
        dicnum-=1
        num1.configure(text='game number '+str(dicnum))
        trn1.configure(text='')
        won.configure(text='')
        for i in range(3):
            for j in range(3):
                btn[i][j].configure(text=dic[str(dicnum)]['xo'][i][j],font=('Arial','80'))
        nm=dic[str(dicnum)]['n1']
        nm11.delete(0,END)
        nm11.insert(0,'X='+nm)
        nm=dic[str(dicnum)]['n2']
        nm21.delete(0,END)
        nm21.insert(0,'O='+nm)        
    view()
    win()
    
def down():
    global dicnum
    dic[str(dicnum)]['n1']=nm11.get()[2:]
    dic[str(dicnum)]['n2']=nm21.get()[2:]
    dicnum+=1
    num1.configure(text='game number '+str(dicnum))
    trn1.configure(text='')
    won.configure(text='')
    try:
        for i in range(3):
            for j in range(3):
                btn[i][j].configure(text=dic[str(dicnum)]['xo'][i][j],font=('Arial','80'))
        nm=dic[str(dicnum)]['n1']
        nm11.delete(0,END)
        nm11.insert(0,'X='+nm)
        nm=dic[str(dicnum)]['n2']
        nm21.delete(0,END)
        nm21.insert(0,'O='+nm)
        view() 
        win()
    except:
        dic[str(dicnum)]={}
        dic[str(dicnum)]['xo']=[[''for i in range(3)]for j in range(3)]
        dic[str(dicnum)]['cnt']=0
        for i in range(3):
            for j in range(3):
                btn[i][j].configure(text=dic[str(dicnum)]['xo'][i][j],font=('Arial','80'))
        nm11.delete(0,END)
        nm11.insert(0,'')
        nm21.delete(0,END)
        nm21.insert(0,'')  
   
def ent1():
    nm=nm11.get()
    nm11.delete(0,END)
    nm11.insert(0,'X='+nm)
    
def ent2():
    nm=nm21.get()
    nm21.delete(0,END)
    nm21.insert(0,'O='+nm)
    
def view():
    trn=[nm11,nm21]
    if dic[str(dicnum)]['cnt'] < 9:
        trn1.configure(text='now is '+trn[dic[str(dicnum)]['cnt']%2].get()[2:]+'\'s turn' )
    else:
        trn1.configure(text='game finish\'d' )
        
def ttt(i,j):
    btn[i].append (Button(tk))
    btn[i][j].place(width=182,height=182,x=j*209,y=i*209)
    btn[i][j].configure(bg='#ffdfff')
    btn[i][j].bind('<Button-1>', lambda event: click(i,j))
    
dic={}
dicnum=1
dic[str(dicnum)]={}
dic[str(dicnum)]['cnt']=0
tk=Tk()
tk.geometry('800x600')
tk.configure(bg = '#000000')
cc=Canvas(tk,bg = '#ffffff')
cc.place(width=200,height=600,x=600,y=0)
num0=Label(cc)
num0.place(width=200,height=50,x=0,y=0)
num0.configure(bg='#ff00ff',text='current game\nuse button\'s to go to other game',font=('Arial','10'))
num1=Label(cc)
num1.place(width=150,height=50,x=0,y=50)
num1.configure(bg='#ff00ff',text='game number '+str(dicnum),font=('Arial','13'))
num10=Button(cc)
num10.place(width=50,height=25,x=150,y=50)
num10.configure(bg='#ff00ff',text='up',command=up)
num11=Button(cc)
num11.place(width=50,height=25,x=150,y=75)
num11.configure(bg='#ff00ff',text='down',command=down)
nm10=Label(cc)
nm10.place(width=200,height=50,x=0,y=100)
nm10.configure(bg='#ffa0a0',text='enter name for first player\nwith x  and press enter',font=('Arial','10'))
nm11=Entry(cc)
nm11.place(width=150,height=50,x=0,y=150)
nm11.configure(bg='#ffa0a0',font=('Arial','13'))
nm12=Button(cc)
nm12.place(width=50,height=50,x=150,y=150)
nm12.configure(bg='#ffa0a0',text='enter',command=ent1)
nm20=Label(cc)
nm20.place(width=200,height=50,x=0,y=200)
nm20.configure(bg='#a0ffa0',text='enter name for second player\nwith o  and press enter',font=('Arial','10'))
nm21=Entry(cc)
nm21.place(width=150,height=50,x=0,y=250)
nm21.configure(bg='#a0ffa0',font=('Arial','13'))
nm22=Button(cc)
nm22.place(width=50,height=50,x=150,y=250)
nm22.configure(bg='#a0ffa0',text='enter',command=ent2)
trn0=Label(cc)
trn0.place(width=200,height=50,x=0,y=300)
trn0.configure(bg='#a0a0ff',text='to see whese turn it is\npress view',font=('Arial','10'))
trn1=Label(cc)
trn1.place(width=150,height=50,x=0,y=350)
trn1.configure(bg='#a0a0ff',font=('Arial','13'))
trn2=Button(cc)
trn2.place(width=50,height=50,x=150,y=350)
trn2.configure(bg='#a0a0ff',text='view',command=view)
won=Label(cc)
won.place(width=200,height=50,x=0,y=400)
won.configure(bg='#ffffa0',font=('Arial','10'))
btn=[]
for i in range(3):
    btn.append([])
    for j in range(3):
       ttt(i,j)
dic[str(dicnum)]['xo']=[[''for i in range(3)]for j in range(3)]           

tk.mainloop()
