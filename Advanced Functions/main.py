from tkinter import *

window = Tk()
window.title("A GUI Program")
window.minsize(width=500,height=300)

# Label
my_label = Label(text="Label text",font=("Arial", 24, "bold"))
my_label.pack()
# widgets can be configured at the time they are created by passing keywords (like above), after they have been created using the named key or using the 'config' method on the widget object itself. (see below)
my_label['text'] = "access by key"
my_label.config(text='override by config')


def button_clicked():
    user_entry = user_input.get()
    my_label.config(text=user_entry)
    print('button clicked')

# button
button = Button(text='click me',command=button_clicked)
button.pack()

# Entry
user_input = Entry(width=10)
user_input.pack()


window.mainloop()