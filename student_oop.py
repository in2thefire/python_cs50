class Student:
    def __init__(self, name, house, patronus):
        if not name: #if name == ""
            raise ValueError("Missing name ")
        if house not in ["Gryffindor", "Rawenclaw","Slytherin","Hufflepuff"]:
            raise ValueError("Invaid House")
        self.name = name
        self.house = house
        self.patronus = patronus
    def __str__(self):
        return f"{self.name} from {self.house} with {self.patronus} as a patronus"
def main():
    student = get_student()
    print(student)
'''   if student.name == "Padma":
     student.house = "Rawenclaw"'''

'''if student[0] == "Padma":
        student[1] = "Rawenclaw"'''
    
    #print(f"{student.name} from {student.house}")#

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

'''def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student'''

'''def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}'''

'''def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student'''
    
'''def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]'''

if __name__ == "__main__":
    main()  