from file_handler import save_expense
from validator import valid_amount


def add_expense():

    amount = input("Enter amount: ")

    if not valid_amount(amount):

        print("Invalid amount")

        return

    category = input("Enter category: ")

    save_expense(amount, category)

    print("Expense Added")
