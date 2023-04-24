from tkinter import *
import json
from datetime import datetime
import pip._vendor.requests as requests
import time
from stopwatch import stopwatch
from weather import weather_widget
from make_draggable import make_draggable

#Initialize Window

root = Tk()
root.configure(bg='#222222')
root.geometry('1280x720')
root.title("Your study spacce")
     
#Frontend part of code - Interface

weatherWidget = weather_widget(root)

stopwatch_frame = Frame(root, bd = 4, bg = 'white')
stopwatch_frame.place(x=10, y=20)
make_draggable(stopwatch_frame)

a = stopwatch(root)

notes = Text(stopwatch_frame)
notes.pack()

root.mainloop()
