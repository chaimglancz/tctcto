from tkinter import *
import math
class Brd :
    cnt_x = 300
    cnt_y = 300
    cnt_z = 600
    def btn (self,t,xx,yy,txt):
        self.button = Button(t)
        self.button.place(width=25,height=25,x=xx,y=yy)
        self.button.configure(bg='yellow',text = txt)
        self.button.bind('<Button-1>', lambda event: click(txt))
        
    def frm (self,t,w,h,xx,yy):
        self.frame = Frame(t)
        self.frame.place(width=w,height=h,x=xx,y=yy)
        self.frame.configure(bg='pink')

    def cnvs (self,t):
        self.canves = Canvas(t)
        self.canves.place(width=600,height=600,x=0,y=0)
  
class Pcs():
    def __init__(self,x,y,z,clr):
        self.x = x
        self.y = y
        self.z = z
        self.clr = clr
        
    def icns (self,xx,yy,clr):
        cnvs0.canves.create_rectangle(xx-5,yy-5,xx+5,yy+5,fill=clr, outline='',tag='ee')

def rot():
    global sh, ch, sv, cv, sc, cc
    sh = math.sin(rh)
    ch = math.cos(rh)
    sv = math.sin(rv)
    cv = math.cos(rv)
    sc = math.sin(rc)
    cc = math.cos(rc)
    
def click(txt):
    global rh, rv, rc
    rh = 0
    rv = 0
    rc = 0
    if txt == '>':
        rh = math.pi/12
    if txt == '<':
        rh = -math.pi/12
    if txt == '/\\':
        rv = math.pi/12
    if txt == '\\/':
        rv = -math.pi/12
    if txt == ',->':
        rc = math.pi/12
    if txt == '<-,':
        rc = -math.pi/12
    if txt == 'x+':
        cnvs0.cnt_x += 10
    if txt == 'x-':
        cnvs0.cnt_x -= 10
    if txt == 'y+':
        cnvs0.cnt_y += 10
    if txt == 'y-':
        cnvs0.cnt_y -= 10
    if txt == 'z+':
        cnvs0.cnt_z += 100
    if txt == 'z-':
        if cnvs0.cnt_z > 200:
            cnvs0.cnt_z -= 100
    rot()    
    cnvs0.canves.delete('ee')
    put_on_brd()

def disply(num):
    x = gg[num].x
    y = gg[num].y
    z = gg[num].z
    x, z = x * ch - z * sh, z * ch + x * sh
    x, y = x * cc - y * sc, x * sc + y * cc 
    y, z = z * sv + y * cv, z * cv - y * sv
    gg[num].x = x
    gg[num].y = y
    gg[num].z = z
    dspl_x = cnvs0.cnt_z * x / (cnvs0.cnt_z + z)
    dspl_y = cnvs0.cnt_z * y / (cnvs0.cnt_z + z)
    return [num, dspl_x, dspl_y, int(z), gg[num].clr]

def put_on_brd():
    lst = []
    for i in range(len(gg)):
        xy = disply(i)
        lst.append(xy)
    for j in range(-300,300) :
        for i in range(len(gg)):
            if lst[i][3] == -j:
                gg[lst[i][0]].icns(cnvs0.cnt_x + lst[i][1] ,cnvs0.cnt_y + lst[i][2], lst[i][4])
      
rh = 0
sh = 0
ch = 1
rv = 0
sv = 0
cv = 1
rc = 0
sc = 0
cc = 1
    
tk = Tk()
tk.geometry('600x675')

cnvs0 = Brd()
cnvs0.cnvs(tk)
gg = []
for i in range(-100,100,10):
    for j in range(-100,100,10):
        gg.append(Pcs(i,j,100,'blue'))
for i in range(-100,100,10):
    for j in range(-100,100,10):
        gg.append(Pcs(100,i,j,'orange'))
for i in range(-100,100,10):
    for j in range(-100,100,10):
        gg.append(Pcs(i,-100,j,'purple'))
for i in range(-100,100,10):
    for j in range(-100,100,10):
        gg.append(Pcs(i,100,j,'red'))
for i in range(-100,100,10):
    for j in range(-100,100,10):
        gg.append(Pcs(-100,i,j,'green'))
for i in range(-100,100,10):
    for j in range(-100,100,10):
        gg.append(Pcs(i,j,-100,'yellow'))
        
put_on_brd()

btn_brd1 = Brd()
btn_brd1.frm(tk,125,75,357,600)

button_1 = Brd()
button_1.btn(btn_brd1.frame,50,0,'/\\')

button_2 = Brd()
button_2.btn(btn_brd1.frame,75,25,'>')

button_3 = Brd()
button_3.btn(btn_brd1.frame,25,25,'<')

button_4 = Brd()
button_4.btn(btn_brd1.frame,50,50,'\\/')

button_5 = Brd()
button_5.btn(btn_brd1.frame,100,0,'<-,')

button_6 = Brd()
button_6.btn(btn_brd1.frame,0,0,',->')

btn_brd2 = Brd()
btn_brd2.frm(tk,125,75,117,600)

button_7 = Brd()
button_7.btn(btn_brd2.frame,13,8,'x+')

button_8 = Brd()
button_8.btn(btn_brd2.frame,13,42,'x-')

button_9 = Brd()
button_9.btn(btn_brd2.frame,50,8,'y+')

button_10 = Brd()
button_10.btn(btn_brd2.frame,50,42,'y-')

button_11 = Brd()
button_11.btn(btn_brd2.frame,88,8,'z+')

button_12 = Brd()
button_12.btn(btn_brd2.frame,88,42,'z-')
  
tk.mainloop()
