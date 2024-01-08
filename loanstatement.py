import tdesktop as td

def calculate_interest():
    try:
        loan_amount = float(entry_loan_amount.get())
        monthly_payment = float(entry_monthly_payment.get())
        num_payments = int(entry_num_payments.get())

        total_interest = (monthly_payment * num_payments) - loan_amount
        interest_percentage = (total_interest / loan_amount) * 100
        monthly_interest = total_interest / num_payments

        result_label.set(f"Total Interest: {total_interest:.2f} INR\n"
                         f"Interest Percentage: {interest_percentage:.2f}%\n"
                         f"Monthly Interest: {monthly_interest:.2f} INR")
    except ValueError:
        result_label.set("Please enter valid numeric values.")

# Create a desktop window
window = td.Window()

# Create and place widgets
window.add(td.Label("Loan Amount (INR):"), 1, 1)
window.add(td.Label("Monthly Payment (INR):"), 2, 1)
window.add(td.Label("Number of Payments:"), 3, 1)

entry_loan_amount = window.add(td.Entry(), 1, 2)
entry_monthly_payment = window.add(td.Entry(), 2, 2)
entry_num_payments = window.add(td.Entry(), 3, 2)

calculate_button = window.add(td.Button("Calculate Interest", calculate_interest), 4, 1, 2)

result_label = window.add(td.Label(""), 5, 1, 2)

# Run the desktop application
window.run()
