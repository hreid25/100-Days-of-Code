from tkinter import *
from datetime import datetime, timedelta


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

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_restart():
    canvas.delete('default')
    canvas.delete('b_type')
    timer_text = canvas.create_text(102,130,text="00:00", font=(FONT_NAME, "20", "bold"),fill='white',tag='default')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global REPS
    REPS += 1
    # set current time btn was clicked
    b_type = canvas.create_text(102,100,text='Work Timer',font=(FONT_NAME,'20','bold'), fill='white',tag='b_type')
    time_start = datetime.now()
    # set the time at which the timer should end
    work_end = time_start + timedelta(minutes=25)
    work_timer = work_end - datetime.now()
    # set the short break timer
    sb_end = time_start + timedelta(minutes=5)
    sb_timer = sb_end - datetime.now()
    # set the long break timer
    lb_end = time_start + timedelta(minutes=25)
    lb_timer = lb_end - datetime.now()
    # call the count down function according to the reps
    # short break timer occurs 2/4/6
    if REPS % 2 == 0:
        canvas.itemconfig(b_type, text='Short Break')
        count_down(sb_timer)
    # long break timer occurs at 8 reps
    elif REPS % 8 == 0:
        canvas.itemconfig(b_type, text='Long Break')
        count_down(lb_timer)
    # work timer occurs 1/3/5/7 rep
    else:
        canvas.itemconfig(b_type, text='Work Timer')
        count_down(work_timer)

# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(timer):
    canvas.itemconfig(timer_text, text=timer)
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

reset_btn = Button(text="Reset",font=(FONT_NAME,'10','bold'),command=timer_restart)
reset_btn.grid(column=3,row=3)

check_marks = Label(text="✓",bg=GREEN,fg=RED)
check_marks.grid(column=2,row=3)





window.mainloop()