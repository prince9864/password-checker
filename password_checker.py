"""
Password Strength Checker (simple version)
Type a password and the program tells you if it is WEAK, MEDIUM or STRONG.
Type 'quit' to stop.
"""

import string

# A small list of very common passwords
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123",
                    "admin", "letmein", "welcome", "iloveyou", "password1"]


def check_password(password):
    score = 0          # starts at 0, goes up to 100
    problems = []      # reasons why the password is weak

    # ---- 1. Length (up to 40 points) ----
    if len(password) >= 12:
        score += 40
    elif len(password) >= 8:
        score += 25
        problems.append("Make it 12 or more characters long.")
    else:
        score += 10
        problems.append("Too short. Use at least 8 characters.")

    # ---- 2. Character variety (10 points each) ----
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in string.punctuation:
            has_symbol = True

    if has_lower:
        score += 10
    else:
        problems.append("Add lowercase letters (a-z).")

    if has_upper:
        score += 10
    else:
        problems.append("Add uppercase letters (A-Z).")

    if has_digit:
        score += 10
    else:
        problems.append("Add numbers (0-9).")

    if has_symbol:
        score += 10
    else:
        problems.append("Add symbols like ! @ # $ %.")

    # ---- 3. Common patterns ----
    bad_pattern = False

    if password.lower() in COMMON_PASSWORDS:
        problems.append("This is a very common password. Hackers try it first!")
        score = 5
        bad_pattern = True

    for pattern in ["123", "abc", "qwe", "111", "000"]:
        if pattern in password.lower():
            problems.append("Contains an easy pattern: " + pattern)
            score -= 15
            bad_pattern = True
            break

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            problems.append("Same character repeated 3 times in a row.")
            score -= 10
            bad_pattern = True
            break

    if not bad_pattern:
        score += 20    # bonus for having no bad patterns

    # Keep the score between 0 and 100
    if score < 0:
        score = 0
    if score > 100:
        score = 100

    # ---- 4. Decide the result ----
    if score < 40:
        result = "WEAK"
    elif score < 70:
        result = "MEDIUM"
    else:
        result = "STRONG"

    return score, result, problems


# ---- Main program ----
print("=== Password Strength Checker ===")
print("Type 'quit' to exit.\n")

while True:
    password = input("Enter a password to check: ")

    if password.lower() == "quit":
        print("Goodbye!")
        break

    if password == "":
        print("Please type something.\n")
        continue

    score, result, problems = check_password(password)

    print("\nScore  :", score, "/ 100")
    print("Result :", result)

    if len(problems) > 0:
        print("How to improve:")
        for p in problems:
            print("  -", p)
    else:
        print("Great password! No problems found.")

    print()
