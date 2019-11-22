from tkinter import *

speed = 120
sm = 4
xx = 1
def dlt():
    cc.delete('ee')
    cc.after(int(30000/speed),lambda:move())
def move ():
    global xx
    clr = '#808080'
    if xx >= 1:
        xx = 0
        clr = '#00ff00'
    cc.create_oval(xx,0,600,600,fill=clr, outline='',tag='ee')
    xx += 1/sm
    cc.after(int(30000/speed),lambda:dlt())
        
def conf():
    global speed, sm, xx
    speed = int(speed_entry.get())
    sm = int(sm_entry.get())
    xx = 1
   
tk = Tk()
tk.geometry('950x600')

cc = Canvas(tk)
cc.place(width=600,height=600,x=0,y=0)
cc.configure(bg='#000000')

speed_frame = Label(tk)
speed_frame.place(width=100,height=50,x=650,y=50)
speed_frame.configure(bg='pink',text = 'speed')

speed_entry = Entry(tk)
speed_entry.place(width=100,height=50,x=800,y=50)
speed_entry.configure(bg='pink',justify=CENTER)
speed_entry.insert(0,speed)

sm_frame = Label(tk)
sm_frame.place(width=100,height=50,x=650,y=150)
sm_frame.configure(bg='pink',text = '3 or 4')

sm_entry = Entry(tk)
sm_entry.place(width=100,height=50,x=800,y=150)
sm_entry.configure(bg='pink',justify=CENTER)
sm_entry.insert(0,sm)

btn = Button(tk)
btn.place(width=100,height=50,x=725,y=250)
btn.configure(bg='pink',text = 'apply',command = conf)

move()

tk.mainloop()
