
import locale
locale.setlocale(locale.LC_ALL, "en_GB.UTF-8")



user = {
    "tathianareis": {"name": "Tathiana", "pin": "1234"},
    "paulwilliams": {"name": "Paul", "pin": "4321"},
}

expense = {}


# Supporting functions:

# Validate and convert to a float
def validate_and_parse(amount):
    try:
        # Convert formatted string to a float
        value = locale.atof(amount)
        return value
    except ValueError:
        raise ValueError("Invalid amount format for locale")
    
# Format currency
def format_as_currency(value):
    return locale.format_string('%.2f', value, grouping=True)


def login():
    userId = input("\nEnter username: ").lower()
    pin = input("\nEnter pin number: ")

    try:
        # Validate PIN length and numeric value
        if len(pin) != 4:
            raise ValueError("Pin must be exactly 4 digits.")
        if not pin.isdigit():
            raise ValueError("Pin must be numeric.")

        # Check if the entered userId exists and the pin matches
        if userId in user and user[userId]["pin"] == pin:
            print(f"\nWelcome, {user[userId]['name']}!")
            log_expense()
        else:
            raise ValueError("Invalid username or pin.")
        
    except ValueError as e:
        print(f"\n{e}. Please try again.")
        login()  # Recursively call login to allow another attempt
        

def log_expense():    
  
    # Initialize the expense dictionary if it doesn't exist
    global expense
    try:
        expense
    except NameError:  #A NameError occurs when you try to access a variable that hasn’t been assigned or defined yet.
        expense = {}
    
    # Get the expense description
    while True:
        expenseDescription = input("\nEnter expense description: ").strip()
        if expenseDescription:
            break
        print("Expense description cannot be empty. Please try again.")

    # Get the expense amount
    while True:
        expenseAmount = input("\nEnter expense amount: ").strip()
        try:
            validated_amount = validate_and_parse(expenseAmount)
            formatted_value = format_as_currency(validated_amount)
            expenseAmount = formatted_value
            break
        except ValueError:
            print("Expense amount must be a numeric value. Please try again.")
    
    # Get the expense category
    while True:
        expenseCategory = input("\nEnter expense category: ").strip()
        if expenseCategory:
            break
        print("Expense category cannot be empty. Please try again.")

    # Add the expense to the dictionary
    expense[expenseDescription] = {"amount": expenseAmount, "category": expenseCategory}
    print(f"\nExpense '{expenseDescription}' added successfully!")
    print("Would you like to add another expense?")
    answer = input("Would you like to add another expense? (yes/no): ").strip().lower()
    if answer in ["yes", "y"]:
        log_expense()
    else:
        display_summary()
        view_expense()

    
        
def view_expense():
    if not expense:  # Check if the expense dictionary is empty
        print("\nNo expenses to show.")
        return

    print("\nList of Expenses:")
    for description, details in sorted(expense.items()):  # Sort by the keys (descriptions)
        amount = details["amount"]
        category = details["category"]
        print(f"- {description}: Amount = {amount}, Category = {category}")
        
def display_summary():
    if not expense:  # Check if the expense dictionary is empty
        print("\nNo expenses to show.")
        return

    print("\nExpenses Summary:")
    totalAmount = 0
    category_totals = {}
    for description, details in sorted(expense.items()):  # Sort by the keys (descriptions)
        totalAmount += float(details["amount"]) 
        category = details["category"]
        amount = float(details["amount"])
        if category in category_totals:
             category_totals[category] += amount
        else:
            category_totals[category] = amount
    print(f"Total amount spent = {totalAmount}")    
    print("Total Amount Spent in Each Category:")
    for category, total in category_totals.items():
        print(f"- {category}: {total}")


login()
#display_summary()
#view_expense()

print(expense)
    
    
  
    

