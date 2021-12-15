from tkinter.font import ITALIC, BOLD
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename
import sys
import os

import PySimpleGUI as sg
import keyboard

from functions import *
from interpreter import *

#!Buttons on Top
btn = sg.Button(
        button_text = "Run", tooltip = "Search in all files",
        font = ("Consolas", 11),
        size = (15, 1), key = "-BTN-"
    )

btn2 = sg.Button(
    "Hide", key = "-Hide-", size = (15, 1), font = ("Consolas", 11)
)

btn3 = sg.Button("Open", size = (15, 1),  font = ("Consolas", 11), key = "-OPEN-")

layout_top = [btn, btn2, btn3]

#!Base Column 1
mline = sg.Multiline(
        default_text = "", auto_refresh = True,
        background_color = "#282c34", expand_x = True, expand_y = True,
        font = ("Consolas", 12, ITALIC), text_color = "#c1c4c8",
        enable_events = True, reroute_cprint = True, 
        key = "-CODE-", no_scrollbar = True
    )

visib = True
base_column_left = sg.Column(
        [[mline]], expand_x = True, expand_y = True, background_color = "#21252b", key = "-CL-",
        visible = visib
    )

#! Base Column 2
outputline = sg.Multiline(
    expand_x = True, expand_y=True, background_color = "#21252b", font = ("Consolas", 11, ITALIC),
    key = "-OUT-", text_color = "white", autoscroll = True
)

list_box = sg.Listbox(
    os.listdir(), expand_x = True, expand_y = True, horizontal_scroll = True,
    background_color = "#21252b", text_color = "white", no_scrollbar = False,
    font = ("Consolas", 11, ITALIC), right_click_menu = ["", ["  Show/Hide  "]],
    select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, enable_events = True, key = "-BOX-"
)

sg.theme("Black")

layout = [
    layout_top,
    [sg.pin(base_column_left, expand_x = True, expand_y = True, shrink=False)
    ,
    sg.Column(
        [
            [
                sg.Column(
                    [[sg.Btn("Full Screen")]], expand_x = True, expand_y =True
                ), 
                sg.Column(
                    [[list_box]], expand_x = True, expand_y = True
                )
            ],
            [
                sg.TabGroup(
                    [[
                        sg.Tab("Output", [[outputline]]), 
                        sg.Tab("Error", [[sg.Multiline(
                            expand_x = True, expand_y=True, background_color = "#21252b",
                            font = ("Consolas", 11, ITALIC), key = "-ERROR-", text_color = "white",
                            enable_events = True)
                            ]])
                    ]], expand_y = True, expand_x = True
                )
            ]
        ], 
        expand_x = True, expand_y = True,
        key = "-FOLDERS-", background_color = "#21252b")
    ]
] 

window = sg.Window(
    "Code Editor", layout, background_color = "#21252b", size = (1200, 800),
    no_titlebar = False, right_click_menu = ["", ["Exit"]], grab_anywhere = True,
    alpha_channel = 1, right_click_menu_font = ("Consolas", 11), right_click_menu_tearoff = False,
    finalize = True,  #return_keyboard_events=True
)

class TextRedirector():
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.update(f"{str}\n{'-' * 60}\n", append = True)
    
    def flush(self):
        pass

sys.stdout = TextRedirector(window["-OUT-"])
sys.stderr = TextRedirector(window["-OUT-"])

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    
    if event == "-OPEN-":
        open_file(window, sg, askopenfilename)

    if event == "-BOX-":
        open_from_box(window, values)

    if event == "-Hide-":
        print(window['-ERROR-'].get_size())

    if event == "-BTN-":
        run_code(values["-CODE-"], "this_file.py")
        pass
        

    if event == "Full Screen":
        window.Maximize()


    auto_complete(window)
    
window.close()
