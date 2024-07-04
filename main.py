from tkinter import *
import random
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbols= [choice(symbols) for _ in range(nr_symbols)]
    password_numbers= [choice(numbers) for _ in range(nr_numbers)]

    pass_list= password_letter + password_symbols+ password_numbers

    shuffle(pass_list)

    password_gen = "".join(pass_list)
    pass_entry.insert(0,password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=pass_entry.get()

    if len(website) == 0 or len(password)==0:
        messagebox.showinfo("oops",message="Please make sure you haven't left any fields empty")
    else:

        is_ok= messagebox.askokcancel(title=website,message=f"These are the details entered : \nEmail:{email}"
        f"\nPassword:{password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                pass_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,114,image=img)
canvas.grid(column=2, row=1)


website_label = Label(text="Website:")
website_label.grid(column=1,row=2)


email_label = Label(text="Email/Username:")
email_label.grid(column=1,row=3)

password_label=Label(text="Password:")
password_label.grid(column=1,row=4)


website_entry=Entry(width=35)
website_entry.grid(column=2,row=2,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(column=2,row=3,columnspan=2)
email_entry.insert(0,"samanta21@gmail.com")
pass_entry=Entry(width=21)
pass_entry.grid(column=2,row=4)




add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=5,column=2,columnspan=2)

generate=Button(text="Generate Password",command=generate)
generate.grid(row=4,column=3)
window.mainloop()