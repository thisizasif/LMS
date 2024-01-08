import json
import os
import uuid
import subprocess
import importlib

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print("\033[1;35m*********************************************\033[0m")
    print("\033[1;35m*        Welcome to Loan Management         *\033[0m")
    print("\033[1;35m*        Crafted by: thisizasif             *\033[0m")
    print("\033[1;35m*   GitHub: https://github.com/thisizasif   *\033[0m")
    print("\033[1;35m*********************************************\033[0m")

def main_menu():
    print("\n\033[1;34mOptions:\033[0m")  # \033[1;34m sets color to bright blue
    print("\033[1;33m1. Create Account\033[0m")  # \033[1;33m sets color to bright yellow
    print("\033[1;33m2. Make Loan\033[0m")
    print("\033[1;33m3. Make Payment\033[0m")
    print("\033[1;33m4. Loan Statement\033[0m")
    print("\033[1;33m5. Account Details\033[0m")
    print("\033[1;31m6. Exit\033[0m")  # \033[1;31m sets color to bright red

def load_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(f"Error: {module_name}.py not found.")
        return None

def execute_makeloan_script():
    clear_terminal()
    try:
        subprocess.run(["python3", "makeloan.py"], check=True)
    except subprocess.CalledProcessError:
        print("Error executing makeloan.py")
    input("Press Enter to continue...")  # Wait for user input before clearing

def execute_makepayment_script():
    clear_terminal()
    makepayment_module = load_module("makepayment")
    if makepayment_module:
        makepayment_module.make_payment()
    input("Press Enter to continue...")  # Wait for user input before clearing

def execute_loanstatement_script():
    clear_terminal()
    loanstatement_module = load_module("loanstatement")
    if loanstatement_module:
        loanstatement_module.view_statement()
    input("Press Enter to continue...")  # Wait for user input before clearing

def execute_accountdetails_script():
    clear_terminal()
    accountdetails_module = load_module("accountdetails")
    if accountdetails_module:
        accountdetails_module.view_account_details()
    input("Press Enter to continue...")  # Wait for user input before clearing

def create_account():
    clear_terminal()
    createaccount_module = load_module("createaccount")
    if createaccount_module:
        createaccount_module.create_account()
    input("Press Enter to continue...")  # Wait for user input before clearing

def main():
    while True:
        clear_terminal()
        display_banner()
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            execute_makeloan_script()
        elif choice == "3":
            execute_makepayment_script()
        elif choice == "4":
            execute_loanstatement_script()
        elif choice == "5":
            execute_accountdetails_script()
        elif choice == "6":
            print("Exiting the Loan Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()