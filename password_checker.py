import re

def password_complexity_checker(password):
    # Initialize score
    score = 0
    feedback = []

    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Check each criterion and update score
    if length_criteria:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if number_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine password strength
    if score >= 6:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    # Provide feedback
    if feedback:
        feedback_message = "Suggestions to improve your password:\n" + "\n".join(feedback)
    else:
        feedback_message = "Your password is strong."

    return strength, feedback_message

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its complexity: ")
    strength, feedback_message = password_complexity_checker(password)
    print(f"Password Strength: {strength}")
    print(feedback_message)
