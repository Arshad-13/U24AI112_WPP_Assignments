# Find Digits
# You are given a number N, you need to print the number of positions where digits exactly
# divides N.
# Input format
# The first line contains T (number of test cases followed by T lines each containing N).
# Constraints
# 1 <= T <= 15
# 0 <= N <= 1010
# Output Format
# For each test case print the number of positions in N where digits in that number exactly
# divides the number N in separate line.
# Input
# 2
# 12
# 13
# Output
# 2
# 1
# Explanation

# Test case 1:
# 2 digits in the number 12 divides the number exactly.
# Test case 2:
# Only 1 digit in the number 13 divides the number exactly.

x = int(input("Enter the number of test cases: "))
for i in range(x):
    n = int(input("Enter the number: "))
    m = n
    count = 0
    while n > 0:
        rem = n % 10
        if rem != 0 and m % rem == 0:
            count += 1
        n = n // 10
    print(count)
    