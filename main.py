import os
import importlib

def clear_screen():
    # Clear screen command for different operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print("*************************************")
    print("     Welcome to Loan Management      ")
    print("         Crafted by: thisizasif      ")
    print("    GitHub: https://github.com/thisizasif")
    print("*************************************")

def main_menu():
    print("\nOptions:")
    print("1. Make Loan")
    print("2. Make Payment")
    print("3. Loan Statement")
    print("4. Account Details")
    print("5. Exit")

def load_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(f"Error: {module_name}.py not found.")
        return None

def main():
    while True:
        clear_screen()
        display_banner()
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            makeloan_module = load_module("makeloan")
            if makeloan_module:
                makeloan_module.make_loan()
        elif choice == "2":
            makepayment_module = load_module("makepayment")
            if makepayment_module:
                makepayment_module.make_payment()
        elif choice == "3":
            loanstatement_module = load_module("loanstatement")
            if loanstatement_module:
                loanstatement_module.view_statement()
        elif choice == "4":
            accountdetails_module = load_module("accountdetails")
            if accountdetails_module:
                accountdetails_module.view_account_details()
        elif choice == "5":
            print("Exiting the Loan Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
