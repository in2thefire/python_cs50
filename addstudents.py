import csv

name = input("What's your name? ")
house = input("What's your house? ")
home = input("What's your home? ")

with open("students.csv", "a",newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house", "home"])
    writer.writerow({"name": name, "house": house, "home": home})