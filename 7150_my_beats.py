from tkinter import *

speed = 120
sm = 4
xx = 0
only_one = True
def move ():
    global xx
    clr = '#00ff00'
    if xx == 1200:
        xx = 0
        clr = '#ff0000'
    cc.delete('ee')
    
    
    cc.create_oval(xx,0,xx+1200/sm,300,fill=clr, outline='',tag='ee')
    xx += 1200/sm
    cc.after(int(60000/speed),lambda:move ())
        
def conf():
    global speed, sm, xx
    speed = int(speed_entry.get())
    sm = int(sm_entry.get())
    xx = 0
   
tk = Tk()
tk.geometry('1200x500')

cc = Canvas(tk)
cc.place(width=1200,height=300,x=0,y=0)
cc.configure(bg='#000000')

speed_frame = Label(tk)
speed_frame.place(width=100,height=50,x=100,y=400)
speed_frame.configure(bg='pink',text = 'speed')

speed_entry = Entry(tk)
speed_entry.place(width=100,height=50,x=250,y=400)
speed_entry.configure(bg='pink',justify=CENTER)
speed_entry.insert(0,speed)

sm_frame = Label(tk)
sm_frame.place(width=100,height=50,x=500,y=400)
sm_frame.configure(bg='pink',text = '3 or 4')

sm_entry = Entry(tk)
sm_entry.place(width=100,height=50,x=650,y=400)
sm_entry.configure(bg='pink',justify=CENTER)
sm_entry.insert(0,sm)

btn = Button(tk)
btn.place(width=100,height=50,x=900,y=400)
btn.configure(bg='pink',text = 'apply',command = conf)

move()

tk.mainloop()
