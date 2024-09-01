def main():
    print_column(3)
    square(4)
    print_raw(6)
    
def print_raw(lenght):
    print("?" * lenght)
    

def square(size):
    for _ in range(size):
        print("#" * size)
    print()

def print_column(height):
    for _ in range(height):
        print("#")
    print()
main()