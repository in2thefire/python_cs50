import csv

name = input("What's your name? ")
house = input("What's your house? ")
home = input("What's your home? ")

with open("students.csv", "a",newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, house, home])