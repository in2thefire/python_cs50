with open("names.txt","r") as file:
    #lines = file.readlines()
    for line in file:
        print("Hello, ", line.rstrip())