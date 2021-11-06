import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Profil import male_cpm_small, male_cpm_medium, male_cpm_big, female_cpm_medium,female_cpm_small,female_cpm_big
from Profil import BMI

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = tk.Label(self, text="CALORIES APP", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=4, padx=10, pady=10)
        image2 = Image.open("C:/Users/emilk/PycharmProjects/CaloriesCalendarGit/CaloriesCalendar/calculatorcalories.png")
        image1 = image2.resize((300, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image1)

        label2 = tk.Label(self, image=photo)
        label2.image = photo
        label2.grid(row=1,column=2,rowspan=6, columnspan=5)

        button1 = tk.Button(self, text="Calculator",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text="Calories",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = tk.Button(self, text="History",
                             command=lambda: controller.show_frame(Page3))

        # putting the button in its place by
        # using grid
        button3.grid(row=3, column=1, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CALCULATOR", font=LARGEFONT)
        label.grid(row=0, column=2, columnspan = 4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text="MENU",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = tk.Button(self, text="CALORIES",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

        ageL = tk.Label(self, text="Age")
        ageL.grid(row=1,column=2)
        age = tk.Entry(self)
        age.grid(row=1,column=3)

        heighL = tk.Label(self, text="Heigh [cm]")
        heighL.grid(row=2,column=2)
        heigh = tk.Entry(self)
        heigh.grid(row=2,column=3)

        weightL = tk.Label(self, text="Weight [kg]")
        weightL.grid(row=3,column=2)
        weight = tk.Entry(self)
        weight.grid(row=3,column=3)

       # variable = tk.StringVar(self)
       # variable.set("K")
       # wL = tk.Label(self, text="Sex")
        #wL.grid(row=4, column=2)
       # w = tk.OptionMenu(self, variable, "W", "M", )
        wL = tk.Label(self, text="Sex: W/M")
        wL.grid(row=4, column=2)
        w = tk.Entry(self)
        w.grid(row=4,column=3)

        #activityL = tk.Label(self, text="Activity")
       # activityL.grid(row=5,column=2)
        #variable2 = tk.StringVar(self)
        #variable2.set("small")  # default value


        #z = tk.OptionMenu(self, variable2, "big", "medium", "small")
        zL = tk.Label(self, text="Activity: small/medium/big")
        zL.grid(row=5, column=2)
        z=tk.Entry(self)
        z.grid(row=5,column=3)


        cpm_output = tk.Label(self)
        cpm_output.grid(row=7, column=3)

        bmi_output = tk.Label(self)
        bmi_output.grid(row=8, column=3)

        def calculateCPM():
            Heigh=float (heigh.get())
            Weight = float (weight.get())
            Age = float (age.get())

            if w.get() =="W":
                if z.get() == "big":
                    cpm = female_cpm_big(Weight,Heigh,Age)
                if  z.get()== "medium":
                    cpm = female_cpm_medium(Weight,Heigh,Age)
                if z.get() == "small":
                    cpm = female_cpm_small(Weight,Heigh,Age)
            else:

                if z.get() == "big":
                    cpm = male_cpm_big(Weight,Heigh,Age)
                if z.get() == "medium":
                    cpm = male_cpm_medium(Weight,Heigh,Age)
                if z.get() == "small":
                    cpm = male_cpm_small(Weight,Heigh,Age)

            cpm_output.config(text=int(cpm))
            a = tk.Label(self,text="YOUR CPM : ")
            a.grid(row=7, column=2)


        def calculateBMI():
            Heigh = float(heigh.get())
            Weight = float(weight.get())

            bmi = BMI(Weight,Heigh)
            bmi_output.config(text=int(bmi))
            b = tk.Label(self, text="YOUR BMI : ")
            b.grid(row=8, column=2)


        button = tk.Button(self, text="CALCULATE CPM", command=calculateCPM)
        button.grid(row=5,column=1)

        button2=tk.Button(self,text="CALCULATE BMI", command=calculateBMI)
        button2.grid(row=6,column=1)




# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)
# Driver Code
app = tkinterApp()
app.mainloop()
