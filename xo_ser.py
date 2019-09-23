import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from tkinter import *

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
srv=HTTPServer(('0.0.0.0',8000),Ser)
print('server is ready ');
srv.serve_forever()
            
