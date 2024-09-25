import sys
#try:    
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("Add more arguments")

if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")

print("Hello, your name is", sys.argv[1])