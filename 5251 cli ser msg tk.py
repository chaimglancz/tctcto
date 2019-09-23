import json
from urllib import request
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from tkinter import *
def submit():#
    cc=htt('http://127.0.0.1:8000/'+en.get())
def view():
    cc=htt('http://127.0.0.1:8000/')
    la.configure(text=cc[63:])
def htt(url):
    aa=request.urlopen(url)
    bb= json.loads(aa.read())
    return bb
def ser():
    class Aa(BaseHTTPRequestHandler):
        def do_GET(self):
            global message
            ff='to view leve empty, to change type /something. the message is  '
            self.send_response(200)
            self.send_header('Content-Type','text/plain')
            self.end_headers()
            self.wfile.write(json.dumps(ff+str(message)).encode())
            gg=self.path[1:]
            if gg=='' or gg=='favicon.ico':
                message=message
            else:
                message=gg
    ee=HTTPServer(('127.0.0.1',8000),Aa)
    print('server is ready ');
    ee.serve_forever()
message=''
dd = Thread(target=ser)
dd.start() 
    
tk=Tk()
tk.geometry('550x500')
en=Entry(tk)
en.place(width=400,height=150,x=0,y=50)
en.configure(bg='#ffffa0')
la=Label(tk)
la.place(width=400,height=150,x=0,y=300)
la.configure(bg='#ffa0a0')
button1 = Button(tk)
button1.place(width=100,height=150,x=450,y=50)
button1.config(bg='#a0ffff',text='submit',command=submit)
button2 = Button(tk)
button2.place(width=100,height=150,x=450,y=300)
button2.config(bg='#c0ffa0',text='view',command=view)


print('client is ready ')



tk.mainloop()
