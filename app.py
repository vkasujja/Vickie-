from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    try:
        city=textfield.get()
        
        geolocater= Nominatim(user_agent="geoapiExercises")
        location= geolocater.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5e4263b98295ffd47ff7e62da7b20409"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main'] 
        description = json_data['weather'][0]['description']  
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))  
    
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)                    
    
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")    
    
#search box
search_image=PhotoImage(file="box.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),)
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="img.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=360,y=40)
image = Image.open("img.png")
resized_image = image.resize((32, 32), Image.LANCZOS)
resized_image.save("img.png")
icon_image = tk.PhotoImage(file="img.png")

#logo
logo_iage=PhotoImage(file="logoo.png")
logo=Label(image=logo_iage)
logo.place(x=150,y=100)
image = Image.open("logoo.png")
resized_image = image.resize((100, 100), Image.LANCZOS)
resized_image.save("logoo.png")
icon_image = tk.PhotoImage(file="logoo.png")

#Bottom box
Frame_image=PhotoImage(file="frame.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=0,pady=0,side=BOTTOM)
image = Image.open("frame.png")
resized_image = image.resize((670, 150), Image.LANCZOS)
resized_image.save("frame.png")
icon_image = tk.PhotoImage(file="frame.png")

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
Label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label1.place(x=170,y=400)

Label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label2.place(x=270,y=400)

Label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label3.place(x=420,y=400)

Label4=Label(root,text="PRSSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label4.place(x=630,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=300,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=150)

w=Label(text="...",font=("arial",20,"bold"),bg="#4169E1")
w.place(x=180,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#4169E1")
h.place(x=300,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#4169E1")
d.place(x=480,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#4169E1")
p.place(x=670,y=430)  



root.mainloop()