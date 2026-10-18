import string

# Password Strength Analyzer
# Developed by: Haneen Jamil
# This program evaluates passwords using five basic security checks.

def check_password_strength(password):
    score = 0

    # Check 1: A longer password is generally harder to guess.
    if len(password) >= 8:
        score += 1

    # Check 2: Look for at least one uppercase letter.
    if any(ch.isupper() for ch in password):
        score += 1

    # Check 3: Look for at least one lowercase letter.
    if any(ch.islower() for ch in password):
        score += 1

    # Check 4: Check whether the password contains a number.
    if any(ch.isdigit() for ch in password):
        score += 1

    # Check 5: Look for a special character such as @, # or !.
    if any(ch in string.punctuation for ch in password):
        score += 1

    # Assign a strength level based on the total score.
    if score <= 2:
        return "WEAK - Consider improving your password."
    elif score <= 4:
        return "MODERATE - Your password could be stronger."
    else:
        return "STRONG - All five basic checks passed!"


# Main program starts here.
print("=" * 48)
print("       PASSWORD SECURITY ANALYZER")
print("          By Haneen Jamil")
print("=" * 48)

# Ask the user to enter a sample password.
password = input("\nEnter a test password: ")

# Evaluate the password and display the result.
result = check_password_strength(password)

print("\nPassword Security Report")
print("-" * 48)
print("Strength Assessment:", result)
print("-" * 48)
print("Thank you for using the Password Security Analyzer!")
