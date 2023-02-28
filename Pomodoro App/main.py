from tkinter import *
from datetime import datetime, timedelta
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_restart():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():

    def calc_timer(timer_duration, break_name):
        timer_label.config(text=break_name)
        timer_ends_at = time_start + timedelta(minutes=timer_duration)
        timer = timer_ends_at - datetime.now()
        return timer

    global REPS
    REPS += 1
    time_start = datetime.now()
    # Long break timer occurs at 8 reps
    if REPS % 8 == 0:
        timer = calc_timer(25,'Break')
        count_down(timer)
    # Short break timer occurs 2/4/6
    elif REPS % 2 == 0:
        timer = calc_timer(5,'Break')
        count_down(timer)
    # Work timer occurs 1/3/5/7 rep
    else:
        timer = calc_timer(25,'Work Timer')
        count_down(timer)

# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(countdown):
    global timer
    canvas.itemconfig(timer_text, text=countdown)
    if countdown > timedelta(seconds=0):
        timer = window.after(1000, count_down, countdown - timedelta(seconds=1))
    else:
        timer_start()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=GREEN)

# bring up tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224, bg=GREEN, highlightthickness=0)
canvas.create_image(102,112,image=tomato_img)
# canvas.create_image(0,0,image=tomato_img)
timer_text = canvas.create_text(102,130,text="00:00", font=(FONT_NAME, "20", "bold"),fill='white',tag='timer_default_canv')
canvas.grid(column=2,row=2)

# Place 'Timer', start, reset and checkmark buttons
timer_label = Label(text="Timer",font=(FONT_NAME,'35','bold'), bg=GREEN)
timer_label.grid(column=2,row=1)

start_btn = Button(text="Start",font=(FONT_NAME,'10','bold'),command=timer_start)
start_btn.grid(column=1,row=3)

reset_btn = Button(text="Reset",font=(FONT_NAME,'10','bold'),command=timer_restart)
reset_btn.grid(column=3,row=3)

check_marks = Label(bg=GREEN,fg=RED)
check_marks.grid(column=2,row=3)





window.mainloop()