
def show_menu():
    print("/n----------Personal Expense Tracker----------")
    print("1. Add Expense")
    print("2. View Monthly Expense")
    print("3. Category-wise Monthly Report")
    print("4. Exit")

import tkinter as tk
from tkinter import messagebox

import csv
from datetime import datetime

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_expense():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if validate_date(date):
            break
        else:
            print("Invalid date format. Try again.")

    category = input("Enter category (Food, Travel, etc): ")

    while True:
        amount = input("Enter amount: ")
        if amount.replace('.', '', 1).isdigit():
            amount = float(amount)
            break
        else:
            print("Amount must be a number. Try again.")

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("----------Expense added successfully----------")


def view_monthly_expense():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"].startswith(month):
                    total += float(row["amount"])

        print("-" * 40)
        print(f"Total expense for {month}: {total}")
        print("-" * 40)

    except FileNotFoundError:
        print("No expense data found.")

def category_wise_report():
    month = input("Enter month (YYYY-MM): ")
    category_total = {}
    grand_total = 0

    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"].startswith(month):
                    category = row["category"]
                    amount = float(row["amount"])

                    grand_total += amount

                    if category in category_total:
                        category_total[category] += amount
                    else:
                        category_total[category] = amount

        if not category_total:
            print("No expenses found for this month.")
        else:
            print(f"\n Category-wise expense for {month}")
            for cat, total in category_total.items():
                print(f"{cat} : {total}")

            print("-" * 23)
            print(f"TOTAL : {grand_total}")
            print("-" * 23)

    except FileNotFoundError:
        print("Expense file not found.")

def main():
    while True:
        show_menu()
        choice = input("Enter Your Choice (1-4):")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_monthly_expense()
        elif choice == "3":
            category_wise_report()
        elif choice == "4":
            print("Thank You Exiting.....")
            break
        else:
            print("Invalid Choice_Try Agian.")

def add_expense_gui():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if not validate_date(date):
        messagebox.showerror("Error", "Invalid date format (YYYY-MM-DD)")
        return

    if not amount.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Amount must be a number")
        return

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    messagebox.showinfo("Success", "Expense added successfully!")

    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def monthly_report_gui():
    month = month_entry.get()
    total = 0

    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"].startswith(month):
                    total += float(row["amount"])

        messagebox.showinfo(
            "Monthly Expense",
            f"Total expense for {month}: {total}"
        )

    except FileNotFoundError:
        messagebox.showerror("Error", "Expense file not found")

def category_report_gui():
    month = month_entry.get()
    category_total = {}
    grand_total = 0

    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["date"].startswith(month):
                    category = row["category"]
                    amount = float(row["amount"])

                    grand_total += amount

                    if category in category_total:
                        category_total[category] += amount
                    else:
                        category_total[category] = amount

        if not category_total:
            messagebox.showinfo("Category Report", "No data found for this month")
            return

        report_text = f"Category-wise Expense for {month}\n\n"
        for cat, total in category_total.items():
            report_text += f"{cat} : {total}\n"

        report_text += "-" * 25 + "\n"
        report_text += f"TOTAL : {grand_total}"

        messagebox.showinfo("Category Report", report_text)

    except FileNotFoundError:
        messagebox.showerror("Error", "Expense file not found")


root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("420x420")
root.configure(bg="#f5f5f5")


heading = tk.Label(
    root,
    text="Personal Expense Tracker",
    font=("Segoe UI", 18, "bold"),
    bg="#f5f5f5",
    fg="#333"
)
heading.pack(pady=15)


# Date
date_label = tk.Label(
    root,
    text="Date (YYYY-MM-DD)",
    font=("Segoe UI", 10),
    bg="#f5f5f5"
)

date_label.pack()
date_entry = tk.Entry(root, width=30, font=("Segoe UI", 10))
date_entry.pack(pady=5)

# Category
category_label = tk.Label(
    root,
    text="category",
    font=("Segoe UI", 10),
    bg="#f5f5f5"
)
category_label.pack()
category_entry= tk.Entry(root, width=30, font=("Segoe UI", 10))
category_entry.pack(pady=5)

# Amount
amount_label = tk.Label(
    root,
    text="Amount",
    font=("Segoe UI", 10),
    bg="#f5f5f5"
)
amount_label.pack()
amount_entry = tk.Entry(root, width=30, font=("Segoe UI", 10))
amount_entry.pack(pady=5)

add_button = tk.Button(
    root,
    text="Add Expense",
    command=add_expense_gui,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=20
)
add_button.pack(pady=12)


#month
month_label = tk.Label(
    root,
    text="Month (YYYY-MM)",
    font=("Segoe UI", 10),
    bg="#f5f5f5"
)
month_label.pack()
month_entry = tk.Entry(root, width=30, font=("Segoe UI", 10))
month_entry.pack(pady=5)

monthly_button = tk.Button(
    root,
    text="View Monthly Expense",
    command=monthly_report_gui,
    bg="#2196F3",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=20
)
monthly_button.pack(pady=10)

category_button = tk.Button(
    root,
    text="View Category-wise Expense",
    command=category_report_gui,
    bg="#9C27B0",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=20
)
category_button.pack(pady=10)

root.mainloop()

#main()
