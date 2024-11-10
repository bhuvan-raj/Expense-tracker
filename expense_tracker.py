import csv
from datetime import datetime

def add_expense():
    amount = input("Enter the amount: ")
    category = input("Enter the category (e.g., Food, Transport, etc.): ")
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("Expense added successfully.")

def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        print("Date\t\tCategory\tAmount")
        print("-" * 30)
        for row in reader:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

def filter_expenses(filter_type, filter_value):
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        print("Date\t\tCategory\tAmount")
        print("-" * 30)
        for row in reader:
            if (filter_type == 'category' and row[1] == filter_value) or \
               (filter_type == 'date' and row[0] == filter_value):
                print(f"{row[0]}\t{row[1]}\t{row[2]}")

def summarize_expenses():
    total_expenses = 0
    category_totals = {}
    
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            amount = float(row[2])
            total_expenses += amount
            category_totals[row[1]] = category_totals.get(row[1], 0) + amount
    
    print(f"Total Expenses: {total_expenses}")
    print("Expenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: {total}")

def menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Summarize Expenses")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_type = input("Filter by 'category' or 'date': ")
            filter_value = input("Enter the value to filter by: ")
            filter_expenses(filter_type, filter_value)
        elif choice == '4':
            summarize_expenses()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
