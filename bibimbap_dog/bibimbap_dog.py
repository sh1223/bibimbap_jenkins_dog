from threading import Thread, Event
import os, sys
import time
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class BibimbapJenkinsDog(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Bibimbap Jenkins Dog")
        self.geometry("820x550")
        self.columnconfigure(0, weight=1)

        container = ttk.Frame(self)
        container.grid()

        monitoring = Monitoring(container)
        monitoring.grid()


class Monitoring(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.running = "standby"

        self.hostname = tk.StringVar()
        self.interval = tk.StringVar(value=300) # default value set with value arg
        self.info_value = tk.StringVar(value="Bibimbap jenkins dog ready")

        name_label = ttk.Label(self, text="Host name: ")
        name_entry = ttk.Entry(self, width=38, textvariable=self.hostname)
        
        ping_interval_label = ttk.Label(self, text="Interval: ")
        ping_interval_entry = ttk.Entry(self, width=15, textvariable=self.interval)
        
        start_button = ttk.Button(self, text="start", command=self.start_thread)
        stop_button = ttk.Button(self, text="stop", command=self.stop)
        
        self.text_box_1 = tk.Text(self, width=50)
        self.text_box_2 = tk.Text(self, width=50)

        info_label = ttk.Label(self, textvariable=self.info_value)

        
        name_label.grid(row=0, column=0, padx=(0, 10), pady=(10,0), sticky="E")
        name_entry.grid(row=0, column=1, pady=(10,0), sticky="W")
        name_entry.focus()
        
        ping_interval_label.grid(row=1, column=0, padx=(0, 10), pady=(10,10), sticky="E")
        ping_interval_entry.grid(row=1, column=1, pady=(10,10), sticky="w")
        
        start_button.grid(row=2, column=0, pady=(0,10), sticky="E")
        stop_button.grid(row=2, column=1, pady=(0,10), sticky="W")
        
        self.text_box_1.grid(row=3, column=0)
        self.text_box_1.bind("<Key>", lambda e: "break")
        self.text_box_2.grid(row=3, column=1)
        self.text_box_2.bind("<Key>", lambda e: "break")

        info_label.grid(row=4, column=1, sticky="E")

    def start_thread(self):
        self.running = "run"
        self.t = Thread(target = self.scanning)
        self.t.start()

    def stop(self):
        self.running = "stop"
        self.info_value.set("stop")

    def scanning(self):
        while self.running == "run":
            _hostname = self.hostname.get() #"google.com"
            self.info_value.set(f"bibimbap jenkins dog listens to {_hostname}")
            try:
                _interval = int(self.interval.get())
            except ValueError:
                _interval = 60

            response = os.system("ping -c 1 " + _hostname)

            if response == 0:
                print(_hostname, 'is up!')
                self.text_box_1.configure(state="normal")
                self.text_box_1.insert("end-1c", f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {_hostname} up!\n")
                self.text_box_1.configure(state="disabled")
                print(self.text_box_1.index("end"), "@@@@@@@@@@@")

                if int(self.text_box_1.index("end").split('.')[0]) > 26:
                    self.text_box_1.configure(state="normal")
                    self.text_box_1.delete("1.0", "end")
                    self.text_box_1.configure(state="disabled")
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            else:
                print(_hostname, 'is down!')
                self.text_box_2.configure(state="normal")
                self.text_box_2.insert("end-1c", f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {_hostname} is down !\n Let's restart jenkins server\n")
                self.text_box_2.configure(state="disabled")
                
                # TODO
                # run command line

                if int(self.text_box_1.index("end").split('.')[0]) > 26:
                    self.text_box_1.configure(state="normal")
                    self.text_box_1.delete("1.0", "end")
                    self.text_box_1.configure(state="disabled")
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                
                time.sleep(15)

            time.sleep(_interval)  


if __name__ == "__main__":
    root = BibimbapJenkinsDog()
    root.columnconfigure(0, weight=1)
    root.mainloop()