import re

email = input("What's your email address? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
#1
#if "@" in email and "." in email:
    #print("Valid email address")
#else:
    #print("Invalid email address")

#2
#username, domain = email.split("@")

#if username and domain.endswith(".edu"):
    #print("Valid email address")
#else:
    #print("Invalid email address")