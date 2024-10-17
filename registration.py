from tkinter import *
from tkinter import messagebox

class Registration:
    def __init__(self, win):
        self.Lbl1 = Label(win, fg="Green", bg="Dark Grey", text="Account Registration System", font=("Times New Roman", 22))
        self.Lbl1.place(x=30, y=30)

        self.Lbl2 = Label(win, text="First Name : ", bg="Dark Grey", font=("Times New Roman", 10), fg="Green")
        self.Lbl2.place(x=74, y=100)
        self.Entry1 = Entry(win, bd=3)
        self.Entry1.place(x=200, y=100)

        self.Lbl3 = Label(win, text="Surname : ", bg="Dark Grey", font=("Times New Roman", 10), fg="Green")
        self.Lbl3.place(x=74, y=140)
        self.Entry2 = Entry(win, bd=3)
        self.Entry2.place(x=200, y=140)

        self.Lbl4 = Label(win, text="Username : ", bg="Dark Grey", font=("Times New Roman", 10), fg="Green")
        self.Lbl4.place(x=74, y=180)
        self.Entry3 = Entry(win, bd=3)
        self.Entry3.place(x=200, y=180)

        self.Lbl5 = Label(win, text="Password : ", bg="Dark Grey", font=("Times New Roman", 10), fg="Green")
        self.Lbl5.place(x=74, y=220)
        self.Entry4 = Entry(win, bd=3, show="*")
        self.Entry4.place(x=200, y=220)

        self.Lbl6 = Label(win, text="Email : ", bg="Dark Grey", font=("Times New Roman", 10), fg="Green")
        self.Lbl6.place(x=74, y=260)
        self.Entry5 = Entry(win, bd=3)
        self.Entry5.place(x=200, y=260)

        self.Lbl7 = Label(win, text="Contact Number : ", bg="Dark Grey", font=("Times New Roman", 10), fg="Green")
        self.Lbl7.place(x=74, y=300)
        self.Entry6 = Entry(win, bd=3)
        self.Entry6.place(x=200, y=300)

        self.Button1 = Button(win, fg="Green", text="Submit", command=self.submit, bg="Light Grey", font=("Times New Roman bold", 12))
        self.Button1.place(x=120, y=350)
        self.Button2 = Button(win, fg="Green", text="Clear", command=self.clear, bg="Light Grey", font=("Times New Roman bold", 12))
        self.Button2.place(x=230, y=350)

        win.config(bg="Dark Grey")

    def submit(self):
        first_name = self.Entry1.get()
        surname = self.Entry2.get()
        username = self.Entry3.get()
        password = self.Entry4.get()
        email = self.Entry5.get()
        contact_number = self.Entry6.get()

        if all([first_name, surname, username, password, email, contact_number]):
            messagebox.showinfo("Submission Successful", "Registration Submitted Successfully!")
        else:
            messagebox.showwarning("Submission Failed", "Please fill in all fields")

    def clear(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry6.delete(0, END)


if __name__ == "__main__":
    window = Tk()
    app = Registration(window)
    window.geometry("400x500+720+250")
    window.title("Account Registration System")
    window.mainloop()
