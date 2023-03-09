from modules import functions
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
todos = functions.get_todos()

# All the stuff inside your window.
layout = [[sg.Text('Type in a to-do'), sg.InputText(tooltip="Enter to-do"), sg.Button('Add')],
          [sg.Listbox(values=todos, select_mode='extended', key='fac', size=(30, 6))],
          [sg.Button('Exit')]]

# Create the Window
window = sg.Window('My To-Do App', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    # Display the window
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
        break
    if event == 'Add':
        todos.append(values[0] + '\n')
        functions.write_todos(todos)
        values[0] = ''

window.close()
