# Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists.

#1 feet = 12 inches
#1 feet = 0.3333 yards
#1 feet = 0.00018939 miles
#1 feet = 304.8 millimeters
#1 feet = 30.48 centimeters
#1 feet = 0.3048 meters
#1 feet = 0.0003048 kilometers

inches = 12
yards = 0.3333
miles = 0.00018939
millimeters = 304.8
centimeters = 30.48
meters = 0.3048
kilometers = 0.0003048

feet = int(input("Enter the length in feet: "))
convert = [inches, yards, miles, millimeters, centimeters, meters, kilometers]
conversions = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
print(conversions)
conversion = int(input("Enter the conversion: "))

print("The length in", conversions[conversion - 1], "is", feet*convert[conversion - 1])