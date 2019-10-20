import math
AB = int(input("Input value for AB side --> "))
AC = int(input("Input value for AC side --> "))

BC = math.sqrt(AB**2 + AC**2)
print("The hypotenuse of the triangle ABC = ", BC)