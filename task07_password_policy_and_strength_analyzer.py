# 1. Check minimum length
def check_length(password, min_length=8):
    return len(password) >= min_length

# 2. Check uppercase letters
def check_uppercase(password):
    return any(char.isupper() for char in password)

# 3. Check lowercase letters
def check_lowercase(password):
    return any(char.islower() for char in password)

# 4. Check digits
def check_digits(password):
    return any(char.isdigit() for char in password)

# 5. Check special characters
def check_special(password):
    return any(not char.isalnum() for char in password)

# Analyze the password
def analyze_password(password, min_length=8):
    report = {
        "Minimum length": check_length(password, min_length),
        "Uppercase letters": check_uppercase(password),
        "Lowercase letters": check_lowercase(password),
        "Digits": check_digits(password),
        "Special characters": check_special(password)
    }

    passed = all(report.values())

    return {
        "report": report,
        "strong": passed
    }


# Test fictional passwords
passwords = [
    "Hello123!",
    "hello",
    "HELLO123!",
    "HelloWorld!",
    "abc12345",
    "MyPass@2026"
]

for password in passwords:
    result = analyze_password(password)

    print("\nPassword:", password)
    print("-----------------------------")

    for requirement, passed in result["report"].items():
        if passed:
            print(f"{requirement}: PASS")
        else:
            print(f"{requirement}: FAIL")

    print("Password strength:", "Strong" if result["strong"] else "Weak")
