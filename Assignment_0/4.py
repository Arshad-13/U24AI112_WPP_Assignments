#python program to swap to numbers without using third variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The numbers before swapping are: ", num1, num2)
num1, num2 = num2, num1
print("The swapped numbers are: ", num1, num2)