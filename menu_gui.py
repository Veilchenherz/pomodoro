from customtkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5aa55f"
LIGHT_GREEN = "#7bb77f"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"


class Options(CTkToplevel):

    def __init__(self, work_time, short_time, long_time, dark_mode, callback=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_min = work_time
        self.short_min = short_time
        self.long_min = long_time
        self.min_list = []
        self.callback = callback

        self.title("Einstellungen")
        self.geometry("200x350")
        self.minsize(200, 350)
        self.resizable(False, False)
        self.configure(fg_color=(YELLOW, "gray14"))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=8)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=5)
        self.focus()
        self.grab_set()

        self.top_label = CTkLabel(self, text="Einstellungen", text_color=GREEN, font=(FONT_NAME, 25, "bold"))
        self.top_label.grid(row=0, column=0, pady=5, padx=5, columnspan=4)

        self.work_label = CTkLabel(self, text="Dauer Arbeitseinheiten:", height=10, padx=12, pady=2)
        self.work_label.grid(row=1, column=0, sticky="WS", columnspan=2)

        self.short_break_label = CTkLabel(self, text="Dauer kurze Pausen:", padx=12, pady=2)
        self.short_break_label.grid(row=3, column=0, sticky="WS", columnspan=3)

        self.long_break_label = CTkLabel(self, text="Dauer lange Pausen:", padx=12, pady=2)
        self.long_break_label.grid(row=5, column=0, sticky="WS", columnspan=3)

        self.work_input = CTkEntry(self, width=60, height=10)
        self.work_input.insert(0, work_time)
        self.work_input.grid(row=2, column=0, pady=2, padx=5, sticky="NE")

        self.short_break_input = CTkEntry(self, width=60, height=10)
        self.short_break_input.insert(0, short_time)
        self.short_break_input.grid(row=4, column=0, pady=2, padx=5, sticky="NE")

        self.long_break_input = CTkEntry(self, width=60, height=10)
        self.long_break_input.insert(0, long_time)
        self.long_break_input.grid(row=6, column=0, pady=2, padx=5, sticky="NE")

        self.min_label_1 = CTkLabel(self, text="min")
        self.min_label_1.grid(row=2, column=1, sticky="WN", pady=2, padx=0)

        self.min_label_2 = CTkLabel(self, text="min")
        self.min_label_2.grid(row=4, column=1, sticky="WN", pady=2, padx=0)

        self.min_label_3 = CTkLabel(self, text="min")
        self.min_label_3.grid(row=6, column=1, sticky="WN", pady=2, padx=0)

        self.dark_mode_label = CTkLabel(self, text="Nachtmodus:")
        self.dark_mode_label.grid(row=7, column=0, sticky="W", padx=12, columnspan=3)

        self.dark_mode_switch = CTkSwitch(self, text="", progress_color=GREEN, width=50)
        if dark_mode == "1":
            self.dark_mode_switch.toggle()
        self.dark_mode_switch.grid(row=7, column=1, sticky="E")

        self.ok_button = CTkButton(
            self,
            text="OK",
            text_color="white",
            hover_color=LIGHT_GREEN,
            width=80, fg_color=GREEN,
            command=self.press_ok_button
        )
        self.ok_button.grid(row=8, column=0, sticky="W", padx=12, columnspan=2, pady=10)

        self.cancel_button = CTkButton(
            self,
            text="Abbrechen",
            width=80,
            text_color="white",
            fg_color=GREEN,
            hover_color=LIGHT_GREEN,
            command=self.press_cancel_button
        )
        self.cancel_button.grid(row=8, column=1, columnspan=3, sticky="E", padx=12, pady=10)

    def press_ok_button(self):
        self.min_list = [self.work_input.get(), self.short_break_input.get(), self.long_break_input.get(), self.dark_mode_switch.get()]
        self.callback(self.min_list)
        self.destroy()

    def press_cancel_button(self):
        self.destroy()






