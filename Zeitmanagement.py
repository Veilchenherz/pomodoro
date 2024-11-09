import math
from tkinter import *
from menu_gui import Options
from main_window_gui import MainWindow

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5aa55f"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
small_tomato_visible = False
repetitions = 0
timer = None
dark_mode_dict = {
    "0": "light",
    "1": "dark"
}
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    main_window.after_cancel(timer)
    main_window.reset_gui()
    global repetitions
    repetitions = 0
    main_window.reset_button.configure(state=DISABLED)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global repetitions
    main_window.start_button.configure(state=DISABLED)
    main_window.options_button.configure(state=DISABLED)
    main_window.reset_button.configure(state=NORMAL)
    repetitions += 1
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60

    if repetitions % 8 == 0:
        countdown_time = long_break_sec
        main_window.top_label.configure(text="Pause")

    elif repetitions % 2 == 0:
        countdown_time = short_break_sec
        main_window.top_label.configure(text="Pause")

    else:
        countdown_time = work_sec
        main_window.top_label.configure(text="Arbeiten")

    countdown(countdown_time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    main_window.tomato_canvas.itemconfig(main_window.timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = main_window.after(1000, countdown, count - 1)

    else:
        main_window.attributes("-topmost", True)
        main_window.focus()
        main_window.attributes("-topmost", False)
        start_timer()
        global repetitions, small_tomato_visible
        number_of_checkmarks = math.floor(repetitions / 2)

        if not small_tomato_visible:
            main_window.checkmarks.itemconfig(
                main_window.checkmarks_image,
                image=main_window.img_ready
            )
            small_tomato_visible = True

        main_window.checkmarks.itemconfig(
            main_window.number_work_units,
            text=number_of_checkmarks,
            fill="white",
            font=("Roboto", 25, "bold")
        )

#---------------------------Options Menu----------------------------#


def open_menu():
    options = Options(
        work_time=work_min,
        short_time=short_break_min,
        long_time=long_break_min,
        dark_mode=dark_mode,
        callback=values_changed
    )


def values_changed(new_data):
    global work_min, short_break_min, long_break_min, dark_mode
    work_min = int(new_data[0])
    short_break_min = int(new_data[1])
    long_break_min = int(new_data[2])
    dark_mode = str(new_data[3])
    main_window.change_appearance(dark_mode)

    with open("data.txt", "w") as data_file:
        data_file.write(f"{new_data[0]}\n{new_data[1]}\n{new_data[2]}\n{new_data[3]}")



with open("data.txt") as data_file:
    data = data_file.readlines()
    dark_mode = str(data[3])

main_window = MainWindow(
    start_function=start_timer,
    reset_function=reset_timer,
    options_function=open_menu,
    dark_mode=dark_mode_dict[dark_mode]
)

with open("data.txt") as data_file:
    data = data_file.readlines()
    work_min = int(data[0])
    short_break_min = int(data[1])
    long_break_min = int(data[2])

main_window.mainloop()






# window = Tk()
# window.title("Pomodoro Zeitmanagement")
# window.config(padx=100, pady=50, bg=YELLOW)
# window.minsize(800,400)



# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato)
#
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
# canvas.grid(row=1, column=1)
#
# start_button = Button(text="Start", bg="white", command=start_timer)
# start_button.grid(row=2, column=0, sticky="E")
#
# reset_button = Button(text="Zurücksetzen", bg="white", command=reset_timer)
# reset_button.grid(row=2, column=2, sticky="W")
#
# top_label = Label(text="Zeitmanagement", font=(FONT_NAME, 45, "normal"))
# top_label.config(bg=YELLOW, fg=GREEN)
# top_label.grid(row=0, column=1)
#
# check_marks = Label(fg=GREEN, bg=YELLOW, font=("Courier",25,"normal"))
# check_marks.grid(row=3, column=1)
#
# options_button = Button(text="Einstellungen", command=open_menu)
# options_button.grid(row=0, column=2)
#
# window.mainloop()
