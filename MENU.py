import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import Canvas, INSERT
from tkinter import filedialog as fd
from tkinter import messagebox

from PIL import Image, ImageTk
from Profil import male_cpm_small, male_cpm_medium, male_cpm_big, female_cpm_medium,female_cpm_small,female_cpm_big
from Profil import BMI
import requests
import csv

LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="CALORIES APP", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)
        image2 = Image.open("C:/Users/emilk/PycharmProjects/CaloriesCalendarGit/CaloriesCalendar/calculatorcalories.png")
        image1 = image2.resize((300, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image1)

        label2 = tk.Label(self, image=photo)
        label2.image = photo
        label2.grid(row=1,column=2,rowspan=6, columnspan=5)

        button1 = tk.Button(self, text="Calculator",command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)
        button2 = tk.Button(self, text="Calories",command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)
        button3 = tk.Button(self, text="History",command=lambda: controller.show_frame(Page3))
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
        button1.grid(row=0, column=1)

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

        wL = tk.Label(self, text="Sex: W/M")
        wL.grid(row=4, column=2)
        w = tk.Entry(self)
        w.grid(row=4,column=3)

        zL = tk.Label(self, text="Activity: small/medium/big")
        zL.grid(row=5, column=2)
        z=tk.Entry(self)
        z.grid(row=5,column=3)

        frame1 = tk.Frame(self)
        frame1.grid(row=8,column=2,columnspan=3,rowspan=2,padx=10,pady=10)

        cpm_output = tk.Label(frame1)
        cpm_output.grid(row=0, column=1)

        bmi_output = tk.Label(frame1)
        bmi_output.grid(row=1, column=1)

        def calculateCPM():
            try:
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
                cpm_output.config(width=5)
                cpm_output.config(bg="blue")
                cpm_output.config(text=int(cpm))
                a = tk.Label(frame1,text="YOUR CPM : ")
                a.grid(row=0, column=0)
            except:
                tk.messagebox.showinfo(title="Warning", message="Fill all informations")


        def calculateBMI():
            try:
                Heigh = float(heigh.get())
                Weight = float(weight.get())

                bmi = BMI(Weight,Heigh)
                bmi_output.config(width=5)
                bmi_output.config(text=int(bmi))

                b = tk.Label(frame1, text="YOUR BMI : ")
                b.grid(row=1, column=0)
                infoLabel = tk.Label(frame1,text="")
                infoLabel.grid(row=1,column=3)
                if bmi<18.5:
                    infoLabel.config(text="(underweight)")
                    bmi_output.config(bg="red")
                if bmi>18.5 and bmi<24.9:
                    infoLabel.config(text="(proper weight)")
                    bmi_output.config(bg="blue")
                if bmi>24.9:
                    infoLabel.config(text="(overweight)")
                    bmi_output.config(bg="red")
            except:
                tk.messagebox.showinfo(title="Warning", message="Fill all informations")


        button = tk.Button(self,bg="red", text="CALCULATE CPM", command=calculateCPM,heigh=1,width=13)
        button.grid(row=3,column=1)

        button2=tk.Button(self,bg="red", text="CALCULATE BMI", command=calculateBMI,heigh=1,width=13)
        button2.grid(row=4,column=1)



class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="TODAY", font=LARGEFONT)
        label.grid(row=0, column=3, padx=10, pady=10)
        # button to show frame 2 with text

        button2 = ttk.Button(self, text="MENU",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=0)

        sniadL = tk.Label(self,text="FOOD NAME")
        sniadL.grid (row=3,column=2)

        sniad = tk.Entry(self)
        sniad.grid(row=3, column=3,padx=2)
        sniadGL= tk.Label(self,text="gram")
        sniadGL.grid(row=3,column=5,padx=2)
        sniadG = tk.Entry(self)
        sniadG.grid(row=3, column=4,padx=2)



        wynikL = tk.Label(self, text = 0,font=("Courier", 20))
        wynikL.grid(row=10,column=4,ipadx=2)
        opisL = tk.Label(self,text="SUM KCAL",font=("Courier", 20))
        opisL.grid(row=10,column=3, ipadx=2)





        wronglabel = tk.Label(self)
        wronglabel.grid(row=6,column=3)
        def APIB():
            api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
            query = sniad.get()
            response = requests.get(api_url + query, headers={'X-Api-Key': '+K83QUc3yx5viW1/jBEWqw==YJ6E1gKifoWb4kZn'})
            if response.status_code == requests.codes.ok:
                try:
                     wronglabel.config(text="")
                     ab =  int(response.json()["items"][0]["calories"])/100*int(sniadG.get())
                     a= round(ab,1)
                     b = int(wynikL.cget("text")) + a
                     print(b)

                     wynikL.config(text=b)

                     file1 = open('history.csv', 'a')
                     file1.write(sniad.get() + ":" + str(a)+" kcal"+ ",")

                except:
                    wronglabel.config(text="This food is not in food base")

            else:
                wynikL.config(text="Connection with database is not avaialable in this moment")


        def remove():
            wynikL.config(text=0)

        def endDay():
            file1=open('history.csv','a')
            file1.write("\n")

            wynikL.config(text=0)

        def startDay():
            file1=open('history.csv','a')
            file1.write(str(datetime.date(datetime.now()))+"\n")


        button3 = tk.Button(self,bg = "red", text="ADD",command=APIB)
        button3.grid(row=7,column=3,ipadx=2,padx=10, pady=20)

        button4 = tk.Button(self, bg="red", text="REMOVE ALL", command=remove)
        #button4.grid(row=7, column=3,padx=2)

        button5 = tk.Button(self,bg='red',text='END DAY',command=endDay)
        button5.grid(row=7,column=4,ipadx=2,padx=10, pady=20)

        button6=tk.Button(self,bg='red',text="START DAY",command=startDay)
        button6.grid(row=7, column=2,padx=10, pady=20)

class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="HISTORY", font=LARGEFONT)
        label.grid(row=0, column=3,pady=20,padx=20)
        button2 = ttk.Button(self, text="MENU",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=0,column=0,padx = 10, pady=10)

        frame1 = tk.LabelFrame(self)
        frame1.grid(row=2,column=4,columnspan=2,padx=10,pady=10)
        label1 = tk.Label(frame1,text="TODAY",bg='red')
        label1.grid(row=0,column=0)

        try:
            with open('history.csv', newline='') as f:
                csv_reader = csv.reader(f)
                date = next(csv_reader)
                today = next(csv_reader)
                yesterday_date=next(csv_reader)
                yesterday = next(csv_reader)
                twodayago_date=next(csv_reader)
                twodaysago = next (csv_reader)
        except:
            pass

        splitted1 = str(today).split(',')

        splitted2 = str(yesterday).split(',')

        splitted3 = str(twodaysago).split(',')


        #Today=splitted1[0]+'\n'+splitted1[1]+'\n'+splitted1[2]
        Today = today[0]+'\n'+today[1]+'\n'+today[2]
        print(Today)

        #Yesterday = splitted2[0]+'\n'+splitted2[1]+'\n'+splitted2[2]
        Yesterday = yesterday[0]+'\n'+yesterday[1]+'\n'+yesterday[2]

       # TwoDaysAgo = splitted3[0]+'\n'+splitted3[1]+'\n'+splitted3[2]
        TwoDaysAgo = twodaysago[0]+'\n'+twodaysago[1]+'\n'+twodaysago[2]



        labelT=tk.Label(frame1,text=Today)
        labelT.grid(row=1,column=0)

        frame2 = tk.LabelFrame(self)
        frame2.grid(row=2, column=2, columnspan=2)
        label2 = tk.Label(frame2,text='YESTERDAY',bg='red')
        label2.grid(row=0,column=0,columnspan=2)
        labelY = tk.Label(frame2, text=Yesterday)
        labelY.grid(row=1, column=0)

        frame3 = tk.LabelFrame(self)
        frame3.grid(row=2, column=0,padx=10,pady=10)
        label3 = tk.Label(frame3,text='2 DAYS AGO',bg='red')
        label3.grid(row=0,column=0,columnspan=2)

        labelTW = tk.Label(frame3, text=TwoDaysAgo)
        labelTW.grid(row=1, column=0)

        def Show():
            newWindow = tk.Toplevel(self)
            newWindow.title("All history")
            newWindow.geometry("500x300")
            text = tk.Text(newWindow)
            text.grid(pady=10, padx=10)
            txt_file = open("history.csv", "r")
            text.insert(INSERT, txt_file.read())



        showButton = tk.Button(self,text="EXPORT HISTORY TO CSV",command=Show)
        showButton.grid(column=3,row=5,padx=20,pady=20)


# Driver Code
app = tkinterApp()
app.mainloop()
