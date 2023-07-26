def get_todos(filepath="todos.txt"):
    """Read todo items from the text file
    and returns the list of todos"""

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_param, filepath="todos.txt"):
    """write new todo list back to the text file"""

    with open(filepath, "w") as file:
        file.writelines(todos_param)


if __name__ == "__main__":
    print("The file directly executed")
# if __name__ == "functions":
#     print("this file excuted due to the import in main")
