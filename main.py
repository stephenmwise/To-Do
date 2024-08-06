import functions
import time

now = time.strftime("%xb %d, %Y %H:%M:%S")
print(f"It is {now}")

#Begin main loop
while True:
    user_action = input("Options: Add, View, Edit, Complete, Exit: ")
    user_action = user_action.capitalize().strip()
    #ADD user_action
    if user_action.startswith("Add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

        print(f"{todo} has been added to your list.")

    #VIEW user_action
    elif user_action.startswith("View"):
        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            print(f"{index+1}. {item}")

    #EDIT user_action
    elif user_action.startswith("Edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            newItem = input(f"Replace '{todos[number]}': ")
            todos[number] = newItem + "\n"

            print(f"'{newItem}' successfully added.")

            functions.write_todos(todos)

        #Exception ValueError
        except ValueError:
            print("Invalid input. Please enter a number.")

    #COMPLETE user_action
    elif user_action.startswith("Complete"):

        todos = functions.get_todos()

        try:
            finish = int(user_action[9:])
            finishedItem = todos[finish-1].strip("\n")
            todos.pop(finish - 1)

            functions.write_todos(todos)

            print(f"You completed: '{finishedItem}'")

        #Exceptions: ValueError and IndexError
        except ValueError:
            print("Please enter a number")
            continue
        except IndexError:
            print("No item with that number.")
            continue

    #EXIT user option
    elif user_action == "Exit":
        break

    #ELSE just print invalid input,then continue the main loop
    else:
        print("Invalid input. Please enter an option:")
    continue