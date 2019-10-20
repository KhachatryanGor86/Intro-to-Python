num = input("Please input a number : ")

bool = False
while bool == True:
    if type(num) == 'int':
        bool = True

if num % 2 == 0:
    print("The inputed number is even")
else:
    print("The inputed number is odd")