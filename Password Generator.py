import random
import string

length = 8
uppercase = True
lowercase = True
numbers = True
symbols = True


characters = ''
if lowercase:
    characters += string.ascii_lowercase
elif uppercase:
    characters += string.ascii_uppercase
elif numbers:
    characters += string.digits
elif symbols:
    characters += string.punctuation

elif not characters :
    raise ValueError("Must include atleast one character type.")

password = ' '.join(random.sample(characters,length))

print(password)