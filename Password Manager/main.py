from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# --------------------------  CONSTANTS --------------------------

# FONT = 'Arial'
BG_COLOR = 'white'
# INPUT_LABELS_FONT_SIZE = '12'
# ENTRY_TYPE_WIDTH = 25

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
        # TODO if the JSON file is empty at first, catch the decode error and then write the password to the file.
        try:
            with open('data.json', 'r') as password_file:
                passwords = json.load(password_file)
                if website in passwords.items():
                # Confirm password update, if website was not found, add the password to the pass_data file.
                    is_ok = messagebox.askokcancel(title='Confirm Change',message=f'Would you like to change the password for {email}')
                    if is_ok:
                        password_file.update(credential_entry)
                        json.dump(password_file,data_file,indent=4)
        # if the website was not found in our list, confirm that the user would like to add the new credentials
        except Exception as JSONDecodeError:
            print('First Password added')
            # Write code to dump the new credential to the password file here.
        else:
            is_ok = messagebox.askokcancel(title='Confirm Change',message=f'Would you like to add the password for {website_entry.get()}?')
            if is_ok:
                with open('data.json', 'w') as data_file:
                    json.dump(credential_entry,data_file,indent=4)
                # pass_data.write(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')
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
website_entry = Entry(bg=BG_COLOR, width=50)
website_entry.grid(column=1,row=1,columnspan=2)
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

find_pass_entry = Button(text='Query Website Password' ,bg=BG_COLOR,width=43)
find_pass_entry.grid(column=1,row=5,columnspan=2)

window.mainloop()