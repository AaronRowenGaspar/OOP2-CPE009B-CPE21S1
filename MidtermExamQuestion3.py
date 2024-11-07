from tkinter import*

class Fullname:
    def __init__(self, win):
        
        self.lbl = Label(win, fg='Red', text='Enter your fullname:')
        self.lbl.place(x=60, y=80)
        self.entry1 = Entry(win, bd=4, font='Arial, 15')
        self.entry1.place(x=250, y=80)
        
        self.bttn = Button(win, fg='Red', text='Click to display your fullname', command=self.display)
        self.bttn.place(x=60, y=150)
        self.entry2 = Entry(win, bd=4, font='Arial, 15')
        self.entry2.place(x=250, y=150)
    
    
    def display(self):
        fullname = str(self.entry1.get())
        self.entry2.insert(END, str(fullname))
        
if __name__ == "__main__":
    window = Tk()
    app = Fullname(window)
    window.geometry("500x250+500+300")
    window.title("Midterm in OOP")
    window.mainloop()

