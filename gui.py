import tkinter as tk



height = 400
width = 800
root = tk.Tk()
root.title("Login")
canvas = tk.Canvas(root, height = height, width = width)
canvas.pack()

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

login_button = tk.Button(frame, text = "Login", command = lambda: login(login_entry.get()) +
                                                                    password(password_entry.get()))
login_button.place(relx = 0.335, rely = 0.325)

# register_label = tk.Label(frame, text = "Don't have an account yet?", bg = "#C8D3D5")
# register_label.place(relx = 0.075, rely = 0.65)

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

register_button = tk.Button(frame, text = "Register", command = lambda: register_login(login_register_entry.get()) +
                                                                        register_password(password_register_entry.get()) + 
                                                                        register_repassword(repassword_register_entry.get()))
register_button.place(relx = 0.845, rely = 0.45)

text_label = tk.Label(frame)
text_label.place(relx = 0.1, rely = 0.6, relheight = 0.275, relwidth = 0.8)
text_label["text"] = "test"
root.resizable(False, False)
root.mainloop()



def login(log_in):
    func(log_in)
    return log_in

def password(password):
    return password

def register_login(login):
    return login

def register_password(password):
    return password

def register_repassword(repassword):
    return repassword

def func(asd):
    asd + None

# screen()
