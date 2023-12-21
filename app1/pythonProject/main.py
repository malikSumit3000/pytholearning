import functions
import time

now = time.strftime("%d-%b-%y %H:%M:%S")
print(now)


while True:
    user_input = input("Type add, show, edit, complete or exit :")
    user_input = user_input.strip()
    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_input.startswith("show"):
        print("The todo items :")

        todos = functions.get_todos()

        for n, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{n + 1}. {item.capitalize()}"
            print(row)

    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo :")
            try:
                todos[number] = new_todo + '\n'

                functions.write_todos(todos)

                print("Item replaced.")
            except IndexError:
                print("There is no item with that index")
                continue
        except ValueError:
            print("This command is not valid")
            continue
    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was completed"
            print(message)
        except IndexError:
            print("There is no item with that index")
            continue
        except ValueError:
            print("This command is not valid")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("This command is not valid!")

print("Bye!")
