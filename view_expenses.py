from file_handler import read_expenses


def view_expenses():

    expenses = read_expenses()

    if len(expenses) == 0:

        print("No expenses found")

        return

    print("\nExpenses\n")

    count = 1

    for expense in expenses:

        print(
            f"{count}. ₹{expense[0]} - {expense[1]}"
        )

        count += 1
