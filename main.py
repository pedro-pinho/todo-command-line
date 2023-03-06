from modules import functions

while True:
    filepath_todo = "files/todos.txt"
    user_action = input('Type add, show, edit, complete or exit: ')
    # Strip from whitespaces
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # list comprehension
        # new_todos = [item.strip('\n').title() for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index+1}.{item}")
        # index and item still exist here, with the last value

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            existing_todo = todos[number]
            edited_todo = input("Enter the new value for this todo: ") + "\n"
            todos[number] = edited_todo

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command!")
            continue
        except IndexError:
            print("There's no item with that number")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[number].strip('\n').title()
            todos.pop(number)
            print(f"Todo {todo_to_remove} completed!")
            functions.write_todos(todos)

        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("There's no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Unknown command")

print('Bye!')
