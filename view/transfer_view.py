from controller.account_controller import AccountController
from controller.transaction_controller import TransactionController
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view import menu_view

controller = TransactionController()
account_controller = AccountController()


def show_data_on_table():
    success, result = controller.get_by_type(("transfer",))

    if success:
        for item in table.get_children():
            table.delete(item)

        for transaction in result:
            transaction_id, transaction_type, amount, date, account, to_account = transaction.to_tuple()
            table.insert("", END, values=(transaction_id, amount, date, account, to_account))


def show_accounts_on_table():
    success, accounts = account_controller.get_all()

    if success:
        for item in account_table.get_children():
            account_table.delete(item)

        for account in accounts:
            account_table.insert("", END, values=(account.account_id, account.account_number, f"{account.balance:.2f}"))


def reset_form():
    account_number.set("")
    to_account_number.set("")
    amount.set("")
    show_data_on_table()
    show_accounts_on_table()


def transfer_click():
    success, message = controller.transfer(account_number.get(), to_account_number.get(), amount.get())
    if success:
        messagebox.showinfo("Transfer", message)
        show_data_on_table()
        show_accounts_on_table()
    else:
        messagebox.showerror("Transfer Error", message)


def close_form():
    win.withdraw()
    menu_view.win.deiconify()


def show():
    reset_form()
    win.deiconify()


win = Tk()
win.geometry("890x400")
win.title("Bank Application - Transfer")
win.wm_protocol("WM_DELETE_WINDOW", close_form)

# Account Number
account_number = StringVar()
Label(win, text="Account").place(x=20, y=20)
Entry(win, textvariable=account_number).place(x=130, y=20)

# To Account Number
to_account_number = StringVar()
Label(win, text="To Account").place(x=20, y=60)
Entry(win, textvariable=to_account_number).place(x=130, y=60)

# Amount
amount = StringVar()
Label(win, text="Amount").place(x=20, y=100)
Entry(win, textvariable=amount).place(x=130, y=100)

Button(win, text="Transfer", width=8, command=transfer_click).place(x=20, y=160)

# Transactions (total width = 530)
table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5),
    show="headings",
    height=8,
)

table.heading(1, text="Id")
table.heading(2, text="Amount")
table.heading(3, text="Date")
table.heading(4, text="Account")
table.heading(5, text="To Account")

table.column(1, width=60)
table.column(2, width=90)
table.column(3, width=160)
table.column(4, width=110)
table.column(5, width=110)

table.place(x=330, y=20)

# Accounts (only for help, total width = 530, same as the table above)
Label(win, text="Accounts").place(x=330, y=215)
account_table = ttk.Treeview(
    win,
    columns=(1, 2, 3),
    show="headings",
    height=5,
)

account_table.heading(1, text="Id")
account_table.heading(2, text="Number")
account_table.heading(3, text="Balance")

account_table.column(1, width=130)
account_table.column(2, width=200)
account_table.column(3, width=200)

account_table.place(x=330, y=235)

reset_form()
