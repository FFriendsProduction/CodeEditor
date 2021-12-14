def auto_complete(window):
    try:
        li = ["("]
        if window["-CODE-"].get()[-1] in li:
            window["-CODE-"].update(")", append = True)
        
    except:
        print("auto_complete")

def after_colon(keyboard):
    keyboard.send("enter")
    keyboard.write("    ")

def open_file(window, sg, askopenfilename):
    try:
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        with open(filepath, "r") as input_file:
            text = input_file.read()
            window["-CODE-"].update(text)
    except:
        sg.popup("Somethings went wrong", title = "Error")


# def dosya_kaydet():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = metin.get(1.0, END)
#         output_file.write(text)
#     pencere.title(f"Simple Text Editor - {filepath}")
