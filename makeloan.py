import json
import os
import uuid

def make_loan():
    print("*************************************")
    print("         Loan Application Form       ")
    print("*************************************")

    # Generate a unique borrower ID
    borrower_id = str(uuid.uuid4())

    # Get user input for loan application
    name = input("1. Enter your full name: ")
    phone_number = input("2. Enter your phone number: ")
    monthly_income = float(input("3. Enter your monthly income: "))
    loan_amount = float(input("4. Enter the amount of loan you are requesting: "))
    loan_purpose = input("5. Enter the purpose of the loan: ")

    # Create a dictionary to store loan application details
    loan_application = {
        "borrower_id": borrower_id,
        "name": name,
        "phone_number": phone_number,
        "monthly_income": monthly_income,
        "loan_amount": loan_amount,
        "loan_purpose": loan_purpose,
    }

    # Create a folder named "Loan_Application_Forms" if it doesn't exist
    forms_folder = "Loan_Application_Forms"
    os.makedirs(forms_folder, exist_ok=True)

    # Save loan application details to a JSON file
    file_name = f"{forms_folder}/loan_application_{borrower_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(loan_application, json_file, indent=4)

    print("\nLoan application submitted successfully!")
    print(f"Your Borrower ID: {borrower_id}")
    print(f"Details saved in: {file_name}")

if __name__ == "__main__":
    make_loan()