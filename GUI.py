import tkinter as tk
from tkinter import *
from Profil import CPM, BMI


root = Tk()
title = tk.LabelFrame(master=root, text="CALORIES CALCULATOR", width= 150, height = 20, bg = "red")
title.pack()

wejsciowe = tk.Frame (master=root, width=100, height = 250,bg="green")
wejsciowe.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
wyjsciowe = tk.Frame(master=root, width=100, height=250,bg="blue")
wyjsciowe.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

ageL = Label(wejsciowe, text="Age")
ageL.pack()
age = tk.Entry(wejsciowe,bd=5)
age.pack()

heighL = Label(wejsciowe, text="Heigh [cm]")
heighL.pack()
heigh = tk.Entry(wejsciowe)
heigh.pack()

weightL = Label(wejsciowe, text="Weight [kg]")
weightL.pack()
weight = tk.Entry(wejsciowe)
weight.pack()

variable = StringVar(wejsciowe)
variable.set("K") # default value

w = OptionMenu(wejsciowe, variable, "W", "M",)
w.pack()

activityL = Label(wejsciowe, text="Activity")
activityL.pack()
variable2 = StringVar(wejsciowe)
variable.set("K") # default value

w = OptionMenu(wejsciowe, variable2, "big", "medium","small")
w.pack()



root.mainloop()
