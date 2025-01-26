import random
import string

def generate_password(length=8):
    # Define the character set for the password
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Set the desired length of the password
password_length = 12  # You can change this to any length you prefer
generated_password = generate_password(password_length)

print("Generated Password:", generated_password)
