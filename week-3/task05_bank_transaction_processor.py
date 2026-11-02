def deposit(user, amount):
    if amount <= 0:
        print("Amount must be positive.")
        return user["balance"]

    user["balance"] += amount
    record_transaction(user, "deposit", amount)

    return user["balance"]

def withdraw(user, amount):
    if amount <= 0:
        print("Amount must be positive.")
        return user["balance"]

    if amount > user["balance"]:
        print("Insufficient balance.")
        return user["balance"]

    user["balance"] -= amount
    record_transaction(user, "withdrawal", amount)

    return user["balance"]

def check_balance(user):
    return user["balance"]

def record_transaction(user, transaction_type, amount):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": user["balance"]
    }

    user["transactions"].append(transaction)

def generate_summary(user):
    total_deposited = 0
    total_withdrawn = 0

    print("\n===== TRANSACTION SUMMARY =====")

    for transaction in user["transactions"]:
        print(
            f"{transaction['type'].title()}: "
            f"{transaction['amount']} | "
            f"Balance: {transaction['balance_after']}"
        )

        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    print("-------------------------------")
    print(f"Total deposited: {total_deposited}")
    print(f"Total withdrawn: {total_withdrawn}")
    print(f"Final balance: {user['balance']}")
    print("===============================")


user = {
    "balance": 1000,
    "transactions": []
}

deposit(user, 500)
withdraw(user, 200)
deposit(user, 300)
withdraw(user, 100)

print("Current balance:", check_balance(user))

generate_summary(user)
