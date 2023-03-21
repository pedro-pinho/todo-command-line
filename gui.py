from modules import functions
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
todos = functions.get_todos()

# All the stuff inside your window.
layout = [[sg.Text('Type in a to-do'), sg.InputText(tooltip="Enter to-do", key='todo', do_not_clear=False), sg.Button('Add')],
          [sg.Listbox(values=todos, key='todos', size=(45, 10), enable_events=True), sg.Button('Edit')],
          [sg.Button('Exit')]]

# Create the Window
window = sg.Window('My To-Do App',
                   layout,
                   font=('Helvetica', 20))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    # Display the window
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
    if event == 'Add':
        todos.append(values['todo'] + '\n')
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    if event == 'Edit':
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']
        index = todos.index(todo_to_edit)
        todos[index] = new_todo + '\n'
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    if event == 'todos':
        window['todo'].update(value=values['todos'][0])

window.close()
