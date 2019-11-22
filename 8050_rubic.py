from tkinter import *

class Buttons:
    def __init__(self,t,xx,yy,txt):
        self.button = Button(t)
        self.button.place(width=160,height=35,x=xx,y=yy)
        self.button.configure(bg='yellow',text = txt)
        self.button.bind('<Button-1>', lambda event: click(txt))
def change_side(a,b,c,d,e,f,g,h,i,j,k,ll,m,n,o,p,q,r,s,t):
    l[a],l[b],l[c],l[d],l[e],l[f],l[g],l[h],l[i],l[j],l[k],l[ll],l[m],l[n],l[o],l[p],l[q],l[r],l[s],l[t] \
        = l[j],l[k],l[ll],l[a],l[b],l[c],l[d],l[e],l[f],l[g],l[h],l[i],l[s],l[t],l[m],l[n],l[o],l[p],l[q],l[r]
def change_middle(a,b,c,d,e,f,g,h,i,j,k,ll):
    l[a],l[b],l[c],l[d],l[e],l[f],l[g],l[h],l[i],l[j],l[k],l[ll] = l[j],l[k],l[ll],l[a],l[b],l[c],l[d],l[e],l[f],l[g],l[h],l[i]       
def click(txt):
    if txt == 'top   -->' or txt == 'whole   -->':change_side(9,12,15,51,48,45,18,21,24,0,3,6,29,32,35,34,33,30,27,28)
    if txt == 'top   <--' or txt == 'whole   <--':change_side(18,21,24,51,48,45,9,12,15,0,3,6,33,30,35,34,29,32,27,28)
    if txt == 'right   \\/' or txt == 'whole   \\/':change_side(44,41,38,53,52,51,35,32,29,6,7,8,11,14,17,16,15,12,9,10)
    if txt == 'right   /\\' or  txt == 'whole   /\\':change_side(35,32,29,53,52,51,44,41,38,6,7,8,15,12,17,16,11,14,9,10)
    if txt == 'left   /\\' or  txt == 'whole   /\\':change_side(33,30,27,47,46,45,42,39,36,0,1,2,18,21,20,19,26,23,24,25) 
    if txt == 'left   \\/' or txt == 'whole   \\/':change_side(42,39,36,47,46,45,33,30,27,0,1,2,26,23,20,19,18,21,24,25)
    if txt == 'battom   -->' or txt == 'whole   -->':change_side(11,14,17,53,50,47,20,23,26,2,5,8,44,41,38,37,36,39,42,43)
    if txt == 'battom   <--' or txt == 'whole   <--':change_side(20,23,26,53,50,47,11,14,17,2,5,8,36,39,38,37,44,41,42,43)
    if txt == 'front clackwise' or txt == 'whole clackwise':change_side(9,10,11,44,43,42,26,25,24,27,28,29,6,7,8,5,2,1,0,3)
    if txt == 'front cnter clackwise' or txt == 'whole cnter clackwise':change_side(26,25,24,44,43,42,9,10,11,27,28,29,2,1,8,5,6,7,0,3)
    if txt == 'back clackwise' or txt == 'whole clackwise':change_side(15,16,17,38,37,36,20,19,18,33,34,35,51,52,53,50,47,46,45,48)
    if txt == 'back cnter clackwise' or txt == 'whole cnter clackwise':change_side(20,19,18,38,37,36,15,16,17,33,34,35,47,46,53,50,51,52,45,48)
    if txt == 'whole   /\\':change_middle(34,31,28,50,49,48,43,40,37,3,4,5)
    if txt == 'whole   \\/':change_middle(43,40,37,50,49,48,34,31,28,3,4,5)
    if txt == 'whole   -->':change_middle(10,13,16,52,49,46,19,22,25,1,4,7)
    if txt == 'whole   <--':change_middle(19,22,25,52,49,46,10,13,16,1,4,7)
    if txt == 'whole clackwise':change_middle(12,13,14,41,40,39,23,22,21,30,31,32)
    if txt == 'whole cnter clackwise':change_middle(23,22,21,41,40,39,12,13,14,30,31,32)
    cnvs.delete('ee')
    make()
mid = 338
lst_0 = [i for i in ['#ff8000','green','#0000c0','white','yellow','#ff0000'] for j in range(9)]     
l = [i for i in lst_0]
 
tk = Tk()
tk.geometry('1010x675')
tk.title('rubics cube!')
cnvs = Canvas(tk)
cnvs.place(width=675,height=675,x=0,y=0)
cnvs.configure(bg='tan')

n = [-95,-35,-30,30,35,95]   
nrb = [[95,125,-95,-125,-65,-35,-30,-60,0,30,35,5,65,95],[128,158,-128,-158,-98,-68,-63,-93,-33,-3,2,-28,32,62]\
    ,[161,191,-161,-191,-131,-101,-96,-126,-66,-36,-31,-61,-1,29]]
ntr = [[-95,-125,-65,-5,-35,-95,0,60,30,-30,65,125,95,35],[-128,-158,-32,28,-2,-62,33,93,63,3,98,158,128,68]\
    ,[-161,-191,1,61,31,-29,66,126,96,36,131,191,161,101]]
def make():
    for i in range(3):
        for j in range(3):
            tpl = (mid + n[0 + i * 2],mid + n[0 + j * 2], mid + n[1 + i * 2],mid + n[0 + j * 2],\
                 mid + n[1 + i * 2],mid + n[1 + j * 2], mid + n[0 + i * 2],mid + n[1 + j * 2] ) 
            cnvs.create_polygon(tpl,fill=l[j + i * 3], outline='#000000', width=5,tag='ee')
            tpl = (mid + nrb[i][0] , mid + nrb[i][j * 4 + 2],mid + nrb[i][1], mid + nrb[i][j * 4 + 3],\
                 mid + nrb[i][1], mid + nrb[i][j * 4 + 4],mid +nrb[i][0], mid + nrb[i][j * 4 + 5]) 
            cnvs.create_polygon(tpl,fill=l[9 + j + i * 3], outline='#000000', width=5,tag='ee') 
            tpl = (mid + ntr[i][j * 4 + 2],mid + ntr[i][1], mid + ntr[i][j * 4 + 3], mid + ntr[i][1],\
                 mid + ntr[i][j * 4 + 4],mid +ntr[i][0], mid + ntr[i][j * 4 + 5],mid +ntr[i][0]) 
            cnvs.create_polygon(tpl,fill=l[27 + j + i * 3], outline='#000000', width=5,tag='ee') 
make()            

set_1 = [ Buttons(tk,763,k * 120 + 30,['whole   /\\','whole   \\/'][k]) for k in range(2)]
set_2 = [ Buttons(tk,680,k * 40 + 70,['whole   <--','whole clackwise'][k]) for k in range(2)]
set_3 = [ Buttons(tk,845,k * 40 + 70,['whole   -->','whole cnter clackwise'][k]) for k in range(2)]
set_4 = [ Buttons(tk,680,k * 40 + 230,['top   <--','left   /\\','back clackwise','front clackwise','left   \\/','battom   <--'][k]) for k in range(6)]
set_5 = [ Buttons(tk,845,k * 40 + 230,['top   -->','right   /\\','back cnter clackwise','front cnter clackwise','right   \\/','battom   -->'][k]) for k in range(6)]

tk.mainloop()

"""
           ------------             ------------
           | 33 34 35 |             | 45 48 51 |
           | 30 31 32 |             | 46 49 52 |
           | 27 28 29 |             | 47 50 53 |
----------------------------------  ------------
| 18 21 24 | 0  3  6  | 9  12 15 |      back
| 19 22 25 | 1  4  7  | 10 13 16 |  
| 20 23 26 | 2  5  8  | 11 14 17 | 
---------------------------------   
           | 42 43 44 |
           | 39 40 41 |
           | 36 37 38 |
           ------------
"""