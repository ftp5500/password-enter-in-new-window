import tkinter as tk
window = tk.Tk()

def checkPassword():
    password = "Orange"
    enteredpassword = passwordEntry.get()
    if password == enteredpassword:
        confirmLable.config(text = "Correct")
    else:
        confirmLable.config(text = "Incorrect")

passwordLable = tk.Label(window, text = "Password")
passwordEntry = tk.Entry(window, show = "*")

button = tk.Button(window, text = "Enter" , command = checkPassword)
confirmLable = tk.Label(window)

passwordLable.pack()
passwordEntry.pack()
button.pack()
confirmLable.pack()

window.mainloop()

