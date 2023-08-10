from tkinter import *
import math
import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
repl = 1
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer_laber
    global timer_text
    global repl
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text , text='00:00')

    repl = 0
    tick.config(text="")
    list = []
    timer_laber.config(text='Timer')


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global timer_laber
    global repl
    if repl == 0:
        count_down(WORK_MIN)
        timer_laber.config(text='Timer',fg=GREEN)
        repl += 1
    elif not repl % 2 == 0:
        count_down(WORK_MIN)
        timer_laber.config(text='Timer' ,fg=GREEN)
        repl += 1

    elif repl == 8:
        count_down(LONG_BREAK_MIN)
        timer_laber.config(text='Break',fg=RED)
        repl= 1
    elif repl% 2 == 0:
        count_down(SHORT_BREAK_MIN)
        timer_laber.config(text='Break',fg=PINK)
        repl += 1
    print(repl)



def break_timer(x):
    count_down(x)
def label_change():
    global reps
    global timer_laber
    global current_label
    current_label = timer_laber['text']
    if current_label == 'Timer':
        current_label ="Break"
    else:
        current_label = "Timer"
    print(current_label)
    timer_laber.config(text=f"{current_label}")



hello = 0
i = 2
y = 0
list = []
normal_str = ""
a = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_laber
    global hello
    global normal_str
    global list
    global my_timer

    min = math.floor(count/60)
    sec = count%60
    if count < 10 or sec == 0:
        sec = f"0{sec}"


    canvas.itemconfig(timer_text,text=f"{min}:{sec}")

    if count > 0:
        my_timer = window.after(1000,count_down,count-1)

    else:
        if repl% 2 == 0:
            if not repl == 8:
                list.append("✓")
                normal_str = ""

                for i in list:
                    normal_str = normal_str + i
                    tick.config(text=normal_str)
            else:
                tick.config(text="✓✓✓✓")
                list = []
        start_timer()
        print(list)
        print(normal_str)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))

canvas.grid(row=2,column=2)

#timer_label easy peasy mantra bot mantra noob
timer_laber = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,'bold'))
timer_laber.grid(column=2,row=0)

#start button

start_button= Button(text="Start",command=start_timer)
start_button.grid(column=1,row=5)

#tick_label
tick = Label(text="",fg=GREEN,bg=YELLOW)
tick.grid(column=2,row=6)

#reset button

reset_button= Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=5)



window.mainloop()
