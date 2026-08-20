# 1.Arithematic Operators
marks=90
attendance=80
#Arithematic operators
print("--ARITHEMATIC OPERATIONS--")
print("marks after bonus:",marks+10)
print("marks after lost:",marks-10)
print("Double marks:",marks*2)
print("Half marks:",marks/2)
print("remainder of marks after dividing by 7:",marks%7)
print("floor division of marks by 7:",marks//7)
print("marks raised to the power of 2:",marks**2)
# comparison operators
print("--COMPARISON OPERATORS--")
print("Passed:",marks>=40)
print("Failed:",marks<40)
print("perfect score:",marks==100)
# logical operators
print("--LOGICAL OPERATORS--")
print("Eligible:",marks>=40 and attendance>75)
print("Not eligible:",marks<40 or attendance<75)
print("not failed:",not(marks<40))