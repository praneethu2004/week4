

import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with a random mix of all character sets
    if length > 4:
        all_chars = lower + upper + digits + special
        password.extend(random.choice(all_chars) for _ in range(length - 4))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

def generate_passwords(length, count):
    return [generate_password(length) for _ in range(count)]

def main():
    print("Welcome to the Secure Password Generator!")
    try:
        length = int(input("Enter the length of the passwords (minimum 8): "))
        count = int(input("Enter the number of passwords to generate: "))
        
        passwords = generate_passwords(length, count)
        for i, password in enumerate(passwords, 1):
            print(f"Password {i}: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
