import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ""
length = int(input ("How long? "))

for i in range(length):
    password += secrets.choice(characters)

print(password)