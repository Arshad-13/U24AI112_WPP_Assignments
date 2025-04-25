# 1. Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.

x = input("Enter a word: ")
for i in range(len(x)):
    if i % 2 == 0:
        print(x[i], end="")
    else:
        print(x[i].upper(), end="")