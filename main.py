from menu import display_menu

from add_expense import add_expense

from view_expenses import view_expenses

from delete_expense import delete_expense

from summary import show_summary


while True:

    display_menu()

    choice = input("Choose option: ")

    if choice == "1":

        add_expense()

    elif choice == "2":

        view_expenses()

    elif choice == "3":

        delete_expense()

    elif choice == "4":

        show_summary()

    elif choice == "5":

        print("Goodbye")

        break

    else:

        print("Invalid option")
