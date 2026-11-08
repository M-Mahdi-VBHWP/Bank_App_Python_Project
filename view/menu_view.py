import importlib

from tkinter import *
from tkinter import messagebox


def open_form(form_name):
    win.withdraw()
    form = importlib.import_module("view." + form_name)
    form.show()


def about_click():
    messagebox.showinfo("Bank Application", "Programmer : Mohammad Mahdi Soleimani")


def close_app():
    if messagebox.askyesno("Bank Application", "Are you sure you want to exit?"):
        win.master.destroy()


win = Toplevel()
win.geometry("300x390")
win.title("Bank Application")
win.wm_protocol("WM_DELETE_WINDOW", close_app)

Label(win, text="Bank Application", font=("Arial", 14, "bold")).place(x=70, y=15)

Button(win, text="Branches", width=25, height=2, command=lambda: open_form("branch_view")).place(x=35, y=60)
Button(win, text="Users", width=25, height=2, command=lambda: open_form("user_view")).place(x=35, y=125)
Button(win, text="Accounts", width=25, height=2, command=lambda: open_form("account_view")).place(x=35, y=190)
Button(win, text="Transactions", width=25, height=2, command=lambda: open_form("transaction_view")).place(x=35, y=255)
Button(win, text="About", width=25, height=2, command=about_click).place(x=35, y=320)
