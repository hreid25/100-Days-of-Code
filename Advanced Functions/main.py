from tkinter import *

def button_clicked():
    user_entry = user_input.get()
    my_label.config(text=user_entry)
    print('button clicked')

window = Tk()
window.title("A GUI Program")
window.minsize(width=500,height=300)

# Label
my_label = Label(text="Label text",font=("Arial", 24, "bold"))
my_label.pack()
# widgets can be configured at the time they are created by passing keywords (like above), after they have been created using the named key or using the 'config' method on the widget object itself. (see below)
my_label['text'] = "access by key"
my_label.config(text='override by config')
my_label.grid(column=0,row=0)

# Button Grid and Pack cannot be used simultaneously. You must choose one or the other when working on a layout

# button
button = Button(text='click me',command=button_clicked)
button.grid(column=2,row=1)

# button 2
button_two = Button(text='2nd button')
button_two.grid(column=3,row=0)
# Entry
user_input = Entry(width=10)
user_input.grid(column=4,row=3)
# user_input.pack()
# user_input.insert()

window.mainloop()