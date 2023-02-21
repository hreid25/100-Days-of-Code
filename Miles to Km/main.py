from tkinter import *

FONT = ('Arial',12)

def get_kms():
    mile_nums = float(miles_entry.get())
    num_kms = round(mile_nums * 1.60934)
    km_converted.config(text=num_kms, font=FONT)

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300,height=150)
window.config(padx=20,pady=20)

miles_entry = Entry(width=15,font=FONT)
miles_entry.grid(column=2,row=1)

miles_label = Label(text='Miles', font=FONT)
miles_label.grid(column=3,row=1)
miles_label.config(padx=20,pady=20)


text_label = Label(text='is equal to: ', font=FONT)
text_label.grid(column=1,row=2)

km_converted = Label(text=0, font=FONT)
km_converted.config(padx=20, pady=20)
km_converted.grid(column=2,row=2)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=3,row=3)

calc_btn = Button(text="Calculate", command=get_kms, font=FONT)
calc_btn.grid(column=2,row=3)


window.mainloop()