import tkinter as tk


def login_page():

    height = 400
    width = 350
    root = tk.Tk()
    canvas = tk.Canvas(root, height = height, width = width)
    canvas.pack()

    frame = tk.Frame(root, bg = "#C8D3D5")
    frame.place(relx = 0.2, rely = 0.15, relwidth  = 0.6, relheight = 0.5)

    login_label = tk.Label(frame, text = "Login: ")
    login_label.place(relx = 0.075, rely = 0.05)

    login_entry = tk.Entry(frame)
    login_entry.place(relx = 0.325, rely = 0.05)

    password_label = tk.Label(frame, text = "Password: ")
    password_label.place(relx = 0.075, rely = 0.225)

    password_entry = tk.Entry(frame)
    password_entry.config(show = "*")
    password_entry.place(relx = 0.425, rely = 0.225, relwidth = 0.485)

    login_button = tk.Button(frame, text = "Login", command = lambda:test(login_entry.get()))
    login_button.place(relx = 0.75, rely = 0.8)
    
    
    
    root.resizable(False, False)
    root.mainloop()

def test(content):
    print(content)

login_page()
