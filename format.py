import re


name = input("What's your name?").strip()
if matches := re.search(r"^(.+), *(.+)$", name, re.IGNORECASE):
  name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

#if "," in name: 
    #first, last = name.split(", ")
    #name = f"{first} {last}"
