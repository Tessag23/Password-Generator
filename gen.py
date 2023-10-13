import random
import string

def generate_password(length=12):
    u = string.ascii_uppercase
    l = string.ascii_lowercase
    d = string.digits
    spchar = "!@#$%^&*()_-+=<>?/[]{}|"
    s = u + l + d + spchar
    password = ''.join(random.choice(s) for i in range(length))
    return password
password_length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(password_length))