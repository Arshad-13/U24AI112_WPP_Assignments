#python program to find the orange cap winner in test cricket

test1 = [("Sachin", 0), ("Kohli", 150), ("Dhoni", 74)]
test2 = [("sachin", 143), ("Kohli", 0), ("Dhoni", 29)]

total = {test1[0][0]: test1[0][1] + test2[0][1], test1[1][0]: test1[1][1] + test2[1][1], test1[2][0]: test1[2][1] + test2[2][1]}

print(f"\nThe total score of the palyers are {total}")

orange_cap = max(total, key=total.get)

print(f"The orange cap winner is {orange_cap} with {total[orange_cap]} runs")