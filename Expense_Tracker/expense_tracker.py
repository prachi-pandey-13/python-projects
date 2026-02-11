# PERSONAL FINANCE APP EXPENSE TRACKER
print("==========WELCOME TO EXPENSE TRACKER 💸==========")
expenselist = []
while True:

    print("========MENU===========")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    print("========================")

    choice = int(input("Enter your choice : "))

    if(choice == 1):
        print("Add your Expense:--------")
        date = input("Enter date of expense : ")
        category = input("Enter category : ")
        details = input("Enter details : ")
        amount = int(input("Enter amount : "))
        expenses = {
            "Date" : date,
            "Category" : category,
            "Details" : details,
            "Amount" : amount
        }
        expenselist.append(expenses)
        print("Add Expense Successfully")

    elif(choice == 2):
        print("View your Expenses:----------")
        count = 1
        for item in expenselist:
            print(f"{count} -> 'Date' :- {item['Date']} -> 'Category' :- {item['Category']} -> 'Details :- {item['Details']} -> 'Amount' :- {item['Amount']}")
            count += 1

    elif(choice == 3):
        print("View your Total Spending:----------")
        total = 0
        for item in expenselist:
            total = total + item["Amount"]
        print("Total Spending :- ", total)

    elif(choice==4):
        print("====Thankyou for using the Expense Tracker====")
        break
    
    else:
        print("Invalid choice! Try Again!!")
