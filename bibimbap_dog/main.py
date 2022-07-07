import os
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime


running = "standby"

def bibimbap_dog():
    if running == "run":

        _hostname = hostname.get() #"google.com"

        try:
            _interval = int(interval.get())
        except ValueError:
            _interval = 1000 * 60

        response = os.system("ping -c 1 " + _hostname)

        #and then check the response...
        if response == 0:
            print(_hostname, 'is up!')
            text_box_1.configure(state="normal")
            text_box_1.insert("end-1c", f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {_hostname} up!\n")
            text_box_1.configure(state="disabled")
            print(text_box_1.index("end"), "@@@@@@@@@@@")

            if int(text_box_1.index("end").split('.')[0]) > 26:
                text_box_1.configure(state="normal")
                text_box_1.delete("1.0", "end")
                text_box_1.configure(state="disabled")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        else:
            print(_hostname, 'is down!')
            text_box_2.configure(state="normal")
            text_box_2.insert("end-1c", f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {_hostname} is down !\n Let's restart jenkins server\n")
            text_box_2.configure(state="disabled")
            
            # TODO
            # run command line

            if int(text_box_1.index("end").split('.')[0]) > 26:
                text_box_1.configure(state="normal")
                text_box_1.delete("1.0", "end")
                text_box_1.configure(state="disabled")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            
            time.sleep(10)

        root.after(_interval, bibimbap_dog)

    if running == "standby":
        #print("standby")
        ##https://stackoverflow.com/questions/55739436/how-to-retrieve-lines-from-text-widget-individually
        #if text_box_1.get('current linestart', 'current lineend').strip() != "standby":
        #    text_box_1.configure(state="normal")
        #    text_box_1.insert("end-1c", "standby\n")
        #    text_box_1.configure(state="disabled")
        root.after(5000, bibimbap_dog)
    
    if running == "stop":
        print("stop")
        root.after(5000, bibimbap_dog)

def start():
    global running
    running = "run"


def stop():
    global running
    running = "stop"


root = tk.Tk()
root.title("Bibimbap jenkins dog")
root.geometry("820x550")
#root.resizable(False, False)
root.columnconfigure(0, weight=1)

hostname = tk.StringVar()
interval = tk.StringVar(value=60000) # default value set with value arg


input_frame = ttk.Frame(root, padding=(20, 10, 20, 0)) #left, top, right, buttom
input_frame.grid(row=0, column=0) # grid goes to root

name_label = ttk.Label(input_frame, text="Host name: ")
name_label.grid(row=0, column=0, padx=(0, 10)) # grid goes to input_frame
name_entry = ttk.Entry(input_frame, width=50, textvariable=hostname)
name_entry.grid(row=0, column=1) # grid goes to input_frame
name_entry.focus()

ping_interval_label = ttk.Label(input_frame, text="Interval: ")
ping_interval_label.grid(row=1, column=0, padx=(0, 10)) # grid goes to input_frame
ping_interval_entry = ttk.Entry(input_frame, width=15, textvariable=interval)
ping_interval_entry.grid(row=1, column=1, sticky="w") # grid goes to input_frame


button_frame = ttk.Frame(root, padding=(20, 10)) #x, y
button_frame.grid(row=1, column=0)

start_button = ttk.Button(button_frame, text="start", command=start)
start_button.grid(row=0, column=0)

stop_button = ttk.Button(button_frame, text="stop", command=stop)
stop_button.grid(row=0, column=1)


text_frame = ttk.Frame(root)
text_frame.grid(row=2, column=0)

text_box_1 = tk.Text(text_frame, width=50)
text_box_1.grid(row=0, column=0)
#https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
text_box_1.bind("<Key>", lambda e: "break")

text_box_2 = tk.Text(text_frame, width=50)
text_box_2.grid(row=0, column=1)
text_box_2.bind("<Key>", lambda e: "break")

root.after(5000, bibimbap_dog)
root.mainloop()
        
