import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, ttk

def calculate_interest():
    try:
        loan_amount = float(entry_loan_amount.get())
        monthly_payment = float(entry_monthly_payment.get())
        num_payments = int(entry_num_payments.get())

        total_interest = (monthly_payment * num_payments) - loan_amount
        interest_percentage = (total_interest / loan_amount) * 100
        monthly_interest = total_interest / num_payments

        result_label.config(text=f"Total Interest: {total_interest:.2f} INR\n"
                                  f"Interest Percentage: {interest_percentage:.2f}%\n"
                                  f"Monthly Interest: {monthly_interest:.2f} INR")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Loan Interest Calculator")
root.geometry("400x300")

# Create and place widgets
style = ttk.Style()
style.configure("TLabel", padding=10)
style.configure("TButton", padding=10)

label_loan_amount = ttk.Label(root, text="Loan Amount (INR):")
label_monthly_payment = ttk.Label(root, text="Monthly Payment (INR):")
label_num_payments = ttk.Label(root, text="Number of Payments:")

label_loan_amount.grid(row=0, column=0, sticky=tk.E)
label_monthly_payment.grid(row=1, column=0, sticky=tk.E)
label_num_payments.grid(row=2, column=0, sticky=tk.E)

entry_loan_amount = Entry(root)
entry_monthly_payment = Entry(root)
entry_num_payments = Entry(root)

entry_loan_amount.grid(row=0, column=1, padx=10, pady=10)
entry_monthly_payment.grid(row=1, column=1, padx=10, pady=10)
entry_num_payments.grid(row=2, column=1, padx=10, pady=10)

calculate_button = Button(root, text="Calculate Interest", command=calculate_interest, bg="#4CAF50", fg="white")
calculate_button.grid(row=3, column=0, columnspan=2, pady=15)

result_label = Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
