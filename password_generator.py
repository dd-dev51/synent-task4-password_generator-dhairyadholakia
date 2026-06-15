import random
import string

length = int(input("Enter password length: "))

all_characters = (
    string.ascii_uppercase +
    string.ascii_lowercase +
    string.digits +
    string.punctuation
)

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:")
print(password)