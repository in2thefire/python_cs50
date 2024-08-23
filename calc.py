# x = int(input("What's x? "))
# y = int(input("What's y? "))
# print(x + y)

# print(int(input("What's x? ")) + int(input("What's y? ")))

#x = float(input("What's x? "))
#y = float(input("What's y? "))
#z = round(x + y)

#print(f"{z:,}")

def main():
    x = int(input("What's x? "))
    print("X squared is", square(x))

def square(n):
    return n * n

main()