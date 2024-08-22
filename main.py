# Ask user for his name
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
age = input ("How old are you? ")
print(f"Hello, {first}. Your surname is, {last}. Your age is, {age}")

