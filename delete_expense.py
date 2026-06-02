from file_handler import read_expenses
from file_handler import overwrite_expenses


def delete_expense():

    expenses = read_expenses()

    if len(expenses) == 0:

        print("No expenses to delete")

        return

    for index, expense in enumerate(expenses):

        print(
            f"{index + 1}. ₹{expense[0]} - {expense[1]}"
        )

    choice = int(
        input("Select expense number: ")
    )

    if choice < 1 or choice > len(expenses):

        print("Invalid selection")

        return

    expenses.pop(choice - 1)

    overwrite_expenses(expenses)

    print("Expense Deleted")
