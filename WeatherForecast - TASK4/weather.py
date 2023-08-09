from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def getWeather():
    city_name = search_country.get()
    city_location = Nominatim(user_agent="geoapiExercises")
    location = city_location.geocode(city_name)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
    home = pytz.timezone(result)
    localtime = datetime.now(home)
    current_time = localtime.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="WEATHER UPDATE")

    weather_api = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=1a3a05374949eff7b31d7ed0124795b9"

    json_data = requests.get(weather_api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    text1.config(text=(temp,"°"))
    c.config(text=(condition,"|",temp,"°"))

    windtext.config(text=wind)
    humidtext.config(text=humidity)
    desctext.config(text=description)
    presstext.config(text=pressure)
    





root = Tk()
root.title("Weather Forecasting App")
root.geometry("900x600")

search_field = PhotoImage(file="Copy of search.png")
searchImage = Label(image=search_field)
searchImage.place(x=360,y=45)

search_country = Entry(root,justify="center", width=17, font="lucida 25", bg="#404040", fg="white", border=0)
search_country.place(x=400, y=65)
search_country.focus()

search_icon = PhotoImage(file="Copy of search_icon.png")
search_button = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
search_button.place(x=740,y=58)

weather_logo=PhotoImage(file="weatherlogo.png")
logo = Label(image=weather_logo)
logo.place(x=80, y=0)

show_data = PhotoImage(file="Copy of box.png")
data_image = Label(image=show_data)
data_image.pack(padx=5,pady=5,side=BOTTOM)

name = Label(root,font="arial 20 bold", fg="#1ab5ef")
name.place(x=320,y=225)

clock=Label(root, font="Helvetica 20 bold")
clock.place(x=380, y=270)

wind_label = Label(root, text="WIND", font="Helvetica 15 bold", fg="white", bg="#1ab5ef")
wind_label.place(x=120,y=500)

humidity_label = Label(root, text="HUMIDITY", font="Helvetica 15 bold", fg="white", bg="#1ab5ef")
humidity_label.place(x=250,y=500)

desc_label = Label(root, text="DESCRIPTION", font="Helvetica 15 bold", fg="white", bg="#1ab5ef")
desc_label.place(x=430,y=500)

pressure_label = Label(root, text="PRESSURE", font="Helvetica 15 bold", fg="white", bg="#1ab5ef")
pressure_label.place(x=650,y=500)

text1 = Label(font="arial 40 bold", fg="#ee666d")
text1.place(x=400,y=150)

c=Label(font="arial 20 bold", fg="#ee666d")
c.place(x=380,y=320)

windtext = Label(text="?", font="arial 15 bold", bg="#1ab5ef", fg="black")
windtext.place(x=130,y=535)

humidtext = Label(text="?", font="arial 15 bold", bg="#1ab5ef", fg="black")
humidtext.place(x=288,y=535)

desctext = Label(text="?", font="arial 15 bold", bg="#1ab5ef", fg="black")
desctext.place(x=435,y=535)

presstext = Label(text="?", font="arial 15 bold", bg="#1ab5ef", fg="black")
presstext.place(x=687,y=535)


root.mainloop()