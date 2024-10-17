from registration import Registration
import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    app = Registration(window)
    window.geometry("400x500+720+250")
    window.title("Account Registration System")
    window.mainloop()