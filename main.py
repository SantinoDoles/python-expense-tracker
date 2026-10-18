from datetime import datetime

def view_history():
    print("\n--- Expense History ---")

    try:
        with open("expenses.txt", "r") as file:
            history = file.read()
            print(history)

    except FileNotFoundError:
        print("No expense history found. Add expenses first!")

def main_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expenses")
    print("2. View Expense History")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    return choice

def add_expenses():
    print("Let's add your expenses!")


    while True:
        try:
            income = float(input("Enter your monthly income: $"))
        
            if income < 0:
                print("Invalid input! Income cannot be negative.")
                continue

            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"Your monthly income is ${income:.2f}")
    while True:
        try:
            count = int(input("How many expenses would you like to enter? "))
        
            if count <= 0:
                print("Please enter at least 1 expense.")
                continue 

            break
        
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    expenses = []
    categories = []

    for i in range(count):
        category = input("Enter a category: ")
        
        while True:
            try:
                amount = float(input("Enter the amount: $"))
                
                if amount < 0:
                    print("Invalid input! Please enter a positive number.")
                    continue
                
                break
            except ValueError:
                print("Invalid amount! Please enter a number.")

        expenses.append(amount)
        categories.append(category)




    expense = sum(expenses)
    highest = max(expenses)
    lowest = min(expenses)
    average = expense / len(expenses)
    balance = income - expense
    if income > 0:
        spending_percentage = (expense / income) * 100
    else:
        spending_percentage = 0
    print(f"Your remaining balance is ${balance:.2f}")

    if balance < 0:
        print("Warning! You are over budget!")
    elif balance == 0:
        print("You have used your entire budget!")
    else:
        print("Great job! You are within your budget!")

    print("\n----- EXPENSE SUMMARY -----")
    for i in range(count):
        if income > 0:
            category_percentage = (expenses[i] / income) * 100
        else:
            category_percentage = 0
        
        print(f"{categories[i]}: ${expenses[i]:.2f} ({category_percentage:.1f}%)")
    print("---------------------------")
    print(f"Total Expenses: ${expense:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")
    print(f"Income Spent: {spending_percentage:.1f}%")
    print(f"Highest expense: ${highest:.2f}")
    print(f"Lowest expense: ${lowest:.2f}")
    print(f"Average expense: ${average:.2f}")

    now = datetime.now()
    formatted_date = now.strftime("%m/%d/%Y %I:%M %p")

    with open("expenses.txt", "a") as file:
        file.write("\n---------------------\n")
        file.write("My Expense Tracker\n")
        file.write(f"Date: {formatted_date}\n")
        
        for i in range(count):
            if income > 0:
                category_percentage = (expenses[i] / income) * 100
            else:
                category_percentage = 0

            file.write(f"{categories[i]}: ${expenses[i]:.2f} ({category_percentage:.1f}%)\n")

        file.write(f"Monthly Income: ${income:.2f}\n")
        file.write(f"Total Expenses: ${expense:.2f}\n")
        file.write(f"Remaining Balance: ${balance:.2f}\n")
        file.write(f"Income Spent: {spending_percentage:.1f}%\n")
while True:
    choice = main_menu()

    if choice == "1":
        add_expenses()

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("Thank you for using Expense Tracker!")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        break


