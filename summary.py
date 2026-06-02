from file_handler import read_expenses


def show_summary():

    expenses = read_expenses()

    totals = {}

    for expense in expenses:

        amount = float(expense[0])

        category = expense[1]

        if category in totals:

            totals[category] += amount

        else:

            totals[category] = amount

    print("\nSummary\n")

    for category, total in totals.items():

        print(
            f"{category}: ₹{total}"
        )
