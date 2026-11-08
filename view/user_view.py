from controller.user_controller import UserController
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view import menu_view

controller = UserController()
user_list = []


def show_data_on_table(users=None):
    if users is None:
        success, users = controller.get_all()
    else:
        success = True

    if success:
        user_list.clear()
        user_list.extend(users)
        for item in table.get_children():
            table.delete(item)

        for user in users:
            table.insert("", END, values=user.to_tuple())


def reset_form():
    user_id.set("")
    national_code.set("")
    name.set("")
    phone.set("")
    address.set("")
    password.set("")
    show_data_on_table()


def save_click():
    success, message = controller.save(user_id.get(), national_code.get(), name.get(), phone.get(), address.get(), password.get())
    if success:
        messagebox.showinfo("User Save", message)
        reset_form()
    else:
        messagebox.showerror("User Save Error", message)


def edit_click():
    success, message = controller.edit(user_id.get(), national_code.get(), name.get(), phone.get(), address.get())
    if success:
        messagebox.showinfo("User Edit", message)
        reset_form()
    else:
        messagebox.showerror("User Edit Error", message)


def delete_click():
    success, message = controller.delete(user_id.get())
    if success:
        messagebox.showinfo("User Delete", message)
        reset_form()
    else:
        messagebox.showerror("User Delete Error", message)


def login_click():
    success, message = controller.login(user_id.get(), password.get())
    if success:
        messagebox.showinfo("User Login", message)
    else:
        messagebox.showerror("User Login Error", message)


def search_click():
    success, result = controller.get_by_name(name_search.get())
    if success:
        show_data_on_table(result)
    else:
        messagebox.showerror("User Search Error", result)


def select_user(event_info):
    row_id = table.focus()
    if not row_id:
        return
    user = user_list[table.index(row_id)]
    user_id.set(user.user_id)
    national_code.set(user.national_code)
    name.set(user.name)
    phone.set(user.phone)
    address.set(user.address)
    password.set("")


def close_form():
    win.withdraw()
    menu_view.win.deiconify()


def show():
    reset_form()
    win.deiconify()


win = Tk()
win.geometry("860x330")
win.title("Bank Application - Users")
win.wm_protocol("WM_DELETE_WINDOW", close_form)

# User Id
user_id = StringVar()
Label(win, text="User Id").place(x=20, y=20)
Entry(win, textvariable=user_id).place(x=120, y=20)

# Search By Name
name_search = StringVar()
Label(win, text="Search Name").place(x=330, y=20)
Entry(win, textvariable=name_search).place(x=420, y=20)
Button(win, text="Search", width=7, command=search_click).place(x=580, y=17)

# National Code
national_code = StringVar()
Label(win, text="National Code").place(x=20, y=60)
Entry(win, textvariable=national_code).place(x=120, y=60)

# Name
name = StringVar()
Label(win, text="Name").place(x=20, y=100)
Entry(win, textvariable=name).place(x=120, y=100)

# Phone
phone = StringVar()
Label(win, text="Phone").place(x=20, y=140)
Entry(win, textvariable=phone).place(x=120, y=140)

# Address
address = StringVar()
Label(win, text="Address").place(x=20, y=180)
Entry(win, textvariable=address).place(x=120, y=180)

# Password
password = StringVar()
Label(win, text="Password").place(x=20, y=220)
Entry(win, textvariable=password, show="*").place(x=120, y=220)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=280)
Button(win, text="Edit", width=7, command=edit_click).place(x=87, y=280)
Button(win, text="Delete", width=7, command=delete_click).place(x=154, y=280)
Button(win, text="Login", width=7, command=login_click).place(x=221, y=280)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5),
    show="headings",
)

table.heading(1, text="Id")
table.heading(2, text="National Code")
table.heading(3, text="Name")
table.heading(4, text="Phone")
table.heading(5, text="Address")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=110)
table.column(4, width=100)
table.column(5, width=130)

table.bind("<ButtonRelease>", select_user)
table.place(x=330, y=60)

reset_form()
