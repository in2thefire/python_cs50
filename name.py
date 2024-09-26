import sys
#try:    
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("Add more arguments")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#   sys.exit("Too many arguments")
for arg in sys.argv[1:3]:
    print("Hello, your name is", arg)