import random
import string

def generate_password(length=8):
    if length < 4:
        raise ValueError("Password length must be at least 4")

   
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()_+-="

    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    all_chars = uppercase + lowercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    
    random.shuffle(password)

    return "".join(password)


print("Generated Password:", generate_password(10))
