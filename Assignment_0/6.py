#python program to reverse of a given number

num = int(input("Enter a number to reverse it: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print("The reverse of a number is: ", rev)