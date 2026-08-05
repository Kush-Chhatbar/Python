from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_special_characters = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(0, nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(0, nr_numbers)]
    password_symbols = [random.choice(special_characters) for _ in range(0, nr_special_characters)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
         website:{
              "email":email,
              "password":password
         }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showwarning(title="Warning", message="Please donot leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These details are going to be saved\n\n Email: {email}\n Password: {password}\n\n Are you sure with this details?")
        if is_ok:
            try:
                with open("credentials.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("credentials.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            else:
                data.update(new_data)
                with open("credentials.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20, bg="white")

# Title image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.grid(column=1, row=0)
title_image = PhotoImage(file="logo.png")
password_image = canvas.create_image(100, 100, image=title_image)

# Website field
website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

# Email/Username field
email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

# Password field
password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Generate Password button
password_button = Button(text="Generate Password", bg="white", command=generate_password)
password_button.grid(column=2, row=3, columnspan=2)

# Add data in file button
add_data_button = Button(text="Add", bg="white", width=36, command=add_data)
add_data_button.grid(column=1, row=4, columnspan=2)


window.mainloop()