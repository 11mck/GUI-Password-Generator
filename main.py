from tkinter import *
from tkinter import ttk


def password_generator(length, strength):
    from random import randint, shuffle
    pasword = []
    char = [[65, 90], [97, 122]]
    nums = [[48, 57]]
    special = [[33, 47], [58, 64], [91, 96], [123, 126]]
    part_of_passwords = [char, nums, special]
    if strength == 0:
        for i in range(length):
            x = part_of_passwords[0][randint(0, len(part_of_passwords[0]) - 1)]
            pasword.append(chr(randint(x[0], x[1])))
    elif strength == 1:
        x, y = part_of_passwords[0][randint(0, len(part_of_passwords[0]) - 1)], part_of_passwords[1][
            randint(0, len(part_of_passwords[1]) - 1)]
        pasword.append(chr(randint(x[0], x[1])))
        pasword.append(chr(randint(y[0], y[1])))
        for i in range(length - 2):
            which_part = randint(0, 1)
            x = part_of_passwords[which_part][randint(0, len(part_of_passwords[which_part]) - 1)]
            pasword.append(chr(randint(x[0], x[1])))
    else:
        x, y, z = part_of_passwords[0][randint(0, len(part_of_passwords[0]) - 1)], part_of_passwords[1][
            randint(0, len(part_of_passwords[1]) - 1)], part_of_passwords[2][randint(0, len(part_of_passwords[2]) - 1)]
        pasword.append(chr(randint(x[0], x[1])))
        pasword.append(chr(randint(y[0], y[1])))
        pasword.append(chr(randint(z[0], z[1])))
        for i in range(length - 3):
            which_part = randint(0, 2)
            x = part_of_passwords[which_part][randint(0, len(part_of_passwords[which_part]) - 1)]
            pasword.append(chr(randint(x[0], x[1])))

    shuffle(pasword)
    password = ''.join(pasword)
    return password


root = Tk()
root.title("Password Generator")
root.geometry('275x200')
root.resizable(False,False)

def generate_password():
    text = Text(root, height=1)
    text.grid(row=7, column=0, pady=3, padx=3)
    global msg
    msg = password_generator(length.get(), stored.get())
    text.insert('1.0', msg)

def copy():
    from pyperclip import copy
    copy(msg)

length=IntVar(value=8)
stored = IntVar()
ttk.Label(root, text="What's your password strength?").grid(row=0, column=0,sticky=NW)
ttk.Radiobutton(root, text='Weak', value=0, variable=stored).grid(row=1, column=0, sticky=W,padx=1)
ttk.Radiobutton(root, text='Medium', value=1, variable=stored).grid(row=2, column=0, sticky=W,padx=1)
ttk.Radiobutton(root, text='Strong', value=2, variable=stored).grid(row=3, column=0, sticky=W,padx=1)
ttk.Label(root, text="What is the password length?").grid(row=4, column=0, sticky=W)
ttk.Spinbox(root,from_=6,to=24,textvariable=length).grid(row=6,column=0, sticky=NW,padx=3)
ttk.Button(root, text='Generate password', command=generate_password).grid(row=8, column=0, sticky=NW,padx=2,pady=1)
ttk.Button(root,text='Copy to clipboard',command=copy).grid(row=9,column=0,sticky=NW,padx=2)
text=Text(root,height=1)
text.grid(row=7,column=0,pady=3,padx=3)
text.insert('1.0','Generate your password')
text['state']='disabled'

root.mainloop()
