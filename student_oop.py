def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Rawenclaw"
    '''if student[0] == "Padma":
        student[1] = "Rawenclaw"'''
    
    print(f"{student['name']} from {student['house']}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

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