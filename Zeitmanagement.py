import math
from tkinter import *
from menu_gui import Options
from main_window_gui import MainWindow

# colors (hex-codes) and font
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5aa55f"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# show or hide work unit counter
small_tomato_visible = False

# number of units the user completed (work, breaks)
repetitions = 0

# tkinter window.after which is used as a countdown
timer = None

# dark mode keywords for customtkinter
dark_mode_dict = {
    "0": "light",
    "1": "dark"
}


# reset the timer to zero and the gui to the state the app has when it is started
def reset_timer():
    main_window.after_cancel(timer)
    main_window.reset_gui()
    global repetitions
    repetitions = 0
    main_window.reset_button.configure(state=DISABLED)


# control which timer is started to match the correct order of the units within the pomodoro technique
def start_timer():
    global repetitions

    # when a timer is started, you are not able to press the start or options button
    main_window.start_button.configure(state=DISABLED)
    main_window.options_button.configure(state=DISABLED)
    main_window.reset_button.configure(state=NORMAL)

    # count the number of units
    repetitions += 1

    #calculate the durations in seconds
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min * 60

    # long breaks every 8th unit
    if repetitions % 8 == 0:
        countdown_time = long_break_sec
        main_window.top_label.configure(text="Pause")

    # short breaks every 2nd unit (only if no long break must happen)
    elif repetitions % 2 == 0:
        countdown_time = short_break_sec
        main_window.top_label.configure(text="Pause")

    # every other unit is a work unit
    else:
        countdown_time = work_sec
        main_window.top_label.configure(text="Arbeiten")

    # start a countdown with the time corresponding to the applicable unit
    countdown(countdown_time)


# start a countdown with a given time in seconds
def countdown(count):

    # calculate the time in minutes and the remaining seconds from the input in seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # format the remaining seconds with a 0 in front, if the number has only one digit
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    # display the time in the app
    main_window.tomato_canvas.itemconfig(main_window.timer_text, text=f"{count_min}:{count_sec}")

    # run timer recursively as long as the duration (count) is greater than zero
    if count > 0:
        global timer
        timer = main_window.after(1000, countdown, count - 1)

    # behaviour when the timer reached zero
    else:
        # bring the window in front to alert the user
        main_window.attributes("-topmost", True)
        main_window.focus()
        main_window.attributes("-topmost", False)

        # start the next timer
        start_timer()
        global repetitions, small_tomato_visible

        # calculate the amount of work units
        number_of_checkmarks = math.floor(repetitions / 2)

        # if the work counter is not visible (default when app is started), show it to the user
        if not small_tomato_visible:
            main_window.checkmarks.itemconfig(
                main_window.checkmarks_image,
                image=main_window.img_ready
            )
            small_tomato_visible = True

        # update the work unit counter
        main_window.checkmarks.itemconfig(
            main_window.number_work_units,
            text=number_of_checkmarks,
            fill="white",
            font=("Roboto", 25, "bold")
        )


# create a new instance of the options menu (opens a child window)
def open_menu():
    options = Options(
        work_time=work_min,
        short_time=short_break_min,
        long_time=long_break_min,
        dark_mode=dark_mode,
        callback=values_changed
    )


# save data that the user entered into the input fields of the options menu
def values_changed(new_data):

    # access global variables for the durations of the units and the dark mode
    global work_min, short_break_min, long_break_min, dark_mode

    # save data entered by the user
    work_min = int(new_data[0])
    short_break_min = int(new_data[1])
    long_break_min = int(new_data[2])
    dark_mode = str(new_data[3])

    # change app appearance according to the user preference (will do nothing if the user did not change the lever)
    main_window.change_appearance(dark_mode)

    # write the data that the user entered to the data text file to load it again on restart of the app
    with open("data.txt", "w") as data_file:
        data_file.write(f"{new_data[0]}\n{new_data[1]}\n{new_data[2]}\n{new_data[3]}")


# load user preferences (dark/light mode)
with open("data.txt") as data_file:
    data = data_file.readlines()
    dark_mode = str(data[3])

# create a new instance of the main app window
main_window = MainWindow(
    start_function=start_timer,
    reset_function=reset_timer,
    options_function=open_menu,
    dark_mode=dark_mode_dict[dark_mode]
)

# load user preferences (durations)
with open("data.txt") as data_file:
    data = data_file.readlines()
    work_min = int(data[0])
    short_break_min = int(data[1])
    long_break_min = int(data[2])

# keep the main window opened
main_window.mainloop()

