from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ----- Save the information -----
def save_password():
    # Get the information to save
    information = {website_entry.get().upper(): {"email": email_user_entry.get(), "password": password_entry.get()}}
    if len(website_entry.get()) == 0 or len(email_user_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Oops!", message="Don't leave empty fields!")
    else:
        # Ask the user if they want to save and show the information
        info_ok = messagebox.askokcancel(title="Information", message=f"You are about to save this information:"
                                                                      f"\nWebsite--> {website_entry.get()}"
                                                                      f"\nEmail--> {email_user_entry.get()}"
                                                                      f"\nPassword--> {password_entry.get()}\n"
                                                                      f"\nDo you want to save?")
        # If ok is pressed, save the information
        if info_ok:
            # Try to read the information in the file
            try:
                # Get the json file on read mode
                with open(file="./passwords.json", mode="r") as passwords_file:
                    # Get the information of the json file
                    data = json.load(passwords_file)
                    # Update the data with the new information
                    data.update(information)
                    write_information(data)
            # If the file is not created
            except FileNotFoundError:
                # Create the file and write the first information
                write_information(information)
            # If the file is created but it has no information
            except json.decoder.JSONDecodeError:
                # Write the first information
                write_information(information)
            finally:
                # Clear the entries
                website_entry.delete(first=0, last=END)
                password_entry.delete(first=0, last=END)


def write_information(data):
    with open(file="./passwords.json", mode="w") as passwords_file:
        json.dump(data, passwords_file, indent=4)


def search_information():
    website = website_entry.get().upper()
    # If the website is blank, show a warning
    if website == "":
        messagebox.showwarning(title="Empty Entry", message="The entry is empty. Please introduce a website")
    else:
        # Try opening the file
        try:
            with open(file="./passwords.json", mode="r") as password_file:
                data = json.load(password_file)
        # If the file is not created, show a warning
        except FileNotFoundError:
            messagebox.showwarning(title="No Information", message="There is no information saved")
        # If there is no error, it means there is information
        else:
            # Try getting the information of the website
            try:
                data = data[website]
            # If the website is not in the file, show a warning
            except KeyError:
                messagebox.showwarning(title="Website Not Found", message="The website you searched is not saved")
            # If the information is in the file, show the information
            else:
                messagebox.showinfo(title=website, message=f"Email: {data["email"]}\nPassword: {data["password"]}")


# ----- Generate random password -----
def generate_password():
    # Choose all the elements
    random_letters = [random.choice(letters) for _ in range(0, 8)]
    random_numbers = [random.choice(numbers) for _ in range(0, 4)]
    random_symbols = [random.choice(symbols) for _ in range(0, 4)]
    # Put all the elements together
    random_password = random_letters + random_numbers + random_symbols
    # Shuffle the random password
    random.shuffle(random_password)
    # Convert the list into a string
    random_password = "".join(random_password)
    # Insert it into the password entry
    password_entry.insert(index=0, string=random_password)
    # Copy the password
    pyperclip.copy(random_password)


# ----- User Interface -----
root = Tk()
root.title("Password Manager")
root.config(padx=40, pady=30)
root.resizable(height=False, width=False)

# Create a canvas for placing the image
canvas = Canvas(width=200, height=200)
# Create de PhotoImage
lock_img = PhotoImage(file="lock.png")
# Reduce its size 3 times
lock_img = lock_img.subsample(3, 3)
# Place de image on the canvas
canvas.create_image(100, 90, image=lock_img)
canvas.grid(row=0, column=1)

# Create the labels
website_label = Label(text="Website:")
website_label.config(font=("Arial", 12, "bold"))
website_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:")
email_user_label.config(font=("Arial", 12, "bold"))
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.config(font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0)

# Create the entries
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_user_entry = Entry(width=60)
email_user_entry.insert(index=0, string="randomemail@gmail.com")
email_user_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

# Create the buttons
search_website_button = Button(text="Search", width=16, command=search_information)
search_website_button.config(font=("Arial", 8, "normal"))
search_website_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", width=16, command=generate_password)
generate_password_button.config(font=("Arial", 8, "normal"))
generate_password_button.grid(row=3, column=2, padx=6)

add_button = Button(text="Add", width=44, command=save_password)
add_button.config(font=("Arial", 10, "normal"))
add_button.grid(row=4, column=1, columnspan=2, pady=10)

root.mainloop()
