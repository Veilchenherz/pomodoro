from customtkinter import *
from PIL import Image, ImageTk
import tkinter

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5aa55f"
LIGHT_GREEN = "#7bb77f"
YELLOW = "#f7f5dd"
GRAY_BG = "gray14"
FONT_NAME = "Roboto"
TEXT_COLOR_DISABLED = "#b3b3b3"


class MainWindow(CTk):

    def __init__(self, start_function=None, reset_function=None, options_function=None, dark_mode=None, **kwargs):
        super().__init__(**kwargs)
        self.darkmode = dark_mode
        set_appearance_mode(self.darkmode)
        self.title("Zeitmanagement")
        self.iconbitmap(bitmap="tomato.ico")
        self.geometry("700x450")
        self.minsize(width=700, height=450)
        self.resizable(False, False)
        self.configure(padx=30, pady=30)
        self.grid_columnconfigure(1, weight=1)
        self.configure(fg_color=(YELLOW, GRAY_BG))
        self.timer = "00:00"
        self.start_function = start_function
        self.reset_function = reset_function
        self.options_function = options_function

        self.top_label = CTkLabel(
            master=self,
            text="Zeitmanagement",
            text_color=GREEN,
            font=(FONT_NAME, 30, "bold"),
        )
        self.top_label.grid(row=0, column=1, padx=5, pady=5)

        self.start_button = CTkButton(
            master=self,
            text="Start",
            width=160,
            fg_color=GREEN,
            text_color="white",
            hover_color=LIGHT_GREEN,
            font=(FONT_NAME, 18),
            command=self.press_start,
            text_color_disabled=TEXT_COLOR_DISABLED
        )
        self.start_button.grid(row=2, column=0, padx=5, pady=30)

        self.reset_button = CTkButton(
            master=self,
            text="Zurücksetzen",
            width=160,
            fg_color=GREEN,
            hover_color=LIGHT_GREEN,
            text_color="white",
            font=(FONT_NAME, 18),
            command=self.press_reset,
            state=DISABLED,
            text_color_disabled=TEXT_COLOR_DISABLED
        )
        self.reset_button.grid(row=2, column=2, padx=5, pady=30)

        self.options_button = CTkButton(
            master=self,
            text="Einstellungen",
            width=160,
            font=(FONT_NAME, 18),
            fg_color=GREEN,
            hover_color=LIGHT_GREEN,
            text_color="white",
            command=self.press_options,
            text_color_disabled=TEXT_COLOR_DISABLED
        )
        self.options_button.grid(row=2, column=1, padx=5, pady=30)

        self.tomato_canvas = CTkCanvas(master=self, height=223, width=200, bg=GRAY_BG, highlightthickness=0)
        self.tomato_image = tkinter.PhotoImage(file="tomato.png")
        self.tomato_canvas.create_image(100, 110, image=self.tomato_image)
        self.timer_text = self.tomato_canvas.create_text(105, 130, text=self.timer, font=(FONT_NAME, 25), fill="white")
        self.tomato_canvas.grid(row=1, column=1, pady=20)

        self.transparent_image = tkinter.PhotoImage(file="transparent.png")
        self.tomato_image_small = Image.open(fp="tomato.png").resize((90, 100))
        self.img_ready = ImageTk.PhotoImage(self.tomato_image_small)

        self.checkmarks = CTkCanvas(master=self, height=112, width=120, bg=GRAY_BG, highlightthickness=0)
        self.checkmarks_image = self.checkmarks.create_image(61, 50, image=self.transparent_image)
        self.number_work_units = self.checkmarks.create_text(61, 58, text="", fill="white", font=(FONT_NAME, 20))

        self.checkmarks.grid(row=1, column=2, sticky="S", pady=10)


    def reset_gui(self):
        self.tomato_canvas.itemconfig(self.timer_text, text="00:00")
        self.top_label.configure(text="Zeitmanagement")
        self.start_button.configure(state=NORMAL)
        self.options_button.configure(state=NORMAL)
        self.checkmarks.itemconfig(self.number_work_units, text="")
        self.checkmarks.itemconfig(self.checkmarks_image, image=self.transparent_image)

    def change_appearence(self, dark_mode):
        if dark_mode == "1":
            set_appearance_mode("dark")
            self.tomato_canvas.config(background=GRAY_BG)
            self.checkmarks.config(background=GRAY_BG)
        elif dark_mode == "0":
            set_appearance_mode("light")
            self.tomato_canvas.config(background=YELLOW)
            self.checkmarks.config(background=YELLOW)


    def press_start(self):
        self.start_function()

    def press_reset(self):
        self.reset_function()

    def press_options(self):
        self.options_function()






