# hello_world.py
from typing import List, Any

# import PySimpleGUI as sg
#
# layout = [
#     [
#
#      sg.Button('Enter image'),
#     ]
# ],
# sg.Window("Object detection app", layout , margins=(200, 100),resizable=True).read()

import io
import os
import PySimpleGUI as sg
from PIL import Image
file_types = [("JPEG (*.jpg)", "*.jpg"),

              ("All files (*.*)", "*.*")]
def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Enter Image"),
            sg.Button("Predict"),
        ],
    ]
    window = sg.Window("Object detection app", layout, resizable=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Enter Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
    window.close()
if __name__ == "__main__":
    main()