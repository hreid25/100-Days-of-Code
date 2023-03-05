from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# --------------------------  CONSTANTS --------------------------

BG_COLOR = 'white'

# --------------------------  GEN PASSWORD --------------------------

def gen_password():
    password_entry.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# --------------------------  SEARCH PASSWORD --------------------------

def query_password(website_name):
    website = website_entry.get()
# Search for password in JSON and return entry in popup window
    try:
        with open('data.json', 'r') as credential_json:
            pass_json = json.load(credential_json)
            print('this is my json dict: ', pass_json.items())
            user_website_name = str(website_name).lower()
            # Create list of web name keys from JSON passwords
            key_name = [k for k,v in pass_json.items() if user_website_name == str(k).lower()]
            if key_name:
                messagebox.showinfo(title="Password Retrieved", message=f"The password for {website} is: {pass_json[key_name[0]]['password']}")
            else:
                messagebox.showinfo(title="Password Not Found", message=f"No Matching Password was found for {website}")
    except FileNotFoundError:
        messagebox.showerror(title='No Passwords',message='Currently you have no passwords stored. Please create your entries before searching.')

# --------------------------  SAVE PASSWORD --------------------------

def save():
    # Check that the website, and password fields are not blank, if they are, send an error message and clear the fields
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    
    if website_entry.get() and password_entry.get() != "":
        list_credentials = []
        # pass_data = open('pass_data.json', 'w')
        credential_entry = {
            website: {
                'email' : email,
                'password' : password
            }
        }
        # Determine if the user already has a password for a given website
        try:
            with open('data.json', 'r') as credential_json:
                pass_json = json.load(credential_json)
        except FileNotFoundError:
            # The first time a password is entered a json file will not have been created.
            # Create JSON in write mode and store first password
            with open('data.json', 'w') as credential_json:
                json.dump(credential_entry,credential_json,indent=4)
                website_entry.delete(0,'end')
                password_entry.delete(0,'end')
        # Add the new credential entry into the password JSON
        else:
            is_ok = messagebox.askokcancel(title='Confirm Change',message=f'Are you sure you want to add the password for {website_entry.get()}?')
            if is_ok:
                with open('data.json', 'r') as credential_json:
                    pass_json = json.load(credential_json) # Reading the old data, returning a dict object
                    pass_json.update(credential_entry) # Updating old data with new data
                with open('data.json', 'w') as credential_json:
                    json.dump(pass_json,credential_json,indent=4) #saving updated data
                website_entry.delete(0,'end')
                password_entry.delete(0,'end')
    else:
        messagebox.showerror(title='ERROR',message='Please enter a valid Website name and Password.')    

    

# --------------------------  WINDOWS --------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg='white')

padlock_img = PhotoImage(file='og_padlock_150x150.png') 
canvas = Canvas(height=200,width=200,bg=BG_COLOR,highlightthickness=0)
canvas.create_image(100,100,image=padlock_img)
canvas.grid(column=1,row=0)

# Create Field Labels
website_label = Label(text='Website:',bg=BG_COLOR)
website_label.grid(column=0,row=1)

email_label = Label(text='Email:', bg=BG_COLOR)
email_label.grid(column=0,row=2)

password_label = Label(text='Password:',bg=BG_COLOR)
password_label.grid(column=0,row=3)

# Create Entries
website_entry = Entry(bg=BG_COLOR, width=32)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_entry = Entry(bg=BG_COLOR, width=50)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,'hayd.reid@gmail.com')

password_entry = Entry(bg=BG_COLOR, width=32)
password_entry.grid(column=1,row=3)

# Create Buttons
generate_btn = Button(text='Generate Password',bg=BG_COLOR,command=gen_password)
generate_btn.grid(column=2,row=3)

add_btn = Button(text='Add',bg=BG_COLOR, width=43,command=save)
add_btn.grid(column=1,row=4,columnspan=2)

find_pass_entry = Button(text='Search' ,bg=BG_COLOR,width=10,command= lambda: query_password(website_entry.get()))
find_pass_entry.grid(column=2,row=1)

window.mainloop()