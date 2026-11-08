import importlib

from tkinter import *
from view import menu_view


def open_form(form_name):
    win.withdraw()
    form = importlib.import_module("view." + form_name)
    form.show()


def close_form():
    win.withdraw()
    menu_view.win.deiconify()


def show():
    win.deiconify()


win = Tk()
win.geometry("300x390")
win.title("Bank Application - Transactions")
win.wm_protocol("WM_DELETE_WINDOW", close_form)

Button(win, text="Transfer", width=25, height=2, command=lambda: open_form("transfer_view")).place(x=35, y=130)
Button(win, text="Deposit & Withdraw", width=25, height=2, command=lambda: open_form("deposit_withdraw_view")).place(x=35, y=205)
