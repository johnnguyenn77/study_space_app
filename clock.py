# importing whole module
from tkinter import *
#from tkinter.ttk import *
from make_draggable import make_draggable
from time import strftime # importing strftime function to retrieve system's time
 
class clock:
# This function is used to display time on the label
    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.time)
        
    def __init__(self, root):
        # Styling the label widget so that clock will look more attractive
        self.frame = Frame(root, bd = 4, bg = 'white')
        make_draggable(self.frame)
        self.frame.place(x=10, y=20)
        
        self.lbl = Label(self.frame, font=('calibri', 40, 'bold'), bg='white', fg='black')
        self.lbl.pack(anchor='center') # Placing clock at the centre of the tkinter window
        self.time()

# creating tkinter window

root = Tk()
root.title('Clock')
a = clock(root)
mainloop()