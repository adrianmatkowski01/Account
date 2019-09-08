import tkinter as tk
import account


def login():
    account.login_variable(login_entry.get())

def password():
    account.password_variable(password_entry.get())

def register_login():
    account.register_login_variable(login_register_entry.get())

def register_password():
    account.register_password_variable(password_register_entry.get())

def register_repassword():
    account.register_repassword_variable(repassword_register_entry.get())

height = 400
width = 800
root = tk.Tk()
root.title("Account")
canvas = tk.Canvas(root, height = height, width = width)
canvas.pack()

canvas_login_label = tk.Label(canvas, text = "LOGIN", font = 15)
canvas_login_label.place(relx = 0.3, rely = 0.05)

canvas_register_label = tk.Label(canvas, text = "REGISTER", font = 15)
canvas_register_label.place(relx = 0.7, rely = 0.05)

frame = tk.Frame(root, bg = "#C8D3D5")
frame.place(relx = 0.1, rely = 0.125, relwidth  = 0.8, relheight = 0.75)

login_label = tk.Label(frame, text = "Login: ")
login_label.place(relx = 0.075, rely = 0.075)

login_entry = tk.Entry(frame)
login_entry.place(relx = 0.2, rely = 0.075, relwidth = 0.2)

password_label = tk.Label(frame, text = "Password: ")
password_label.place(relx = 0.075, rely = 0.2)

password_entry = tk.Entry(frame)
password_entry.config(show = "*")
password_entry.place(relx = 0.2, rely = 0.2, relwidth = 0.2)

login_button = tk.Button(frame, text = "Login", command = lambda: [login(), password(), account.login(), label_text.set(label_text_variable)])
login_button.place(relx = 0.335, rely = 0.325)

login_register_label = tk.Label(frame, text = "Login: ")
login_register_label.place(relx = 0.6, rely = 0.075)

login_register_entry = tk.Entry(frame)
login_register_entry.place(relx = 0.725, rely = 0.075, relwidth = 0.2)

password_register_label = tk.Label(frame, text = "Password: ")
password_register_label.place(relx = 0.6, rely = 0.2)

password_register_entry = tk.Entry(frame)
password_register_entry.config(show = "*")
password_register_entry.place(relx = 0.725, rely = 0.2, relwidth = 0.2)

repassword_register_label = tk.Label(frame, text = "Confirm Password: ")
repassword_register_label.place(relx = 0.6, rely = 0.325)

repassword_register_entry = tk.Entry(frame)
repassword_register_entry.config(show = "*")
repassword_register_entry.place(relx = 0.8, rely = 0.325, relwidth = 0.125)

register_button = tk.Button(frame, text = "Register", command = lambda: [register_login(),
                                                                        register_password(), 
                                                                        register_repassword(),
                                                                        account.register(),
                                                                        label_text.set(label_text_variable)])
register_button.place(relx = 0.845, rely = 0.45)

label_text_variable = None
label_text = tk.StringVar(root)
text_label = tk.Label(frame, textvariable=label_text)
text_label.place(relx = 0.1, rely = 0.6, relheight = 0.275, relwidth = 0.8)

root.resizable(False, False)
root.mainloop()