# You are a student in a class of 10. Your class teacher assigns you a task of entering the
# names of all the students in the class. You finally want to display the names given the
# condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
# names and display them. [Hint: Slicing works when you are selecting maximum characters]

names = []
x = 1
while x != '0':
    x = (input("Enter the number of names: "))
    if len(x) > 15:
        print("Name longer than 15 char, enter within 15 chars")
        continue
    names.append(x)

names.pop()

for name in names:
    print(name[::-1])