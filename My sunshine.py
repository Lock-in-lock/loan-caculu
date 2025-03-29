import tkinter as tk
from tkinter import messagebox

def calculate_payment():
    try:
        loan_amount = float(loan_entry.get())
        interest_rate = float(interest_entry.get()) / 100 / 12
        loan_term = int(term_entry.get()) * 12

        if interest_rate == 0:
            monthly_payment = loan_amount / loan_term
        else:
            monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate) ** -loan_term)
        
        total_payment = monthly_payment * loan_term
        
        result_label.config(text=f"Monthly Payment: €{monthly_payment:.2f}\nTotal Payment: €{total_payment:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

root = tk.Tk()
root.title("Loan Calculator")
root.geometry("300x300")

tk.Label(root, text="Loan Amount (€):").pack(pady=5)
loan_entry = tk.Entry(root)
loan_entry.pack()

tk.Label(root, text="Annual Interest Rate (%):").pack(pady=5)
interest_entry = tk.Entry(root)
interest_entry.pack()

tk.Label(root, text="Loan Term (Years):").pack(pady=5)
term_entry = tk.Entry(root)
term_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_payment)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
