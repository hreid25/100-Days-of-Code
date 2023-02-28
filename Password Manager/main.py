from tkinter import *
import random

# --------------------------  CONSTANTS --------------------------

# FONT = 'Arial'
BG_COLOR = 'white'
# INPUT_LABELS_FONT_SIZE = '12'
# ENTRY_TYPE_WIDTH = 25

# --------------------------  SAVE TO FILE --------------------------

def add_password():
    pass_data = open('pass_data.txt', 'a')
    payload = {
        'website' : website_entry.get(),
        'password' : password_entry.get(),
        'email' : email_entry.get()
    }
    f = open('pass_data.txt')
    for line in f:
        password_details = line.strip().split('|')
        print(password_details)
        # TODO need to append new password details to additional dictionary entry
        current_passwords = {
            'website' : password_details[0],
            'password' : password_details[1],
            'email' : password_details[2]
        }
    print(payload["website"])
    print('tet printing values method: ', current_passwords.values())
    for k,v in payload.items():
        if v == "":
            print('A value was not supplied.')
            # TODO Create Pop Up Window specifying required data wasn't supplied.
        elif payload["website"] in current_passwords.values():
            print('That website already has a password: ', v, ' Overwrite?')
            # k["password"] == password_entry.get()
            # overwrite the previous password with the new password
        # else:
        #     pass_data.write(f'{payload["website"]} | {payload["email"]} | {payload["password"]}\n')
    
    # pass_data.write(f'{payload["website"]} | {payload["email"]} | {payload["password"]}\n')

# --------------------------  WINDOW --------------------------

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
generate_btn = Button(text='Generate Password',bg=BG_COLOR)
generate_btn.grid(column=2,row=3)

add_btn = Button(text='Add',bg=BG_COLOR, width=43,command=add_password)
add_btn.grid(column=1,row=4,columnspan=2)

find_pass_entry = Button(text='Query Website Password' ,bg=BG_COLOR,width=43)
find_pass_entry.grid(column=1,row=5,columnspan=2)




window.mainloop()