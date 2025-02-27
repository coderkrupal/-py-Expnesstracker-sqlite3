import sqlite3
import pyfiglet
from colorama import Fore

text = pyfiglet.figlet_format("ExpnessTracker")
print(Fore.LIGHTGREEN_EX + text)
con = sqlite3.connect("expnesstracker.db")
cursor = con.cursor()

cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS userdata(
                   id INTEGER  Primary Key,
                   amount REAL  NOT NUll,
                   category TEXT  NOT NUll,
                   description TEXT,
                   date TEXT  
                )
               
               """
)


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
        elif choice == 2:
            print("welcome to view all Expnes Section")
        elif choice == 3:
            print("welcome to Edit expness Section")
        elif choice == 4:
            print("welcome to Delete Expness Section")
        elif choice == 5:
            print("View Expenses by Category/Date")
        else:
            print("invalid chooice")


if __name__ == "__main__":
    main()
