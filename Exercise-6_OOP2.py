from tkinter import*

class MyWindow:
    def __init__(self, win):

        self.Lbl1 = Label(win, fg="Black", bg="#ff66cc", text="Simple Calculator", font=("Arial", 30))
        self.Lbl1.place(x=25, y=30)

        self.Lbl2 = Label(win, text="Number 1 : ", bg="#ff66cc", font=("Arial", 10))
        self.Lbl2.place(x=60, y=100)
        self.Entry1 = Entry(win, bd=3)
        self.Entry1.place(x=140, y=100)

        self.Lbl3 = Label(win, text="Number 2 : ", bg="#ff66cc", font=("Arial", 10))
        self.Lbl3.place(x=60, y=140)
        self.Entry2 = Entry(win, bd=3)
        self.Entry2.place(x=140, y=140)

        self.Lbl4 = Label(win, text="Answer : ", bg="#ff66cc", font=("Arial", 10))
        self.Lbl4.place(x=74, y=180)
        self.Entry3 = Entry(win, bd=3)
        self.Entry3.place(x=140, y=180)

        self.Button1 = Button(win, fg="Black", text="Add", command=self.add, bg="#ffff00")
        self.Button1.place(x=50, y=240)

        self.Button2 = Button(win, fg="Black", text="Subtract", command=self.sub, bg="#ffff00")
        self.Button2.place(x=100, y=240)

        self.Button2 = Button(win, fg="Black", text="Multiply", command=self.mul, bg="#ffff00")
        self.Button2.place(x=175, y=240)

        self.Button2 = Button(win, fg="Black", text="Divide", command=self.div, bg="#ffff00")
        self.Button2.place(x=250, y=240)

        win.config(bg="#ff66cc")


    def add(self):
        self.Entry3.delete(0, 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 + num2
        self.Entry3.insert(END, str(result))

    def sub(self):
        self.Entry3.delete(0, 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 - num2
        self.Entry3.insert(END, str(result))

    def mul(self):
        self.Entry3.delete(0, 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 * num2
        self.Entry3.insert(END, str(result))

    def div(self):
        self.Entry3.delete(0, 'end')
        num1 = float(self.Entry1.get())
        num2 = float(self.Entry2.get())
        result = num1 / num2
        self.Entry3.insert(END, str(result))



window = Tk()
MyWin = MyWindow(window)
window.geometry("360x360+720+250")
window.title("Simple Calculator")
window.mainloop()