from tkinter import *
class Gui:
    def __init__(self,what,xx,txt,siz,cmd):
        self.what = what(tk)
        self.what.place(width=100,height=50,x=xx,y=600)
        self.what.configure(bg='light green',text = txt,font=('Arial',siz),command = cmd)
        
def dlt():
    cc.delete('ee')
      
def move ():
    cc.create_oval(0,0,1200,600,fill='pink', outline='',tag='ee')
    cc.after(100,lambda:dlt())
    cc.after(int(60000/speed),lambda:move())
        
def fast():
    global speed
    speed += 10
    speed_frame = Gui(Label,550,str(speed),'30',None)

def slow():
    global speed
    speed -= 10
    speed_frame = Gui(Label,550,str(speed),'30',None)

speed = 120 

tk = Tk()
tk.geometry('1200x650')

cc = Canvas(tk)
cc.place(width=1200,height=600,x=0,y=0)
cc.configure(bg='#000060')

speed_frame = Gui(Label,550,'120','30',None)
fbtn = Gui(Button,700,'faster','12',fast)
sbtn = Gui(Button,400,'slower','12',slow)

move()

tk.mainloop()
