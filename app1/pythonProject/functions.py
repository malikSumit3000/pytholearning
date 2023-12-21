file_path = 'todos.txt'


def get_todos(filepath=file_path):
    """ Read the text file and return the to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=file_path):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

