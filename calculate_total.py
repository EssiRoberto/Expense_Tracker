expenses = [
    {"item": "Groceries", "amount": 45.50},
    {"item": "Transport", "amount": 15.00},
    {"item": "Coffee", "amount": 4.50}
]

total = sum(e["amount"] for e in expenses)
print(f"Total spent: ${total:.2f}")
