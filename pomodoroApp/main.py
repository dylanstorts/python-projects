import tkinter as t
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Ubuntu"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = t.Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato = t.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.create_text(103, 112, text="00:00", fill="white", font=(FONT_NAME, 32))
canvas.grid(row=1, column=1)

start_btn = t.Button(text="START", bg=PINK, fg=YELLOW)
start_btn.grid(row=2, column=0)

reset_btn = t.Button(text="RESET", bg=PINK, fg=YELLOW)
reset_btn.grid(row=2, column=2)

status_lbl = t.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 32))
status_lbl.grid(row=0, column=1)

check_lbl0 = t.Label(text=CHECK_MARK, font=(FONT_NAME, 16), bg=YELLOW, fg=GREEN)
check_lbl0.grid(row=2, column=1)

# check_lbl1 = t.Label(text="✔️", font=(FONT_NAME, 16), bg=YELLOW, fg=GREEN)
# check_lbl1.grid(row=2, column=1)
#
# check_lbl2 = t.Label(text="✔️", font=(FONT_NAME, 16), bg=YELLOW, fg=GREEN)
# check_lbl2.grid(row=2, column=1)

window.mainloop()
