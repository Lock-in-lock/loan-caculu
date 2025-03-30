import datetime
import tkinter as tk
from tkinter import messagebox


def add_expense(expense_file, item, cost):
    date = datetime.date.today().strftime("%Y-%m-%d")

    with open(expense_file, "a") as f:
        f.write(f"{date},{item},{cost}\n")

    messagebox.showinfo("Success", "Expense added successfully!")


def view_expenses(expense_file, text_area):
    try:
        with open(expense_file, "r") a:
            text_area.delete(1.0, tk.END)  
            text_area.insert(tk.END, "Date,Item,Cost\n")
            for line in f:
                text_area.insert(tk.END, line)
    except FileNotFoundError:
        messagebox.showwarning("No Expenses", "No expenses recorded yet.")


def on_add_button_click(expense_file, item_entry, cost_entry):
    item = item_entry.get()
    try:
        cost = float(cost_entry.get())
        add_expense(expense_file, item, cost)
        item_entry.delete(0, tk.END)
        cost_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid cost.")


def main():
    expense_file = "expenses.csv"

    
    root = tk.Tk()
    root.title("Expense Tracker")

    
    item_label = tk.Label(root, text="Item:")
    item_label.pack(padx=10, pady=5)

    item_entry = tk.Entry(root, width=40)
    item_entry.pack(padx=10, pady=5)

    cost_label = tk.Label(root, text="Cost:")
    cost_label.pack(padx=10, pady=5)

    cost_entry = tk.Entry(root, width=40)
    cost_entry.pack(padx=10, pady=5)

    
    add_button = tk.Button(root, text="Add Expense", command=lambda: on_add_button_click(expense_file, item_entry, cost_entry))
    add_button.pack(padx=10, pady=10)

    view_button = tk.Button(root, text="View Expenses", command=lambda: view_expenses(expense_file, text_area))
    view_button.pack(padx=10, pady=5)

    
    text_area = tk.Text(root, width=50, height=10)
    text_area.pack(padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
