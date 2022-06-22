#Build a Python GUI software that uses the tkinter package to create progress bar widgets.
import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
parent = tk.Tk()
parent.title("PROGRESSBAR")
parent.geometry('300x200')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(parent, length=250, style='black.Horizontal.TProgressbar')
bar['value'] = 90
bar.grid(column=0, row=0)
my_label = tk.Label(parent, text="90%")
my_label.grid(column=1, row=0)
my_label = tk.Label(parent, text="loading please wait...")
my_label.grid(column=0, row=1)
parent.mainloop()