import subprocess
import importlib

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

def execute_makeloan_script():
    try:
        subprocess.run(["python3", "makeloan.py"], check=True)
    except subprocess.CalledProcessError:
        print("Error executing makeloan.py")

def main():
    while True:
        display_banner()
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            execute_makeloan_script()
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
