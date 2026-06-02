import csv

FILE_PATH = "../data/expenses.csv"


def read_expenses():

    expenses = []

    try:

        with open(FILE_PATH, "r") as file:

            reader = csv.reader(file)

            for row in reader:

                expenses.append(row)

    except FileNotFoundError:

        pass

    return expenses


def save_expense(amount, category):

    with open(FILE_PATH, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([amount, category])


def overwrite_expenses(expenses):

    with open(FILE_PATH, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(expenses)
