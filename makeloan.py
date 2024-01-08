# makeloan.py

def make_loan():
    print("*************************************")
    print("         Loan Application Form       ")
    print("*************************************")

    # Get user input for loan application
    name = input("Enter your full name: ")
    amount = float(input("Enter the loan amount: "))
    duration = int(input("Enter the loan duration (in months): "))

    # Perform any additional logic related to making a loan
    # For example, you could calculate interest, update user accounts, etc.

    # Display confirmation message
    print("\nLoan application submitted successfully!")
    print(f"Name: {name}")
    print(f"Loan Amount: ${amount}")
    print(f"Loan Duration: {duration} months")

if __name__ == "__main__":
    make_loan()
