from tkinter import * # import all Classes and constants, though not messagebox module
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project **DAY 5**

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)
    # THE ABOVE NR VARIABLES ARE REPLACEABLE BY IMPORTING RANDINT ETC TO STREAMLINE THE CODE FURTHER

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    # replaces below two lines - LIST COMPREHENSION
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers = [choice(numbers) for i in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # REPLACES BELOW LINES OF CODE
    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0, password)
    pyperclip.copy(password) # password gets copied to clipboard automatically
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        # Adds another username/passwords to existing data.json in turn
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                # Reading old data
                data = json.load(data_file) # changes JSON data to a Python dictionary to easily work with it in our code
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"] # tag on another key 'email' to get hold of value associated with that key
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"{email}\n{password}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=200, height=200)

#Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus() # focus the cursor on this entry upon app starting
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "email@hotmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search passwords", command=find_password)
search_button.grid(column=2 , row=1)

window.mainloop()