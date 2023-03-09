FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the to-do file and return it's content. """
    with open(filepath, "r") as file_todos:
        result = file_todos.readlines()
    return result


def write_todos(todos_to_write, filepath=FILEPATH):
    """ Open the to-do file and write content. """
    with open(filepath, "w") as file_todos:
        file_todos.writelines(todos_to_write)


# print(__name__)
if __name__ == "__main__":
    print("This is only executed on running this file, not on importing")
