#João Pedro Rodrigues de Lima

from tkinter import *
from tkinter import messagebox
from math import sqrt

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.entry = Entry(self, font=("Palatino Linotype", 20), borderwidth = 1)
        self.entry.grid(row=0, column=0, columnspan=5)
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="slate gray", disabledforeground="slate gray")
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()

    def addChar(self, char, btn=None):
        self.entry.configure(state="normal", disabledbackground="slate gray", disabledforeground="black")
        if self.entry.get() == "ERRO!":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def clear(self):
        self.entry.configure(state="normal")
        if self.entry.get() != "ERRO!":
            text = self.entry.get()[:-1]
            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clearAll(self):
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def calculate(self):
        self.entry.configure(state="normal")
        newentry = self.entry.get()
        newentry = newentry.replace("√","sqrt")
        newentry = newentry.replace("×", "*")
        newentry = newentry.replace("²", "**2")
        newentry = newentry.replace("³", "**3")
        newentry = newentry.replace("^", "**")
        newentry = newentry.replace("÷", "/")
        newentry = newentry.replace("," , ".")
        newentry = newentry.replace("%", "/ 100")
        newentry = newentry.replace("mod", "%")
        newentry = newentry.replace("^", "**")

        try:
            ans = eval(newentry)
        except Exception as ex:

            messagebox.showinfo("Mensagem", "ERRO!")

        else:
            self.entry.delete(0,END)
            if len(str(ans)) > 20:
                self.entry.insert(0, '{:.10e}'.format(ans))
            else:
                self.entry.insert(0, ans)
        self.entry.configure(state = "disabled")

    def reset(self, btn):
        if btn != None:
            btn.config(bg = "slate gray")
            if btn == self.clearOneBtn:
                self.clear()
                self.master.after(100, lambda: btn.config(bg = "slate gray"))
            elif btn == self.equalBtn:
                self.master.after(100, lambda: btn.config(bg = "slate gray"))
                self.calculate()
            elif btn == self.clearAllBtn:
                self.clearAll()
                self.master.after(100, lambda: btn.config(bg = "slate gray"))
            else:
                self.master.after(100, lambda: btn.config(bg = "slate gray"))
        else:
            pass

    def bind_buttons(self, master):
        master.bind("<Return>", lambda event, btn=self.equalBtn: self.reset(btn))
        master.bind("<BackSpace>", lambda event, btn=self.clearOneBtn: self.reset(btn))
        master.bind("9", lambda event, char="9", btn=self.nineBtn: self.addChar(char, btn))
        master.bind("8", lambda event, char="8", btn=self.eightBtn: self.addChar(char, btn))
        master.bind("7", lambda event, char="7", btn=self.sevenBtn: self.addChar(char, btn))
        master.bind("6", lambda event, char="6", btn=self.sixBtn: self.addChar(char, btn))
        master.bind("5", lambda event, char="5", btn=self.fiveBtn: self.addChar(char, btn))
        master.bind("4", lambda event, char="4", btn=self.fourBtn: self.addChar(char, btn))
        master.bind("3", lambda event, char="3", btn=self.threeBtn: self.addChar(char, btn))
        master.bind("2", lambda event, char="2", btn=self.twoBtn: self.addChar(char, btn))
        master.bind("1", lambda event, char="1", btn=self.oneBtn: self.addChar(char, btn))
        master.bind("0", lambda event, char="0", btn=self.zeroBtn: self.addChar(char, btn))
        master.bind("*", lambda event, char="×", btn=self.timesBtn: self.addChar(char, btn))
        master.bind("/", lambda event, char="÷", btn=self.divBtn: self.addChar(char, btn))
        master.bind("p", lambda event, char="^", btn=self.powerBtn: self.addChar(char, btn))
        master.bind("m", lambda event, char=" mod ", btn=self.modBtn: self.addChar(char, btn))
        master.bind("%", lambda event, char="%", btn=self.pctBtn: self.addChar(char, btn))
        master.bind(",", lambda event, char=".", btn=self.commaBtn: self.addChar(char, btn))
        master.bind("-", lambda event, char="-", btn=self.minusBtn: self.addChar(char, btn))
        master.bind("+", lambda event, char="+", btn=self.plusBtn: self.addChar(char, btn))
        master.bind("s", lambda event, char="√(", btn=self.rootBtn: self.addChar(char, btn))
        master.bind("!", lambda event, char="!", btn=self.modBtn: self.addChar(char, btn))
        master.bind("(", lambda event, char="(", btn=self.leftparBtn: self.addChar(char, btn))
        master.bind(")", lambda event, char=")", btn=self.rightparBtn: self.addChar(char, btn))
        master.bind("c", lambda event, btn=self.clearAllBtn: self.reset(btn), self.clearAll)

    def create_widgets(self):

        #FIRST COLUMN

        self.pctBtn = Button(self, font = ("Palatino Linotype", 12), text="%", command=lambda: self.addChar('%'))
        self.pctBtn.grid(row=1, column=0, sticky = 'NWNESWSE')
        self.pctBtn["bg"] = "slate gray"
        self.pctBtn["fg"] = "white"

        self.rootBtn = Button(self, font = ("Palatino Linotype", 12), text="√", command=lambda: self.addChar('√('))
        self.rootBtn.grid(row=2, column=0, sticky = 'NWNESWSE')
        self.rootBtn["bg"] = "slate gray"
        self.rootBtn["fg"] = "white"

        self.sqrBtn = Button(self, font = ("Palatino Linotype", 12), text="x²", command=lambda: self.addChar('²'))
        self.sqrBtn.grid(row=3, column=0, sticky = 'NWNESWSE')
        self.sqrBtn["bg"] = "slate gray"
        self.sqrBtn["fg"] = "white"

        self.cubeBtn = Button(self, font = ("Palatino Linotype", 12), text="x³", command=lambda: self.addChar('³'))
        self.cubeBtn.grid(row=4, column=0, sticky = 'NWNESWSE')
        self.cubeBtn["bg"] = "slate gray"
        self.cubeBtn["fg"] = "white"

        self.modBtn = Button(self, font = ("Palatino Linotype", 12), text="mod", command=lambda: self.addChar(' mod '))
        self.modBtn.grid(row=5, column=0, sticky = 'NWNESWSE')
        self.modBtn["bg"] = "slate gray"
        self.modBtn["fg"] = "white"

        #SECOND COLUMN

        self.clearAllBtn = Button(self, font = ("Palatino Linotype", 12), text='C', command=lambda: self.clearAll())
        self.clearAllBtn.grid(row=1, column=1, columnspan = 2, sticky = 'NWNESWSE')
        self.clearAllBtn["bg"] = "slate gray"
        self.clearAllBtn["fg"] = "white"

        self.sevenBtn = Button(self, font = ("Palatino Linotype", 12), text="7", command=lambda: self.addChar(7))
        self.sevenBtn.grid(row=2, column=1, sticky = 'NWNESWSE')
        self.sevenBtn["bg"] = "snow4"
        self.sevenBtn["fg"] = "white"

        self.fourBtn = Button(self, font = ("Palatino Linotype", 12), text="4", command=lambda: self.addChar(4))
        self.fourBtn.grid(row=3, column=1, sticky = 'NWNESWSE')
        self.fourBtn["bg"] = "snow4"
        self.fourBtn["fg"] = "white"

        self.oneBtn = Button(self, font = ("Palatino Linotype", 12), text="1", command=lambda: self.addChar(1))
        self.oneBtn.grid(row=4, column=1, sticky = 'NWNESWSE')
        self.oneBtn["bg"] = "snow4"
        self.oneBtn["fg"] = "white"

        """
        self.factBtn = Button(self, font = ("Palatino Linotype", 12), text="n!", command=lambda: self.addChar('!'))
        self.factBtn.grid(row=5, column=1, sticky = 'NWNESWSE')
        self.factBtn["bg"] = "slate gray"
        self.factBtn["fg"] = "white"
        """

        #THIRD COLUMN

        self.eightBtn = Button(self, font = ("Palatino Linotype", 12), text="8", command=lambda: self.addChar(8))
        self.eightBtn.grid(row=2, column=2, sticky = 'NWNESWSE')
        self.eightBtn["bg"] = "snow4"
        self.eightBtn["fg"] = "white"

        self.fiveBtn = Button(self, font = ("Palatino Linotype", 12), text="5", command=lambda: self.addChar(5))
        self.fiveBtn.grid(row=3, column=2, sticky = 'NWNESWSE')
        self.fiveBtn["bg"] = "snow4"
        self.fiveBtn["fg"] = "white"

        self.twoBtn = Button(self, font = ("Palatino Linotype", 12), text="2", command=lambda: self.addChar(2))
        self.twoBtn.grid(row=4, column=2, sticky = 'NWNESWSE')
        self.twoBtn["bg"] = "snow4"
        self.twoBtn["fg"] = "white"

        self.zeroBtn = Button(self, font = ("Palatino Linotype", 12), text="0", command=lambda: self.addChar(0))
        self.zeroBtn.grid(row=5, column=2, sticky = 'NWNESWSE')
        self.zeroBtn["bg"] = "snow4"
        self.zeroBtn["fg"] = "white"

        #FOURTH COLUMN

        self.nineBtn = Button(self, font = ("Palatino Linotype", 12), text="9", command=lambda: self.addChar(9))
        self.nineBtn.grid(row=2, column=3, sticky = 'NWNESWSE')
        self.nineBtn["bg"] = "snow4"
        self.nineBtn["fg"] = "white"

        self.sixBtn = Button(self, font = ("Palatino Linotype", 12), text="6", command=lambda: self.addChar(6))
        self.sixBtn.grid(row=3, column=3, sticky = 'NWNESWSE')
        self.sixBtn["bg"] = "snow4"
        self.sixBtn["fg"] = "white"


        self.threeBtn = Button(self, font = ("Palatino Linotype", 12), text="3", command=lambda: self.addChar(3))
        self.threeBtn.grid(row=4, column=3, sticky = 'NWNESWSE')
        self.threeBtn["bg"] = "snow4"
        self.threeBtn["fg"] = "white"

        self.commaBtn = Button(self, font = ("Palatino Linotype", 12), text=",", command=lambda: self.addChar("."))
        self.commaBtn.grid(row=5, column=4, sticky = 'NWNESWSE')
        self.commaBtn["bg"] = "slate gray"
        self.commaBtn["fg"] = "white"

        #FIFTH COLUMN

        self.divBtn = Button(self, font = ("Palatino Linotype", 14), text="÷", command=lambda: self.addChar('÷'))
        self.divBtn.grid(row=1, column=4, sticky = 'NWNESWSE')
        self.divBtn["bg"] = "slate gray"
        self.divBtn["fg"] = "white"

        self.timesBtn = Button(self, font = ("Palatino Linotype", 14), text="×", command=lambda: self.addChar('×'))
        self.timesBtn.grid(row=2, column=4, sticky = 'NWNESWSE')
        self.timesBtn["bg"] = "slate gray"
        self.timesBtn["fg"] = "white"

        self.minusBtn = Button(self, font = ("Palatino Linotype", 14), text="-", command=lambda: self.addChar('-'))
        self.minusBtn.grid(row=3, column=4, sticky = 'NWNESWSE')
        self.minusBtn["bg"] = "slate gray"
        self.minusBtn["fg"] = "white"

        self.plusBtn = Button(self, font = ("Palatino Linotype", 14), text="+", command=lambda: self.addChar('+'))
        self.plusBtn.grid(row=4, column=4, sticky = 'NWNESWSE')
        self.plusBtn["bg"] = "slate gray"
        self.plusBtn["fg"] = "white"

        self.equalBtn = Button(self, font = ("Palatino Linotype", 14), text="=", command=lambda: self.calculate())
        self.equalBtn.grid(row = 6, column = 0, columnspan = 5, sticky = 'NWNESWSE')
        self.equalBtn["bg"] = "slate gray"
        self.equalBtn["fg"] = "white"

        #EXTRA

        self.clearOneBtn = Button(self, font = ("Palatino Linotype", 10), text='←', command=lambda: self.clear())
        self.clearOneBtn.grid(row=1, column=3, sticky = 'NWNESWSE' )
        self.clearOneBtn["bg"] = "slate gray"
        self.clearOneBtn["fg"] = "white"

        self.leftparBtn = Button(self, font = ("Palatino Linotype", 12), text="(", command=lambda: self.addChar('('))
        self.leftparBtn.grid(row=5, column=1, sticky = 'NWNESWSE')
        self.leftparBtn["bg"] = "slate gray"
        self.leftparBtn["fg"] = "white"

        self.rightparBtn = Button(self, font = ("Palatino Linotype", 12), text=")", command=lambda: self.addChar(')'))
        self.rightparBtn.grid(row=5, column=3, sticky = 'NWNESWSE')
        self.rightparBtn["bg"] = "slate gray"
        self.rightparBtn["fg"] = "white"

        self.powerBtn = Button(self, font = ("Palatino Linotype", 12), text="^", command=lambda: self.addChar('^'))
        #self.cubeBtn.grid(row=4, column=0, sticky = 'NWNESWSE')

root = Tk()
root.title("Calculadora")
root.resizable(0,0)
app = Application(root)
root.mainloop()
