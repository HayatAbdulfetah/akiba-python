def deposit(user, amount):
    if amount <= 0:
        print("❌ Amount must be positive.")
        return

    user["balance"] += amount
    user["total_deposited"] += amount
    record_transaction(user, "deposit", amount)
    print(f"Deposited: ${amount}")


def withdraw(user, amount):
    if amount <= 0:
        print("❌ Amount must be positive.")
        return

    if amount > user["balance"]:
        print("❌ Insufficient balance.")
        return
        
    # Challenge check: Verify remaining daily limit
    remaining_limit = user["daily_limit"] - user["withdrawn_today"]
    if amount > remaining_limit:
        print(f"❌ Rejected. Exceeds daily limit. Limit left: ${remaining_limit}")
        return

    user["balance"] -= amount
    user["withdrawn_today"] += amount
    user["total_withdrawn"] += amount
    record_transaction(user, "withdrawal", amount)
    print(f"Withdrew: ${amount}")


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
    print("\n===== TRANSACTION SUMMARY =====")
    
    for tx in user["transactions"]:
        print(f"{tx['type'].title()}: ${tx['amount']} | Balance After: ${tx['balance_after']}")

    print("-------------------------------")
    print(f"Total Deposited: ${user['total_deposited']}")
    print(f"Total Withdrawn: ${user['total_withdrawn']}")
    print(f"Final Balance:   ${user['balance']}")
    print("===============================")

# Configurable opening user data
user = {
    "balance": 1000,
    "daily_limit": 500,
    "withdrawn_today": 0,
    "total_deposited": 0,
    "total_withdrawn": 0,
    "transactions": []
}


# Test the program
deposit(user, 500)
withdraw(user, 200)
withdraw(user, 250)
withdraw(user, 100)

generate_summary(user)
