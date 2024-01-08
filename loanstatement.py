def calculate_interest(loan_amount, monthly_payment, num_payments):
    try:
        loan_amount = float(loan_amount)
        monthly_payment = float(monthly_payment)
        num_payments = int(num_payments)

        total_interest = (monthly_payment * num_payments) - loan_amount
        interest_percentage = (total_interest / loan_amount) * 100
        monthly_interest = total_interest / num_payments

        return total_interest, interest_percentage, monthly_interest
    except ValueError:
        return None

def main():
    print("Loan Interest Calculator")

    loan_amount = input("Enter Loan Amount (INR): ")
    monthly_payment = input("Enter Monthly Payment (INR): ")
    num_payments = input("Enter Number of Payments: ")

    result = calculate_interest(loan_amount, monthly_payment, num_payments)

    if result is not None:
        total_interest, interest_percentage, monthly_interest = result
        print(f"\nTotal Interest: {total_interest:.2f} INR")
        print(f"Interest Percentage: {interest_percentage:.2f}%")
        print(f"Monthly Interest: {monthly_interest:.2f} INR")
    else:
        print("\nPlease enter valid numeric values.")

if __name__ == "__main__":
    main()
