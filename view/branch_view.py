from controller.branch_controller import BranchController
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from view import menu_view

controller = BranchController()
branch_list = []


def show_data_on_table(branches=None):
    if branches is None:
        success, branches = controller.get_all()
    else:
        success = True

    if success:
        branch_list.clear()
        branch_list.extend(branches)
        for item in table.get_children():
            table.delete(item)

        for branch in branches:
            table.insert("", END, values=branch.to_tuple())


def reset_form():
    branch_id.set("")
    name.set("")
    address.set("")
    phone.set("")
    city.set("")
    show_data_on_table()


def save_click():
    success, message = controller.save(branch_id.get(), name.get(), address.get(), phone.get(), city.get())
    if success:
        messagebox.showinfo("Branch Save", message)
        reset_form()
    else:
        messagebox.showerror("Branch Save Error", message)


def edit_click():
    success, message = controller.edit(branch_id.get(), name.get(), address.get(), phone.get(), city.get())
    if success:
        messagebox.showinfo("Branch Edit", message)
        reset_form()
    else:
        messagebox.showerror("Branch Edit Error", message)


def search_click():
    success, result = controller.get_by_name(name_search.get())
    if success:
        show_data_on_table(result)
    else:
        messagebox.showerror("Branch Search Error", result)


def select_branch(event_info):
    row_id = table.focus()
    if not row_id:
        return
    branch = branch_list[table.index(row_id)]
    branch_id.set(branch.branch_id)
    name.set(branch.name)
    address.set(branch.address)
    phone.set(branch.phone)
    city.set(branch.city)


def close_form():
    win.withdraw()
    menu_view.win.deiconify()


def show():
    reset_form()
    win.deiconify()


win = Tk()
win.geometry("830x330")
win.title("Bank Application - Branches")
win.wm_protocol("WM_DELETE_WINDOW", close_form)

# Branch Id
branch_id = StringVar()
Label(win, text="Branch Id").place(x=20, y=20)
Entry(win, textvariable=branch_id).place(x=100, y=20)

# Search By Name
name_search = StringVar()
Label(win, text="Search Name").place(x=290, y=20)
Entry(win, textvariable=name_search).place(x=380, y=20)
Button(win, text="Search", width=7, command=search_click).place(x=540, y=17)

# Name
name = StringVar()
Label(win, text="Name").place(x=20, y=60)
Entry(win, textvariable=name).place(x=100, y=60)

# Address
address = StringVar()
Label(win, text="Address").place(x=20, y=100)
Entry(win, textvariable=address).place(x=100, y=100)

# Phone
phone = StringVar()
Label(win, text="Phone").place(x=20, y=140)
Entry(win, textvariable=phone).place(x=100, y=140)

# City
city = StringVar()
Label(win, text="City").place(x=20, y=180)
Entry(win, textvariable=city).place(x=100, y=180)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=260)
Button(win, text="Edit", width=7, command=edit_click).place(x=87, y=260)

table = ttk.Treeview(
    win,
    columns=(1, 2, 3, 4, 5),
    show="headings",
)

table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Address")
table.heading(4, text="Phone")
table.heading(5, text="City")

table.column(1, width=60)
table.column(2, width=110)
table.column(3, width=120)
table.column(4, width=100)
table.column(5, width=80)

table.bind("<ButtonRelease>", select_branch)
table.place(x=290, y=60)

reset_form()
