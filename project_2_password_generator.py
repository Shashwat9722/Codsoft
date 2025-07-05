import random
import string

def generate_password(length=12):
    if length < 4:
        print("Password length should be at least 4.")
        return ""
    # Ensure the password has at least one lowercase, uppercase, digit, and symbol
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    # Fill the rest of the password length with random choices
    chars += random.choices(
        string.ascii_letters + string.digits + string.punctuation,
        k=length-4
    )
    random.shuffle(chars)
    return ''.join(chars)

length = int(input("Enter password length: "))
password = generate_password(length)
if length >= 4:
    print("Generated password:", password)