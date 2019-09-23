import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from tkinter import *

def ser():
    class Ser(BaseHTTPRequestHandler):
        def do_GET(self):

            path_lst=self.path[1:].split('/')
               
            if path_lst[0]=='fill':
                answer=fill(path_lst[1],int(path_lst[2]),int(path_lst[3]))
            elif path_lst[0]=='names':
                answer= put_names(path_lst[1],path_lst[2],path_lst[3])
            elif path_lst[0]=='play':
                answer=view(path_lst[1])
            else:
                answer='/play/game=1-----/start/game=1/fir_nam=chaim/sec_nam=yosef-----/fill/game=1/line=1/thing=3<br/>',dic
                
            self.send_response(200)
            self.send_header('Content-Type','text/html')
            self.end_headers()
            self.wfile.write(json.dumps(answer).encode())
            
    srv=HTTPServer(('0.0.0.0',8000),Ser)
    print('server is ready ');
    srv.serve_forever()
    
def fill(n,i,j):
    if dic[n]['name_1']!=''and dic[n]['name_2']!='':
        if dic[n]['cnt'] < 9 :
            if dic[n]['xo'][i-1][j-1]=='':
                lst=['X','O']
                dic[n]['xo'][i-1][j-1]=lst[dic[n]['cnt']%2]
                win(n)
                if dic[n]['cnt'] < 8:
                    dic[n]['cnt']+=1
                    dic[n]['message']='now is '+dic[n]['name_'+str(dic[n]['cnt']%2+1)]+'\'s turn'       
                else:
                    dic[n]['message']='game finish\'d'
    return dic[n]

def view(n):
    if n not in dic:
        dic[n]={}
        dic[n]['xo']=[[''for i in range(3)]for j in range(3)]
        dic[n]['cnt']=0
        dic[n]['name_1']=''
        dic[n]['name_2']=''
        dic[n]['message']='please enter two name\'s'
        return dic[n]
    else:
        return dic[n]
    
def put_names(n,n1,n2):
    if dic[n]['cnt'] == 0:
        dic[n]['name_1']=n1
        dic[n]['name_2']=n2
        if n1==''or n2=='':
            dic[n]['message']='please enter two name\'s'
        else:
            dic[n]['message']='now is '+n1+'\'s turn'
    return dic[n]
  
def wn(n,s):
    if dic[n]['xo'][int(s[0])][int(s[1])]==dic[n]['xo'][int(s[2])][int(s[3])]==dic[n]['xo'][int(s[4])][int(s[5])]=='O':
        return True
    elif dic[n]['xo'][int(s[0])][int(s[1])]==dic[n]['xo'][int(s[2])][int(s[3])]==dic[n]['xo'][int(s[4])][int(s[5])]=='X':
        return True
    
def win(n):
    if wn(n,'000102')or wn(n,'101112')or wn(n,'202122')or wn(n,'001020')or wn(n,'011121')or wn(n,'021222')or wn(n,'001122')or wn(n,'021120'):
        dic[n]['won']=dic[n]['name_'+str(dic[n]['cnt']%2+1)]+' won'
        dic[n]['cnt']+=6
        dic[n]['message']='game finish\'d'
        
dic={}
trd = Thread(target=ser)
trd.start()






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
