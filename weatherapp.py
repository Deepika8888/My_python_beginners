#importing tkinker module
from tkinter import *
from tkinter import ttk

import requests 

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=6983dfa98d0edae5af05846372281ce4").json()
    
    wb_label.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=(data["main"]["temp"]-273.15))
    pre_label1.config(text=data["main"]["pressure"])

    

win = Tk()
win.title(" Weather App")
win.config(bg= "pink")
win.geometry("500x570")

name_label = Label(win,text="My weather app", font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Dhangadhi", "Kathmandu", "Pokhara", "Birjung", "Biratnagar", "Butwal", "Hetauda"]
com = ttk.Combobox(win, values=list_name, font=("Times New Roman",30,"bold"), textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)




w_label = Label(win,text="Weather climate", font=("Times New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="", font=("Times New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather description", font=("Times New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text="", font=("Times New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperature", font=("Times New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="", font=("Times New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)


pre_label = Label(win,text="Pressure", font=("Times New Roman",20))
pre_label.place(x=25,y=470,height=50,width=210)

pre_label1 = Label(win,text="", font=("Times New Roman",20))
pre_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Get Weather Data", font=("Times New Roman",30,"bold"), command=data_get)
done_button.place(y=190,height=50,width=300,x=150)


win.mainloop()