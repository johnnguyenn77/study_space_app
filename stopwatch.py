from tkinter import *
import sys
import time
from make_draggable import make_draggable

global count
count = 0
class stopwatch():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00.000')        
        
    def start(self):
        global count
        count = 0
        self.timer()   
        
    def stop(self):
        global count
        count=1
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h, m, sms = map(int(float()), self.d.split(":"))
            h = int(h)
            ms, s = divmod(sms, 1000)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                ms += 1
                if(ms == 1000):
                    ms = 0
                    if(m<59):
                        m+=1
                    elif(m==59):
                        m=0
                        h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            if(ms<10):
                ms=str(00)+str(ms)
            elif(ms<100):
                ms=str(0)+str(ms)
            else:
                ms=str(ms)
            self.d=h+":"+m+":"+s+"."+ms           
            self.t.set(self.d)
            if(count==0):
                self.frame.after(1, self.timer)     
                
    def __init__(self, root):
        self.frame = Frame(root, bd = 4, bg = 'white')
        make_draggable(self.frame)
        self.frame.place(x=10, y=20)
        self.t = StringVar()
        self.t.set("00:00:00.000")
        
        lb = Label(self.frame, textvariable = self.t, font=('Helvetica',40), bg = "white").pack()
        
        buttonframe = Frame(self.frame)
        buttonframe.pack()
    
        bt1 = Button(buttonframe, text="Start", width=5,height=1, command= self.start, font=('Helvetica', 12), bg = ("white")).grid(row=0, column=0)#.pack(side = LEFT)
        bt2 = Button(buttonframe, text="Stop", width=5,height=1, command= self.stop, font=('Helvetica', 12), bg = ("white")).grid(row=0, column = 1)#pack(side = LEFT)
        bt3 = Button(buttonframe, text="Reset", width=5,height=1, command= self.reset, font=('Helvetica', 12), bg = ("white")).grid(row=0, column=3)#pack(side = LEFT)
        
# test setup
root = Tk()
root.configure(bg='#222222')
root.geometry('1280x720')
root.title("Your study spacce")
a = stopwatch(root)

root.mainloop()      