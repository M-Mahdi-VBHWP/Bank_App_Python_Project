from controller.account_controller import AccountController
from controller.branch_controller import BranchController
from controller.user_controller import UserController
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view import menu_view

controller = AccountController()
user_controller = UserController()
branch_controller = BranchController()


def show_data_on_table(accounts=None):
    if accounts is None:
        success, accounts = controller.get_all()
    else:
        success = True

    if success:
        for item in table.get_children():
            table.delete(item)

        for account in accounts:
            table.insert("", END, values=account.to_tuple())


def show_users_on_table():
    success, users = user_controller.get_all()

    if success:
        for item in user_table.get_children():
            user_table.delete(item)

        for user in users:
            user_table.insert("", END, values=(user.user_id, user.national_code, user.name))


def show_branches_on_table():
    success, branches = branch_controller.get_all()

    if success:
        for item in branch_table.get_children():
            branch_table.delete(item)

        for branch in branches:
            branch_table.insert("", END, values=(branch.branch_id, branch.name, branch.address))


def reset_form():
    user_id.set("")
    branch_id.set("")
    account_id.set("")
    account_number.set("")
    amount.set("")
    show_data_on_table()
    show_users_on_table()
    show_branches_on_table()


def save_click():
    success, message = controller.save(user_id.get(), branch_id.get(), account_id.get(), account_number.get(), amount.get())
    if success:
        messagebox.showinfo("Account Save", message)
        reset_form()
    else:
        messagebox.showerror("Account Save Error", message)


def search_click():
    success, result = controller.get_by_number(number_search.get())
    if success:
        show_data_on_table(result)
    else:
        messagebox.showerror("Account Search Error", result)


def close_form():
    win.withdraw()
    menu_view.win.deiconify()


def show():
    reset_form()
    win.deiconify()


win = Tk()
win.geometry("940x400")
win.title("Bank Application - Accounts")
win.wm_protocol("WM_DELETE_WINDOW", close_form)

# User Id
user_id = StringVar()
Label(win, text="User Id").place(x=20, y=20)
Entry(win, textvariable=user_id).place(x=130, y=20)

# Branch Id
branch_id = StringVar()
Label(win, text="Branch Id").place(x=20, y=60)
Entry(win, textvariable=branch_id).place(x=130, y=60)

# Account Id
account_id = StringVar()
Label(win, text="Account Id").place(x=20, y=100)
Entry(win, textvariable=account_id).place(x=130, y=100)

# Account Number
account_number = StringVar()
Label(win, text="Account Number").place(x=20, y=140)
Entry(win, textvariable=account_number).place(x=130, y=140)

# Amount (first balance of the account)
amount = StringVar()
Label(win, text="Amount").place(x=20, y=180)
Entry(win, textvariable=amount).place(x=130, y=180)

Button(win, text="Create Account", width=14, command=save_click).place(x=20, y=240)

# Search By Account Number
number_search = StringVar()
Label(win, text="Search Number").place(x=330, y=20)
Entry(win, textvariable=number_search).place(x=440, y=20)
Button(win, text="Search", width=7, command=search_click).place(x=600, y=17)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5),
    show="headings",
    height=5,
)

table.heading(1, text="Id")
table.heading(2, text="Number")
table.heading(3, text="Balance")
table.heading(4, text="Status")
table.heading(5, text="Open Date")

table.column(1, width=70)
table.column(2, width=140)
table.column(3, width=130)
table.column(4, width=100)
table.column(5, width=140)

table.place(x=330, y=55)

# Users (only for help)
Label(win, text="Users").place(x=330, y=195)
user_table = ttk.Treeview(
    win,
    columns=(1, 2, 3),
    show="headings",
    height=5,
)

user_table.heading(1, text="Id")
user_table.heading(2, text="National Code")
user_table.heading(3, text="Name")

user_table.column(1, width=60)
user_table.column(2, width=100)
user_table.column(3, width=110)

user_table.place(x=330, y=215)

# Branches (only for help)
Label(win, text="Branches").place(x=620, y=195)
branch_table = ttk.Treeview(
    win,
    columns=(1, 2, 3),
    show="headings",
    height=5,
)

branch_table.heading(1, text="Id")
branch_table.heading(2, text="Name")
branch_table.heading(3, text="Address")

branch_table.column(1, width=60)
branch_table.column(2, width=110)
branch_table.column(3, width=120)

branch_table.place(x=620, y=215)

reset_form()
