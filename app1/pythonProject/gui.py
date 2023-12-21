import functions
import PySimpleGUI as gui
import time

gui.theme('LightGreen2')

clock = gui.Text(key='clock')
label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter todo", key='todo')
add_button = gui.Button("ADD", size=10)
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("EDIT")
complete_button = gui.Button("COMPLETE")
exit_button = gui.Button("EXIT")

window = gui.Window("To-Do manager", layout=[[clock],
                                             [label],
                                             [input_box, add_button],
                                             [list_box, edit_button, complete_button],
                                             [exit_button]], font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(time.strftime("%d-%b-%y %H:%M:%S"))

    match event:
        case 'ADD':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'EDIT':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select an item first", font=('Helvetica', 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'COMPLETE':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.remove(index)

                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup("Please select an item first", font=('Helvetica', 20))

        case 'EXIT':
            break

        case gui.WIN_CLOSED:
            break

window.close()
