import sqlite3
import pyfiglet
import datetime
from colorama import Fore

text = pyfiglet.figlet_format("ExpnessTracker")
print(Fore.LIGHTGREEN_EX + text)
con = sqlite3.connect("expnesstracker.db")
cursor = con.cursor()

cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS expenses (
                   id INTEGER  Primary Key,
                   amount REAL  NOT NUll,
                   description TEXT,
                   date TEXT  
                )
               
               """
)


con.commit()


def add_expness(amount, des, date):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")

        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            "INSERT INTO expenses (amount,description,date) VALUES (?,?,?) ",
            (amount, des, date),
        )
        con.commit()
        print("✅ Expense added successfully!")

    except ValueError as ve:
        print(f"❌ Invalid input: {ve}")
    except sqlite3.DatabaseError as bd_error:
        print(f"❌ Database error: {bd_error}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
    finally:
        if "conn" in locals():
            con.close()


def view_expness():
    cursor.execute("SELECT * FROM expenses")
    expneses = cursor.fetchall()

    if not expneses:
        print("📌 No expenses recorded yet.")

    print("\n📝 All Expenses:")
    print("-" * 50)
    print(f"{'ID':<5} {'Amount':<10} {'Description':<20} {'Date':<12}")
    print("-" * 50)

    for exp in expneses:
        print(f"{exp[0]:<5} {exp[1]:<10} {exp[2]:<20} {exp[3]:<12}")

    print("-" * 50)


def update_expness(update_id, new_amm, new_des, new_date):
    cursor.execute("SELECT * FROM expenses")
    expneses = cursor.fetchall()
    if not expneses:
        print(f"❌ Expense with ID {update_id} not found.")
        return
    # update using database where clause
    cursor.execute(
        """
                 UPDATE  expenses
                 SET amount = ?,description = ?,date = ?
                 WHERE id = ?
                  """,
        (new_amm, new_des, new_date, update_id),
    )

    con.commit()
    print(f"✅ Expense ID {update_id} updated successfully!")


def main():
    while True:
        print("1.Add Expense")
        print("2.View All Expense")
        print("3.Edit Expness")
        print("4.Delete Expness")
        print("5.View Expenses by Category/Date")
        print("6.Exit")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("welcome add Expness Section")
            ammont = float(input(print("ener your ammout")))
            description = input(print("enter short descriptiion"))
            date = input(print("enter date"))
            add_expness(ammont, description, date)
        elif choice == 2:
            print("welcome to view all Expnes Section")
            view_expness()
        elif choice == 3:
            print("welcome to Edit expness Section")
            update_id = input("enter id nunber for update")
            new_amm = input("enter new ammount")
            new_des = input("enter new description")
            new_date = input("enter a new date")
            update_expness(update_id, new_amm, new_des, new_date)
        elif choice == 4:
            print("welcome to Delete Expness Section")
        elif choice == 5:
            print("View Expenses by Category/Date")
        else:
            print("invalid chooice")


if __name__ == "__main__":
    main()
