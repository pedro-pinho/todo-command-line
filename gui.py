from modules import functions
import PySimpleGUI as sg
import time

sg.theme('DarkTeal2')   # Add a touch of color
todos = functions.get_todos()

# All the stuff inside your window.
input_text = sg.InputText(tooltip="Enter to-do", key='todo', do_not_clear=False, size=46)
list_box = sg.Listbox(values=todos, key='todos', size=(45, 10), enable_events=True)
clock_text = sg.Text('', key='clock')
layout = [[clock_text],
          [sg.Text('Type in a to-do')],
          [input_text, sg.Button('Add')],
          [list_box, sg.Button('Edit'), sg.Button('Complete')],
          [sg.Button('Exit')]]

# Create the Window
window = sg.Window('My To-Do App',
                   layout,
                   font=('Helvetica', 20))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    # Display the window
    event, values = window.read(timeout=200)

    now = time.strftime("%b %d, %Y %H:%M:%S")
    window['clock'].update(value=now)

    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
    if event == 'Add':
        todos.append(values['todo'] + '\n')
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    if event == 'Edit':
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 20))
    if event == 'Complete':
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 20))
    if event == 'todos':
        window['todo'].update(value=values['todos'][0])
window.close()
