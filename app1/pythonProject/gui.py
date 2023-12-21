import functions
import PySimpleGUI as gui

label = gui.Text("Type in a To-Do")
input_box = gui.InputText()
add_button = gui.Button("ADD")

window = gui.Window("To-Do manager", layout=[[label], [input_box, add_button]])
window.read()
window.close()