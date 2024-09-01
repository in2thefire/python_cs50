students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherine"
}
for student in students:
    print(student, students[student], sep=" - ")


students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel terrier"},
    {"name" : "Draco", "house" : "Slytherine", "patronus" : None}
    ]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")