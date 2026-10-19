import pandas as pd
import matplotlib.pyplot as plt
import os


FILE_NAME = "expenses.csv"



# CREATE CSV FILE


def create_file():

    if not os.path.exists(FILE_NAME):

        data = {
            "Date": [],
            "Type": [],
            "Category": [],
            "Amount": [],
            "Description": []
        }

        df = pd.DataFrame(data)

        df.to_csv(FILE_NAME, index=False)



# ADD TRANSACTION


def add_transaction():

    date = input("Enter date (YYYY-MM-DD): ")

    print("\n1. Income")
    print("2. Expense")

    choice = input("Select type: ")

    if choice == "1":
        transaction_type = "Income"

    elif choice == "2":
        transaction_type = "Expense"

    else:
        print("Invalid choice!")
        return

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Enter description: ")

    new_data = {
        "Date": date,
        "Type": transaction_type,
        "Category": category,
        "Amount": amount,
        "Description": description
    }

    df = pd.DataFrame([new_data])

    df.to_csv(
        FILE_NAME,
        mode="a",
        header=False,
        index=False
    )

    print("\nTransaction added successfully!")



# VIEW TRANSACTIONS


def view_transactions():

    df = pd.read_csv(FILE_NAME)

    if df.empty:

        print("\nNo transactions found.")

    else:

        print("\n========== TRANSACTIONS ==========")

        print(df.to_string(index=False))


# FINANCIAL SUMMARY


def financial_summary():

    df = pd.read_csv(FILE_NAME)

    if df.empty:

        print("\nNo transactions available.")
        return

    income = df[
        df["Type"] == "Income"
    ]["Amount"].sum()

    expense = df[
        df["Type"] == "Expense"
    ]["Amount"].sum()

    balance = income - expense

    print("\n========== FINANCIAL SUMMARY ==========")

    print(f"Total Income  : ₹{income:.2f}")

    print(f"Total Expense : ₹{expense:.2f}")

    print(f"Balance       : ₹{balance:.2f}")



# CATEGORY ANALYSIS


def category_analysis():

    df = pd.read_csv(FILE_NAME)

    expense_df = df[
        df["Type"] == "Expense"
    ]

    if expense_df.empty:

        print("\nNo expenses available.")

        return

    category_total = (
        expense_df
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========== CATEGORY ANALYSIS ==========")

    print(category_total)

    highest_category = category_total.idxmax()

    highest_amount = category_total.max()

    print(
        f"\nHighest spending category: "
        f"{highest_category}"
    )

    print(
        f"Amount spent: ₹{highest_amount:.2f}"
    )

# MONTHLY ANALYSIS


def monthly_analysis():

    df = pd.read_csv(FILE_NAME)

    if df.empty:

        print("\nNo transactions available.")

        return

    df["Date"] = pd.to_datetime(
        df["Date"]
    )

    df["Month"] = df["Date"].dt.to_period("M")

    monthly_expenses = (
        df[df["Type"] == "Expense"]
        .groupby("Month")["Amount"]
        .sum()
    )

    print("\n========== MONTHLY EXPENSES ==========")

    print(monthly_expenses)



# SPENDING PATTERN


def spending_pattern():

    print("\n========== SPENDING PATTERN ==========")

    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No expenses available.")
        return

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.to_period("M")

    monthly = df.groupby("Month")["Amount"].sum()

    if len(monthly) < 2:
        print("Add expenses for at least 2 months.")
        return

    print("\nMonthly Spending:")

    print(monthly)

    highest_month = monthly.idxmax()
    lowest_month = monthly.idxmin()

    print("\nHighest spending month:")
    print(highest_month, "₹", round(monthly.max(), 2))

    print("\nLowest spending month:")
    print(lowest_month, "₹", round(monthly.min(), 2))

    average = monthly.mean()

    print("\nAverage monthly spending: ₹", round(average, 2))


# EXPENSE CHART

def expense_chart():

    df = pd.read_csv(FILE_NAME)

    expense_df = df[
        df["Type"] == "Expense"
    ]

    if expense_df.empty:

        print("\nNo expenses available.")

        return

    category_total = (
        expense_df
        .groupby("Category")["Amount"]
        .sum()
    )

    plt.figure(figsize=(8, 5))

    category_total.plot(
        kind="bar"
    )

    plt.title("Expense by Category")

    plt.xlabel("Category")

    plt.ylabel("Amount")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()



# MAIN MENU


def main():

    create_file()

    while True:

        print("\n")
        print("====================================")
        print("       EXPENSE TRACKER")
        print("====================================")

        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Financial Summary")
        print("4. Category Analysis")
        print("5. Monthly Analysis")
        print("6. Spending Pattern")
        print("7. Expense Chart")
        print("8. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            add_transaction()

        elif choice == "2":

            view_transactions()

        elif choice == "3":

            financial_summary()

        elif choice == "4":

            category_analysis()

        elif choice == "5":

            monthly_analysis()
        elif choice == "6":

            spending_pattern()

        elif choice == "7":

            expense_chart()

        elif choice == "8":

            print(
                "\nThank you for using "
                "Expense Tracker!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-8."
            )


# PROGRAM START

if __name__ == "__main__":

    main()