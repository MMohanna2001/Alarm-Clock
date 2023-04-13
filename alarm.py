# Import necessary libraries
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from PIL import ImageTk, Image
from pygame import mixer
from time import sleep
from threading import Thread

counter = 0
#Function to play the alarm sound according to the user's choice 
def sound_alarm():
    if musicbox.get() == 'Simple Alarm':
       mixer.music.load('alarm.mp3')
    elif musicbox.get() == 'Short Tone':
       mixer.music.load('short.mp3')
    elif musicbox.get() == 'Biohazard':
       mixer.music.load('biohazard.mp3')
    elif musicbox.get() == 'Buzzer':
       mixer.music.load('buzzer.mp3')
    
    mixer.music.play()

#Alarm Control Function
def alarm():
    while 1:
        #Getting the Desired Set Time
        control = selected.get()
        alarmH = hourbox.get()
        alarmM = minbox.get()
        alarmS = secbox.get()

        #Getting The Current Time 
        now = datetime.now()
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        second = now.strftime("%S")

        #In Case of Snooze
        if control == 3:
           sleep(1)  
           global counter 
           counter += 1
           if counter == 5:
            sound_alarm()
        
        #If the Set radio button is checked and the desired set time is equal to the desired time
        if control == 1 :
         #To Get Updated Every Second
         sleep(1)
         if  alarmH == hour and alarmM == minute and alarmS == second:
            sound_alarm()

#Function to Activate The alarm
def activate_alarm():
   thread = Thread(target=alarm) #a neew thread to activate alarm
   thread.start()

#Function to Deactivate The alarm
def deactivate_alarm():
   mixer.music.stop()
   selected.set(0)

#Function to Snooze The alarm
def snooze_alarm():
   mixer.music.stop()
   global counter
   counter = 0
   activate_alarm()

#Window configuration
window = Tk() 
window.geometry('350x150')
window.title("Alarm Clock")
window.configure(bg="white")
window.resizable(True, True) # Set the window to be resizable in both directions

#Frame Line Configuration
frame_line = Frame(window, width=350, height=10)
frame_line.grid(row=0, column=0)
canvas = Canvas(frame_line, width=350, height=10, bg="red")
canvas.pack()

#Frame Body Configuration
frame_body = Frame(window, width=350, height=350)
frame_body.grid(row=1, column=0)

#Adding a Photo to the Window
img = Image.open('clk.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)
alarm_image = Label(frame_body,image = img)
alarm_image.place(x = 10, y = 10)

#Creating a Heading For the window
name = Label(frame_body,text= "Alarm", font=('Ivy 25 bold'))
name.place(x = 140,y = 10)

#Creating a Combobox for the user's to choose the desired alarm tone
tones = "Simple Alarm", "Biohazard", "Buzzer", "Short Tone"
musicbox = Combobox(frame_body,width=10,font=('arial 10'),values=tones,state="readonly")
musicbox.place(x=240,y=20)
musicbox.current(0)

#Hours Combobox
hour = Label(frame_body,text= "Hours", font=('Ivy 10 bold italic'))
hour.place(x = 120,y = 50)
hour_values = [str(i).zfill(2) for i in range(24)]
hourbox = Combobox(frame_body, width=2, font=('arial 15'),values=hour_values,state="readonly")
hourbox.current(0)
hourbox.place(x=120,y=70)

#Mins Combobox
min = Label(frame_body,text= "Minutes", font=('Ivy 10 bold italic'))
min.place(x = 180,y = 50)
min_values = [str(i).zfill(2) for i in range(60)]
minbox = Combobox(frame_body, width=2, font=('arial 15'),values=min_values,state="readonly")
minbox.current(0)
minbox.place(x=180,y=70)

#Sec Combobox
sec = Label(frame_body,text= "Seconds", font=('Ivy 10 bold italic'))
sec.place(x = 250,y = 50)
sec_values = [str(i).zfill(2) for i in range(60)]
secbox = Combobox(frame_body, width=2, font=('arial 15'),values=sec_values,state="readonly")
secbox.current(0)
secbox.place(x=250,y=70)

selected = IntVar()

#Set Radio Button
set = Radiobutton(frame_body, value=1,text="SET",command=activate_alarm, variable=selected)
set.place(x=160,y=105)

#Stop Radio Butoon
stop = Radiobutton(frame_body, value=2,text="Stop",command=deactivate_alarm, variable=selected)
stop.place(x=205,y=105)

#Snooze Radio Button
snooze = Radiobutton(frame_body,value=3,text='Snooze',command=snooze_alarm,variable=selected)
snooze.place(x=250,y=105)


mixer.init() #Intailize Mixer Module
window.mainloop() #Start Main Loop