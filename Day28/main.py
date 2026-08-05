from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_countdown, text="00:00")
    tick_mark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        timer_text.config(text="Long Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        timer_text.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)

    else:
        timer_text.config(text="Work Time", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_countdown, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)

    if count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(work_sessions/2)
        for _ in range(work_sessions):
            marks += "✓"
            tick_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer text heading
timer_text = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_text.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

#Tomato image
tomato_image = PhotoImage(file="tomato.png")
image = canvas.create_image(100, 112, image=tomato_image)

# Timer countdown text
timer_countdown = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

#Reset button
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

#Tick mark
tick_mark = Label(text="", fg=GREEN, bg=YELLOW)
tick_mark.grid(column=1, row=3)

window.mainloop()