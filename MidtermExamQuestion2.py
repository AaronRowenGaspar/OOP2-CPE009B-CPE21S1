from tkinter import*

class ChangeColor:
    def __init__(self, win):
        self.button = Button(win, fg='Black', text='Click to Change Color', command=self.ColorChange)
        self.button.place(x=140, y=160)

    def ColorChange(self):
        self.button.config(bg='Yellow')

if __name__ == "__main__":
    window = Tk()
    app = ChangeColor(window)
    window.geometry("400x400+500+300")
    window.title("Special Midterm Exam in OOP")
    window.mainloop()
    

