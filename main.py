from tkinter.font import ITALIC
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename
import os

import PySimpleGUI as sg
import keyboard

from functions import *


mline = sg.Multiline(
        default_text = "", auto_refresh = True,
        background_color = "#282c34", expand_x = True, expand_y = True,
        font = ("Verdana", 11, ITALIC), text_color = "#c1c4c8",
        enable_events = True, reroute_cprint = True, 
        key = "-CODE-", no_scrollbar = True
    )

btn = sg.Button(
        button_text = "Find", tooltip = "Search in all files",
        font = ("Verdana", 11),
        size = (15, 1), key = "-BTN-"
    )

btn2 = sg.Button(
    "Hide", key = "-Hide-", size = (15, 1), font = ("Verdana", 11)
)

btn3 = sg.Button("Open", size = (15, 1),  font = ("Verdana", 11), key = "-OPEN-")

list_box = sg.Listbox(
    os.listdir(), expand_x = True, expand_y = True, horizontal_scroll = True,
    background_color = "#21252b", text_color = "white", no_scrollbar = True,
    font = ("Verdana", 11, ITALIC), right_click_menu = ["", ["  Show/Hide  "]]
)

sg.theme("Black")

layout = [
    # [menubar],
    [btn, btn2, btn3], 
    [
    sg.Column([[mline]], expand_x = True, expand_y = True),
    sg.Column([[list_box]], expand_x = True, expand_y = True, pad = (0,0), key = "-FOLDERS-")
    ]
] 

window = sg.Window(
    "Code Editor", layout, background_color = "#21252b", size = (1000, 800),
    no_titlebar = True, right_click_menu = ["", ["Exit"]], grab_anywhere = True,
    alpha_channel = 1, right_click_menu_font = ("Verdana", 11), right_click_menu_tearoff = False,
    # return_keyboard_events=True
)

keyboard.add_hotkey("ctrl+o", lambda: open_file(window, sg, askopenfilename))
keyboard.add_hotkey("shift + .", lambda: after_colon(keyboard)) #:

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    
    if event == "-OPEN-":
        open_file(window)
    
    auto_complete(window)
    
    # elif event == '-Hide-':
    #     window['-FOLDERS-'].update(visible=window['-FOLDERS-'].metadata == True)
    #     window['-FOLDERS-'].metadata = not window['-FOLDERS-'].metadata
    #     window['-Hide-'].update(text= "Show" if window['-FOLDERS-'].metadata else "Hide")
window.close()
