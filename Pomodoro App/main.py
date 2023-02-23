from tkinter import *
from datetime import datetime, timedelta
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_restart():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    # set current time btn was clicked
    time_start = datetime.now()
    # set the time at which the timer should end
    end_timer = time_start + timedelta(minutes=25)
    timer = end_timer - datetime.now()
    count_down(time_start,end_timer,timer)
    # # start printing the countdown on the tomato
    # while end_timer != time_start:
    #     time.sleep(1)
    #     
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time_start,end_timer,timer):
    canvas.itemconfig(timer_text, text=timer)
    print(type(timer))
    while end_timer != time_start:
        window.after(1000, count_down, timer - timedelta(seconds=1))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=GREEN)

# bring up tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224, bg=GREEN, highlightthickness=0)
canvas.create_image(102,112,image=tomato_img)
timer_text = canvas.create_text(102,130,text="00:00", font=(FONT_NAME, "20", "bold"),fill='white',tag='default')
canvas.grid(column=2,row=2)

# Place 'Timer', start, reset and checkmark buttons
timer_label = Label(text="Timer",font=(FONT_NAME,'50','bold'), bg=GREEN)
timer_label.grid(column=2,row=1)

start_btn = Button(text="Start",font=(FONT_NAME,'10','bold'),command=timer_start)
start_btn.grid(column=1,row=3)

reset_btn = Button(text="Reset",font=(FONT_NAME,'10','bold'))
reset_btn.grid(column=3,row=3)

check_marks = Label(text="✓",bg=GREEN,fg=RED)
check_marks.grid(column=2,row=3)

# timer_start()
window.mainloop()