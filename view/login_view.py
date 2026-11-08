from tkinter import *
from tkinter import messagebox


def login_click(event_info=None):
    if username.get() == "admin" and password.get() == "admin":
        password.set("")
        win.withdraw()
        import view.menu_view
    else:
        messagebox.showerror("Login Error", "Username or Password is Wrong !!!")


win = Tk()
win.geometry("300x180")
win.title("Bank Application - Login")

# Username
username = StringVar()
Label(win, text="Username").place(x=30, y=30)
Entry(win, textvariable=username).place(x=110, y=30)

# Password
password = StringVar()
Label(win, text="Password").place(x=30, y=70)
Entry(win, textvariable=password, show="*").place(x=110, y=70)

Button(win, text="Login", width=10, command=login_click).place(x=110, y=115)
win.bind("<Return>", login_click)

win.mainloop()
