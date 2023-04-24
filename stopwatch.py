from tkinter import *
import sys
import time
global count
count =0
class stopwatch():
    def reset(self):
        global count
        count=1
        self.t.set('00:00:00')        
        
    def start(self):
        global count
        count=0
        self.timer()   
        
    def stop(self):
        global count
        count=1
        
    def close(self):
        self.frame_name.destroy()
        
    def timer(self):
        global count
        if(count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
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
            self.d=h+":"+m+":"+s           
            self.t.set(self.d)
            if(count==0):
                self.frame_name.after(1000,self.timer)     
                
    def __init__(self, root_name):
        self.frame_name = Frame(root_name, bd = 4, bg = 'white')
        self.frame_name.place(x=10, y=20)
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.frame_name,textvariable=self.t,font=("Times 40 bold"),bg="white")
        self.bt1 = Button(self.frame_name,text="Start",command=self.start,font=("Times 12 bold"),bg=("green"))
        self.bt2 = Button(self.frame_name,text="Stop",command=self.stop,font=("Times 12 bold"),bg=("red"))
        self.bt3 = Button(self.frame_name,text="Reset",command=self.reset,font=("Times 12 bold"),bg=("orange"))
        self.lb.place(x=160,y=10)
        self.bt1.place(x=120,y=100)
        self.bt2.place(x=220,y=100)
        self.bt3.place(x=320,y=100)
        self.label = Label(self.frame_name,text="",font=("Times 40 bold"))
        self.frame_name.pack()
        
        
#a = stopwatch()      