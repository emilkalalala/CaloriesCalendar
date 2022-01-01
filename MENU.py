import tkinter as tk
from datetime import date, datetime, timedelta
from tkinter import StringVar, ttk
from tkinter import Canvas, INSERT
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import font as tkfont

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
        image2 = Image.open("calculatorcalories.png")
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
        
        self.hints_list = set()
        self.get_hints_list()
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="TODAY", font=LARGEFONT)
        label.grid(row=0, column=3, padx=10, pady=10)
        # button to show frame 2 with text

        button2 = ttk.Button(self, text="MENU",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=0, column=0)

        self.sniadL = tk.Label(self,text="FOOD NAME")
        self.sniadL.grid (row=3,column=2)

        sv = StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.text_inputed())

        self.sniad = tk.Entry(self, textvariable=sv)
        self.sniad.grid(row=3, column=3,padx=2)

        

        self.previous_list = tk.Listbox(self,height=3)
        self.previous_list.grid(row=4, column=3, sticky="n")
        self.previous_list.grid_forget()

        sniadGL= tk.Label(self,text="gram")
        sniadGL.grid(row=3,column=5,padx=2)
        self.sniadG = tk.Entry(self)
        self.sniadG.grid(row=3, column=4,padx=2)
        self.wynikL = tk.Label(self, text = 0,font=("Courier", 20))
        self.wynikL.grid(row=10,column=4,ipadx=2)
        opisL = tk.Label(self,text="SUM KCAL",font=("Courier", 20))
        opisL.grid(row=10,column=3, ipadx=2)
        self.wronglabel = tk.Label(self)
        self.wronglabel.grid(row=6,column=3)
        button3 = tk.Button(self,bg = "red", text="ADD",command=self.APIB)
        button3.grid(row=7,column=3,ipadx=2,padx=10, pady=20)

        #button4 = tk.Button(self, bg="red", text="REMOVE ALL", command=remove)
        self.calculate_calories()

    def get_hints_list(self):
        with open("hints", "r") as file:
            lines = file.readlines()
            for line in lines:
                self.hints_list.add(line)
        


    def text_inputed(self):
        self.previous_list.delete(0, tk.END)
        if len(self.sniad.get()) > 0:
            self.previous_list.grid_configure(row=4, column=3, sticky="n")
            hints = []
            for hint in self.hints_list:
                if hint.startswith(self.sniad.get()):
                    hints.append(hint)
            hints.sort()
            for i, hint in enumerate(hints):
                self.previous_list.insert(i, hint)
        else:
            self.previous_list.grid_forget()


    def calculate_calories(self):
        calories = float(0)
        with open("history.csv", "r", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                print("emilka")
                print(str(datetime.date(datetime.now())))
                print(row[0])
                if row[0] == str(datetime.date(datetime.now())):
                    print("EMILKKOWE DODAWNIAWE")
                    calories += float(row[2])
        calories = round(calories, 1)
        self.wynikL.config(text=calories)


    def APIB(self):
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        query = self.sniad.get()
        response = requests.get(api_url + query, headers={'X-Api-Key': '+K83QUc3yx5viW1/jBEWqw==YJ6E1gKifoWb4kZn'})
        if response.status_code == requests.codes.ok:
            try:
                self.wronglabel.config(text="")
                ab =  int(response.json()["items"][0]["calories"])/100*int(self.sniadG.get())
                a= round(ab, 1)
                print("TEST JEDEN")
                with open('history.csv', 'a', newline="") as file:
                    print("TEST JEDEN i jedna czwarta")
                    spamwriter = csv.writer(file, delimiter=";", quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    print("TEST JEDEN i pol")
                    spamwriter.writerow([str(datetime.date(datetime.now())), self.sniad.get(), str(a)])
                print("TEST DWA")
                self.calculate_calories()
                self.save_to_history(self.sniad.get())
                self.get_hints_list()
            except Exception as e:
                print(e.args)
                self.wronglabel.config(text="This food is not in food base")

        else:
            self.wynikL.config(text="Connection with database is not avaialable in this moment")


    def save_to_history(self, food):
        with open("hints", "a") as file:
            file.write(food + "\n")

    def remove():
        wynikL.config(text=0)
        #button4.grid(row=7, column=3,padx=2)


class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="HISTORY", font=LARGEFONT)
        appHighlightFont = tkfont.Font(family='Helvetica', size=10, weight='bold')
        label.grid(row=0, column=3,pady=20,padx=20)
        button2 = ttk.Button(self, text="MENU",
                             command=lambda: controller.show_frame(StartPage))
        button2.grid(row=0,column=0,padx = 10, pady=10)

        Today = ""
        TodayKcal = 0

        Yesterday = ""
        YesterdayKcal = 0

        TwoDaysAgo = ""
        TwoDaysAgoKcal = 0

        with open("history.csv", "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                if row[0] == str(date.today()):
                    Today += row[1] + ": " + row[2] + "\n"
                    TodayKcal += float(row[2])
                elif row[0] == str(date.today() - timedelta(days = 1)):
                    Yesterday += row[1] + ": " + row[2] + "\n"
                    YesterdayKcal += float(row[2])
                elif row[0] == str(date.today() - timedelta(days = 2)):
                    TwoDaysAgo += row[1] + ": " + row[2] + "\n"
                    TwoDaysAgoKcal += float(row[2])

        frame1 = tk.LabelFrame(self, width=15, heigh=25)
        frame1.grid(row=2, column=4, columnspan=2, padx=10, pady=10)
        label1 = tk.Label(frame1, text="TODAY", bg='red')
        label1.grid(row=0, column=0)
        labelT=tk.Label(frame1,text=Today)
        labelT.grid(row=1,column=0)
        sum1=tk.Label(frame1,text="SUM KCAL : "+str(TodayKcal), font=appHighlightFont)
        sum1.grid( sticky="S")

        frame2 = tk.LabelFrame(self,width=15,heigh=25)
        frame2.grid(row=2, column=2, columnspan=2)
        label2 = tk.Label(frame2,text='YESTERDAY',bg='red')
        label2.grid(row=0,column=0,columnspan=2)
        labelY = tk.Label(frame2, text=Yesterday)
        labelY.grid(row=1, column=0)
        sum2 = tk.Label(frame2, text="SUM KCAL : " + str(YesterdayKcal), font=appHighlightFont)
        sum2.grid(sticky="S")

        frame3 = tk.LabelFrame(self,width=15,heigh=25)
        frame3.grid(row=2, column=0,padx=10,pady=10)
        label3 = tk.Label(frame3,text='2 DAYS AGO',bg='red')
        label3.grid(row=0,column=0,columnspan=2)

        labelTW = tk.Label(frame3, text=TwoDaysAgo)
        labelTW.grid(row=1, column=0)
        sum3 = tk.Label(frame3, text="SUM KCAL : " + str(TwoDaysAgoKcal), font=appHighlightFont)
        sum3.grid(sticky="S")


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
