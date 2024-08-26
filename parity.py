def main():
    x = int(input("What's x? "))
    if parity(x):
        print("Even")
    else:
        print("Odd")
def parity(n):
     #return True if n % 2 == 0 else False
     return n % 2 == 0
main()