import json
import os
import uuid
from datetime import datetime

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt):
    return input(prompt).strip()

def get_validated_input(prompt, validation_func):
    while True:
        user_input = get_user_input(prompt)
        try:
            validated_input = validation_func(user_input)
            return validated_input
        except ValueError as e:
            print(e)

def is_valid_email(email):
    # Simple email validation (you can use regex for a more robust validation)
    return "@" in email and "." in email

def load_existing_accounts():
    accounts_folder = "accounts"
    existing_accounts = []
    if os.path.exists(accounts_folder):
        for filename in os.listdir(accounts_folder):
            if filename.endswith(".json"):
                with open(os.path.join(accounts_folder, filename), "r") as json_file:
                    account_data = json.load(json_file)
                    existing_accounts.append(account_data.get("email", ""))
    return existing_accounts

def create_account():
    clear_terminal()
    print("\033[1;35m*************************************\033[0m")
    print("\033[1;35m       Create New Account          \033[0m")
    print("\033[1;35m*************************************\033[0m")

    # Load existing accounts to check for duplicate emails
    existing_emails = load_existing_accounts()

    # Get user input for account creation
    account_holder_name = get_user_input("Enter account holder's name: ")
    date_of_birth = get_validated_input("Enter date of birth (YYYY-MM-DD): ",
                                        lambda dob: datetime.strptime(dob, '%Y-%m-%d'))

    # Validate age (for example, you might want to set a minimum age for account holders)
    if (datetime.now() - date_of_birth).days < 365 * 18:
        print("You must be at least 18 years old to create an account.")
        return

    address = get_user_input("Enter address: ")
    email = get_validated_input("Enter email address: ", is_valid_email)

    # Check for duplicate email addresses
    if email in existing_emails:
        print("An account with this email already exists. Please use a different email address.")
        return

    initial_balance = get_validated_input("Enter initial balance: ",
                                          lambda balance: float(balance) if float(balance) >= 0 else None)

    # Account type selection
    account_types = ["Savings", "Checking", "Business"]
    account_type = get_validated_input(f"Select account type ({', '.join(account_types)}): ",
                                       lambda acc_type: acc_type if acc_type in account_types else None)

    # Generate a unique account number
    account_number = str(uuid.uuid4())

    # Create a dictionary to store account details
    account_details = {
        "account_number": account_number,
        "account_holder_name": account_holder_name,
        "date_of_birth": date_of_birth.strftime('%Y-%m-%d'),
        "address": address,
        "email": email,
        "balance": initial_balance,
        "account_type": account_type,
    }

    # Create an "accounts" folder if it doesn't exist
    accounts_folder = "accounts"
    os.makedirs(accounts_folder, exist_ok=True)

    # Save account details to a JSON file
    file_name = f"{accounts_folder}/account_{account_number}.json"
    with open(file_name, "w") as json_file:
        json.dump(account_details, json_file, indent=4)

    print("\nAccount created successfully!")
    print(f"Account Number: {account_number}")
    print(f"Details saved in: {file_name}")

if __name__ == "__main__":
    create_account()
  
