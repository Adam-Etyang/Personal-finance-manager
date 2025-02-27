import mysql.connector
from datetime import datetime
import os

#clearing the screen
def clear_screen():
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # macOS/Linux
    else:
        _ = os.system('clear')

#establishing connection to the database
def database_connection():
    try:
        
        db = mysql.connector.connect(
            host="localhost",
            user=input("enter your database username: "),
            password = input("enter your database password: "),
            database= "personalfinancedb"
        )

        cursor = db.cursor() #pointer that sends queries to the database and retrieves results
        print("database connection succesfull")
        return db, cursor
    except mysql.connector.Error as err:
        print(f"failed to connect to the database : {err}")
        return None, None


# function to send the query to the database and handle errors with the query
def execute_query(cursor , db, query,params = None) :
    try:
        cursor.execute(query,params or ()) # executes the query
        db.commit() # commits changes
        return True
    except mysql.connector.Error as err:
        print(f"error: {err}")
        db.rollback() # rollback changes
        return False

#CLI commands

#add accounts   
def add_account(cursor, db):

    account_name = input("enter account name: ")
    account_type = input("enter account type [saving, current,credit card]: ")
    while account_type not in ["saving", "current" , "credit card"]:
        print("invalid type")
        account_type = input("enter account type [saving, current,credit card]: ")
    balance = float(input("enter initial balance: "))
    institution = input("enter institution: ")

    query = """INSERT INTO accounts 
    (account_name, account_type, balance, institution) 
    VALUES (%s,%s,%s,%s)"""
    params = (account_name, account_type, balance, institution)
    if execute_query(query,params):
        print(f"account '{account_name}'created successfuly ")
    else:
        print("account creation failed")




#view accounts
def view_accounts(cursor):
    print("\n ===== VIEW ALL ACCOUNTS =====")

    query = """SELECT account_id, account_name, account_type, balance, institution FROM accounts"""
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\n accounts: ")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Balance{row[3]}, Institution{row[4]}")
    else:
        print("no accounts found.")


#add transactions
def add_transaction(cursor,db):
    account_id = int(input("enter account id: "))
    date = input("enter date (YYYY-MMM-DD): ")
    amount = float(input("input enter amount: "))
    description = input("enter description of the transaction: ")
    category_id = input("enter category ID(-1 for none): ")
    category_id  = int(category_id) if category_id != "-1" else None
    transaction_type = input("enter transaction type(income/expense): ")
    while transaction_type not in ["income", "expense"]:
        print("invalid choice")
        transaction_type = input("enter transaction type(income/expense): ")

    query = """INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) VALUES (%s,%s, %s, %s, %s, %s);"""
    params = (account_id, date, amount, description, category_id ,transaction_type)
    if execute_query(query, params):
        print(f"transaction'{description}' added succesfully")

    else:
        print("transaction failed!")

    #view transations
def view_transaction(cursor):
    print("==== VIEW ALL TRANSACTIONS ====")
    query = """SELECT t.account_id, t.date, t.amount, t.description, t.category_id, t.transaction_type 
               FROM Transactions t
               LEFT JOIN categories c ON t.category_id = c.category_id
               WHERE t.account_id = %s 
               ORDER BY t.date  DESC"""
    cursor.execute(query, (args.account_id))
    results = cursor.fetchall()
    if results:
        print(f"\n transactions for account ID {args.account_id}: ")
        for row in results:
            print(f"ID: {row[0]}, Date: {row[1]}, Amount: {row[2]}, Description: {row[3]}, Category: {row[4] or 'None'}, Type: {row[5]}")

    else:
        print(f"transactions not found for account {args.account_id}.")


# add categories
def add_category(cursor,db):
    print("==== ADD A NEW CATEGORY ====")
    category_name = input("Enter category name: ")
    parent_category_id = input("enter parent category ID(-1 for none): ")
    parent_category_id = int(parent_category_id) if parent_category_id != "-1" else None

    
    query = """INSERT INTO categories (category_name, parent_category_id) 
VALUES (%s, %s);"""
    params = (category_name, parent_category_id)
    if execute_query(query,params):
        print(f"category '{category_name}' added succesfully")
    else:
        print("category addition failed")

#view categories
def view_category(cursor):
    print("==== VIEW CATEGORIES ==== ")
    query = """SELECT c.category_id, c.category_name, p.category_name AS parent_category_name
    FROM categories c
    LEFT JOIN categories p ON c.parent_category_id = p.category_id
    """ 
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\n categories: ")
        for row in results:
            print(f"category id: {row[0]}, Name: {row[1]},Parent: {row[2] or 'None'}")
        else:
            print("categories not found")


#add budgets
def add_budgets(cursor,db):
    print("==== ENTER A BUDGET ====")
    category_id = int(input("Enter category ID: "))
    start_date = input("enter the start date(YYYY-MM-DDD) : ")
    end_date = input("Enter the end date(YYYY-MM-DD): ")
    amount = float(input("enter the amount: "))
    


    query = """INSERT INTO Budgets (category_id, start_date, end_date, amount) 
VALUES (%s, %s, %s, %s);"""

    params = (category_id,start_date,end_date,amount)
    if execute_query(query,params):
        print("budget added successfully")
    else:
        print("Budget addition failed")


#view budgets
def view_budgets(cursor):
    print("==== VIEW ALL BUDGETS ====")
    query = """SELECT b.budget_id, c.category_id, b.start_date, b.end_date, b.maount
                From budgets b 
                JOIN categories c ON b.category_id = c.category_id"""
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\n budgets: ")
        for row in results:
            print(f"ID: {row[0]}, Category: {row[1]}, Start: {row[2]}, End: {row[3]}, Amount: {row[4]}")
        else:
            print("No budgets found")

#add goals
def add_goals(cursor,db):
    print("==== ADD GOALS ====")
    goal_name = input("enter the goal name: ")
    target_amount = float(input("Enter the target amount: "))
    current_amount= float(input("Enter the current amount: "))
    due_date = input("enter due date(YYYY-MM-DD) :")
    category_id = input("Enter category ID: ")
    category_id = int(category_id) if category != -1 else None

    query = """INSERT INTO Goals (goal_name, target_amount, current_amount, due_date, category_id) 
VALUES (%s, %s, %s, %s, %s);"""
    params = (goal_name, target_amount, current_amount, due_date, category_id )
    if execute_query(query,params):
            print(f"Goal '{goal_name}' added successfully")
    else:
        print("Goal addition failed")
#view goals
def view_goals(cursor):
    print("==== VIEW FINANCIAL GOALS ====")

    query = """SELECT g.goal_id, g.goal_name, g.target_amount, g.current_amount, g.due_date, c.category_name 
               FROM Goals g 
               LEFT JOIN Categories c ON g.category_id = c.category_id"""
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\n goals")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Target: {row[2]}, Current: {row[3]}, Due: {row[4]}, Category: {row[5] or 'None'}")
    else:
        print("No goals found")


#main function

def main():
    clear_screen()

    #database connection
    db,cursor = database_connection()
    
    if db and cursor:

        while True:
            print("\n ==== Personal Finance Tracker ==== ")
            print("++++CHOOSE YOUR OPTION++++")

            print("\n 1. Add Account")
            print("\n 2. View Accounts")
            print("\n 3. Add Transaction")
            print("\n 4. View Transactions")
            print("\n 5. Add Category")
            print("\n 6. View Categories")
            print("\n 7. Add Budget")
            print("\n 8. View Budgets")
            print("\n 9. Add Goal")
            print("\n 10. View Goals")
            print("\n 11. Exit")
        
            choice = input("Enter your choice (1-11): ")  
            if choice == "1":
                add_account(cursor,db)
            elif choice == "2":
                view_accounts(cursor)
            elif choice == "3":
                add_transaction(cursor,db)
            elif choice == "4":
                view_transactions(cursor)
            elif choice == "5":
                add_category(cursor,db)
            elif choice == "6":
                view_categories(cursor)
            elif choice == "7":
                add_budgets(cursor,db)
            elif choice == "8":
                view_budgets(cursor)
            elif choice == "9":
                add_goals(cursor,db)
            elif choice == "10":
                view_goals(cursor)
            elif choice == "11":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 11.")
        cursor.close()
        db.close()
    else:
        print("database connection failed")

if __name__ == '__main__':
    main()



