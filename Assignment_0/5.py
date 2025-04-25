#python program to print table of a number

num = int(input("Enter a number to find its table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)