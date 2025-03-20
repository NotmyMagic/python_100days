from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', "i", 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%' ,'&', ',', '*', '+']

    password_up_letters = [choice(upper) for _ in range(randint(2, 3))]
    password_low_letters = [choice(lower) for _ in range(randint(5, 7))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_low_letters + password_up_letters + password_numbers + password_symbols
    shuffle(password_list)
    
    password = "".join(password_list)
    password_e.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_e.get()
    user = user_e.get()
    password = password_e.get()
    new_data = {website: {
        "email": user,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please check if you have an empty field.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Are you sure you want this to be your info?\nEmail/Username: {user}\nPassword: {password}")

        if is_ok:
            try:
                with open("./part3/password_generate/data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)

                with open("./part3/password_generate/data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            except FileNotFoundError:
                    with open("./part3/password_generate/data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
            finally:
                website_e.delete(0, END)
                password_e.delete(0, END)   

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password generator")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="./part3/password_generate/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website", font=("Ariel", 11 , "italic"))
website_l.grid(column=0, row=1)
user_l = Label(text="Email/Username", font=("Ariel", 11 , "italic"))
user_l.grid(column=0, row=2)
password_l = Label(text="Password", font=("Ariel", 11 , "italic"))
password_l.grid(column=0, row=3)

website_e = Entry(width=49)
website_e.grid(column=1, row=1, columnspan=2, padx=(15, 0))
website_e.focus()
user_e = Entry(width=49)
user_e.grid(column=1, row=2, columnspan=2, padx=(15, 0))
user_e.insert(0, "some-email@gmail.com")
password_e = Entry(width=28)
password_e.grid(column=1, row=3)


pass_btn = Button(text="Generate Password", command=generate)
pass_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=42, command=save)
add_btn.grid(column=1, row=4, columnspan=2, padx=(15, 0))




window.mainloop()