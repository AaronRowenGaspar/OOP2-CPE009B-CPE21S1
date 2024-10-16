import tkinter as tk
from tkinter import messagebox

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Registration")
        self.root.geometry("400x400+500+200")

        # Program title
        self.title_label = tk.Label(root, text="Account Registration System", font=("Impact", 23), bg="Grey", fg="#0dc625")
        self.title_label.place(x=20, y=20)

        # Labels and Entry fields
        self.labels = ["First Name", "Last Name", "Username", "Password", "Email Address", "Contact Number"]
        self.entries = {}
        y_position = 65

        for label in self.labels:
            tk.Label(root, text=label, bg="Grey", fg="#0dc625", font=("Times New Roman bold", 11)).place(x=50, y=y_position)
            entry = tk.Entry(root)
            entry.place(x=200, y=y_position)
            self.entries[label] = entry
            y_position += 45
            

        # Submit and Clear buttons
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.place(x=100, y=y_position)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear)
        self.clear_button.place(x=250, y=y_position)
        
        root.config(bg="Grey")

    def submit(self):
        # Collect data from entries
        data = {label: entry.get() for label, entry in self.entries.items()}
        # Display the collected data (for demonstration purposes)
        messagebox.showinfo("Submitted Data", str(data))

    def clear(self):
        # Clear all entries
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()

