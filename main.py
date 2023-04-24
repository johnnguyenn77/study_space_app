from tkinter import *
import json
from datetime import datetime
import pip._vendor.requests as requests
import time

#Initialize Window

root = Tk()
root.geometry("400x400") #size of the window by default
root.configure(bg='#222222')
#title of our window
root.title("Your study spacce")

def start():
    global is_running
    global start_time
    if not is_running:
        is_running = True
        start_time = time.time()
        update_time()
 
# Stop the stopwatch
def stop():
    global is_running
    is_running = False
 
# Update the elapsed time
def update_time():
    if is_running:
        elapsed_time = time.time() - start_time
        time_label.config(text="{:.2f}".format(elapsed_time))
        time_label.after(50, update_time)

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y) 
 
# ----------------------Functions to fetch and display weather info
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
 
city_value = StringVar()
 
def showWeather():
    #Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "7a050779e88d874aee40ae9332caf333"  #sample API
 
    # Get city name from user from the input field (later in the code)
    city_name=city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end")   #to clear the text field for every new output
 
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched
 
 
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 
#-----------Storing the fetched values of weather of a city
 
        temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
#assigning Values to our weather varaible, to display as output
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
 
#Frontend part of code - Interface

weather_frame = Frame(root, bd=4, bg="white")
weather_frame.place(x=10, y=10)
make_draggable(weather_frame)

stopwatch_frame = Frame(root, bd=4, bg = 'white')
make_draggable(stopwatch_frame)

font_tuple_city_head = ("Courier New", 12, "bold")
font_tuple_inp_city = ("Courier New", 14, "bold")

time_label = Label(stopwatch_frame, text="0.00", font=("Helvetica", 48))
time_label.place(x=110, y=190)
 
# Create the start and stop buttons
start_button = Button(stopwatch_frame, text="Start", width=10, command=start)
start_button.place(x=10, y=10)
stop_button = Button(stopwatch_frame, text="Stop", width=10, command=stop)
stop_button.place(x=260, y=10)
 
# Flag to track whether the stopwatch is running
is_running = False

city_head= Label(weather_frame, text = 'Enter City Name', font = font_tuple_city_head).pack(pady=10) #to generate label heading

inp_city = Entry(weather_frame, textvariable = city_value,  width = 24, font= font_tuple_inp_city).pack()

Button(weather_frame, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(weather_frame, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(weather_frame, width=46, height=10)
tfield.pack()
stopwatch_frame.pack()

root.mainloop()
