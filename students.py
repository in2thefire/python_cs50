import csv

students = []

with open("students.csv") as file:
    #for line in file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"], "home": row["home"]})
        #name, house = line.rstrip().split(",")
        #student = {"name": name, "house": house}
        #student = {}
        #student["name"] = name
        #student["house"] = house
        #students.append(student)

#def get_name(student):
    #return student["name"]

#def get_house(student):
    #return student["house"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']} and from {student['home']}")